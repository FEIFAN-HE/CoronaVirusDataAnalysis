import os
import pandas as pd
import matplotlib.pyplot as plt
import shutil
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

# Create new folder
folder = "./DataVisualization"
try:
    shutil.rmtree(folder)
except Exception:
    pass
os.makedirs(folder)

# read data set
df = pd.read_csv('covid_19_data.csv')

# let's aggregate by the country instead of province
df_by_country = df.groupby(['Country/Region', 'Province/State']).last()\
                  .groupby(level=0).sum()[['Confirmed', 'Deaths', 'Recovered']]
df_by_country['Confirmed %'] = df_by_country['Confirmed'] / sum(df_by_country['Confirmed']) * 100
df_by_country['Death Ratio %'] = df_by_country['Deaths'] / df_by_country['Confirmed'] * 100
print(df_by_country.sort_values(by=['Confirmed'], ascending=False))
print(df.groupby(['Country/Region', 'Province/State']).last()[['Confirmed']].sort_values(by=['Confirmed'], ascending=False))

# make a png plot same with incremental number
def plot_grap():
    for i in range(1, 100000):
        strFile = folder + "/chart%d.png" % i
        if not os.path.isfile(strFile):
            plt.savefig(strFile)
            return

# plot bar graph and pie chart for confirmed case of corona virus distribution excluding the cruises and china
df_by_country_excl = df_by_country[~df_by_country.index.isin(['Others', 'Mainland China'])]
x, y = list(df_by_country_excl.index), list(df_by_country_excl['Confirmed'])

plt.subplots()
plt.title("Corona Virus Geographic Distribution(Excluding China and Cruises)")
plt.barh(x, y)
plot_grap()

plt.subplots()
plt.title("Corona Virus Geographic Distribution(Excluding China and Cruises)")
patches, texts = plt.pie(y)
plt.legend(patches, x, loc=4)
plt.axis('equal')
plot_grap()

# plot distribution of corona virus for china and the cruises; individually as well as the aggregated graph
for region in ["Others", "Mainland China"]:
    df_selected_region = df[df['Country/Region'] == region]
    provinces = df_selected_region['Province/State'].unique()
    x = y = None

    def format_ticks(value, tick_number):
        return x[tick_number] if tick_number % 3 == 0 else ""

    for province in provinces:
        fig, ax = plt.subplots()
        df_by_prov = df[df['Province/State'] == province].ffill()
        x, y = list(df_by_prov['ObservationDate']), list(df_by_prov['Confirmed'])
        plt.plot(x, y)
        fig.autofmt_xdate()
        ax.xaxis.set_major_formatter(plt.FuncFormatter(format_ticks))
        plt.title("Corona Virus Confirmed Count for %s - %s" %(region, province))
        plot_grap()

    if region == "Mainland China":
        fig, ax = plt.subplots()
        plt.title("Corona Virus Rate of Growth")
        for province in provinces:
            df_by_prov = df[df['Province/State'] == province].ffill()
            x, y = list(df_by_prov['ObservationDate']), list(df_by_prov['Confirmed'] / df_by_prov['Confirmed'].max())
            plt.plot(x, y)
            fig.autofmt_xdate()
            ax.xaxis.set_major_formatter(plt.FuncFormatter(format_ticks))
        ax.legend()
        plot_grap()
