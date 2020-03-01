
# Taking a Deep Look Into the Outbreak of Corona Virus

The purpose of this paper is perform data analysis on the data set ***Novel Corona Virus 2019*** to gather insights on the outbreak of the Corona Virus to date(2/22/2020).

## Data Set
**Dataset Citation:**
Kaggle.com. (2020). _Novel Corona Virus 2019 Dataset_. [online] Available at: https://www.kaggle.com/sudalairajkumar/novel-corona-virus-2019-dataset [Accessed 1 Mar. 2020].

To begin our analysis, let's take a look at the schema of the dataset, the format is as follows

SNo|ObservationDate|Province/State|Country/Region|Last Update|Confirmed|Deaths|Recovered
| --- | --- | --- | --- | --- | --- | --- | --- |
1|01/22/2020|Anhui|Mainland China|1/22/2020 17:00|1.0|0.0|0.0
2|01/22/2020|Beijing|Mainland China|1/22/2020 17:00|14.0|0.0|0.0
3|01/22/2020|Chongqing|Mainland China|1/22/2020 17:00|6.0|0.0|0.0


## Taking a Look at the Impact for All Countries
Since the data for each province is not present in all dates(some provinces were not continuiously recordered for all dates), we can not simply get the last date(2/22/2020) and aggregate the values on that date, instead let's get the last entry for each province and aggregate confirmed # for the provinces; we can safely assume the last entry for each province is the latest date for the last recorded.

From the table below, we already see some interesting findings. Mainland China accounts for 98% of the all Corona Virus cases and others(which construct of Diamond Princess cruise ship and Cruise Ship) account for 0.89% of overall case. We can already tell China already had an severe outbreak, and investigating further could give us some useful information about how the outbreak will look like.

```python
# let's aggregate by the country instead of province  
df_by_country = df.groupby(['Country/Region', 'Province/State']).last()\  
                  .groupby(level=0).sum()[['Confirmed', 'Deaths', 'Recovered']]  
df_by_country['Confirmed %'] = df_by_country['Confirmed'] / sum(df_by_country['Confirmed']) * 100  
df_by_country['Death Ratio %'] = df_by_country['Deaths'] / df_by_country['Confirmed'] * 100  
print(df_by_country.sort_values(by=['Confirmed'], ascending=False))  
print(df.groupby(['Country/Region', 'Province/State']).last()[['Confirmed']].sort_values(by=['Confirmed'], ascending=False))
```

Data for confirmed cases by country

Country/Region|Confirmed|Deaths|Recovered|Confirmed %|Death Ratio %
| --- | --- | --- | --- | --- | --- |
Mainland China|76922.0|2441.0|22687.0|98.842245|3.173344
Others|695.0|2.0|1.0|0.893052|0.287770
Hong Kong|69.0|2.0|6.0|0.088663|2.898551
US|60.0|0.0|5.0|0.077098|0.000000
Taiwan|26.0|1.0|2.0|0.033409|3.846154
Australia|22.0|0.0|11.0|0.028269|0.000000
Canada|12.0|0.0|3.0|0.015420|0.000000
Macau|10.0|0.0|6.0|0.012850|0.000000
Germany|5.0|0.0|0.0|0.006425|0.000000
Israel|1.0|0.0|0.0|0.001285|0.000000
Lebanon|1.0|0.0|0.0|0.001285|0.000000

Data for confirmed cases by province

Country/Region | Province/State                          |Confirmed
| --- | --- | --- |
Mainland China |Hubei                                   |64084.0
.               |Guangdong                                |1339.0
.               |Henan                                    |1270.0
.               |Zhejiang                                 |1205.0
.               |Hunan                                    |1013.0
.               |Anhui                                     |989.0
.               |Jiangxi                                   |934.0
.               |Shandong                                  |750.0
Others         |Diamond Princess cruise ship              |634.0
Mainland China |Jiangsu                                   |631.0
.               |Chongqing                                 |573.0
.               |Sichuan                                   |526.0
.               |Heilongjiang                              |479.0
.               |Beijing                                   |399.0
.               |Shanghai                                  |335.0
.               |Hebei                                     |309.0
.               |Fujian                                    |293.0
.               |Guangxi                                   |249.0
.               |Shaanxi                                   |245.0
.               |Yunnan                                    |174.0
.               |Hainan                                    |168.0
.               |Guizhou                                   |146.0
.               |Tianjin                                   |135.0
.               |Shanxi                                    |132.0
.               |Liaoning                                  |121.0
.               |Jilin                                      |91.0
.               |Gansu                                      |91.0
.               |Xinjiang                                   |76.0
.               |Inner Mongolia                             |75.0
.               |Ningxia                                    |71.0
Hong Kong      |Hong Kong                                  |69.0
Others         |Cruise Ship                                |61.0
Taiwan         |Taiwan                                     |26.0
Mainland China |Qinghai                                    |18.0
US             |Ashland, NE                                |11.0
.               |Omaha, NE (From Diamond Princess)          |11.0
Macau          |Macau                                      |10.0
Australia      |From Diamond Princess                       |7.0
Canada         |British Columbia                            |6.0
US             |Travis, CA (From Diamond Princess)          |5.0
.               |Travis, CA                                  |5.0
Germany        |Bavaria                                     |5.0
Australia      |Queensland                                  |5.0
.               |New South Wales                             |4.0
.               |Victoria                                    |4.0
Canada         |Ontario                                     |3.0
US             |Chicago, IL                                 |2.0
.               |Santa Clara, CA                             |2.0
.               |San Diego County, CA                        |2.0
.               |San Benito, CA                              |2.0
.               |Lackland, TX (From Diamond Princess)        |2.0
.               |Lackland, TX                                |2.0
.               |Illinois                                    |2.0
.               |California                                  |2.0
Australia      |South Australia                             |2.0
Canada         |Toronto, ON                                 |2.0
US             |Chicago                                     |1.0
.               |Arizona                                     |1.0
Israel         |From Diamond Princess                       |1.0
Mainland China |Tibet                                       |1.0
US             |Tempe, AZ                                   |1.0
.               |Seattle, WA                                 |1.0
Canada         |London, ON                                  |1.0
US             |Sacramento County, CA                       |1.0
.               |San Antonio, TX                             |1.0
.               |Humboldt County, CA                         |1.0
.               |Orange, CA                                  |1.0
.               |Madison, WI                                 |1.0
.               |Los Angeles, CA                             |1.0
.               |Boston, MA                                  |1.0
Lebanon        |None                                        |1.0
US             |Washington                                  |1.0

## Taking a Look at the Impact Excluding Mainland China and the Cruises
Since Mainland China and Others(Cruises) contain the most confirmed Corona Viruse cases, we can take a more detailed look at that later. Let's first take a breif look at some of the other impacted countries that also has the potential to outbreak. These contries include and in order of # confirmed cases: Hong Kong, US, Taiwan, Australia, Canada, Macau, Germany, Israel, and Lebanon.
```python
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
```

<p float="left">
  <img src="charts/chart1.png" width="400" />
  <img src="charts/chart2.png" width="400" /> 
</p>


## Taking a look at the Impact of Each Province in Mainland China and the Cruises

Let's investigate further at each of the provinces at Mainland China and Cruises to get a general idea of what an outbreak would look like.

```python
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
```

<p float="left">
  <img src="charts/chart3.png" width="200" /> 
  <img src="charts/chart4.png" width="200" /> 
  <img src="charts/chart5.png" width="200" /> 
  <img src="charts/chart6.png" width="200" /> 
  <img src="charts/chart7.png" width="200" /> 
  <img src="charts/chart8.png" width="200" /> 
  <img src="charts/chart9.png" width="200" /> 
  <img src="charts/chart10.png" width="200" /> 
  <img src="charts/chart11.png" width="200" /> 
  <img src="charts/chart12.png" width="200" /> 
  <img src="charts/chart13.png" width="200" /> 
  <img src="charts/chart14.png" width="200" /> 
  <img src="charts/chart15.png" width="200" /> 
  <img src="charts/chart16.png" width="200" /> 
  <img src="charts/chart17.png" width="200" /> 
  <img src="charts/chart18.png" width="200" /> 
  <img src="charts/chart19.png" width="200" /> 
  <img src="charts/chart20.png" width="200" /> 
  <img src="charts/chart21.png" width="200" /> 
  <img src="charts/chart22.png" width="200" /> 
  <img src="charts/chart23.png" width="200" /> 
  <img src="charts/chart24.png" width="200" /> 
  <img src="charts/chart25.png" width="200" /> 
  <img src="charts/chart26.png" width="200" /> 
  <img src="charts/chart27.png" width="200" /> 
  <img src="charts/chart28.png" width="200" /> 
  <img src="charts/chart29.png" width="200" /> 
  <img src="charts/chart30.png" width="200" /> 
  <img src="charts/chart31.png" width="200" /> 
  <img src="charts/chart32.png" width="200" /> 
  <img src="charts/chart33.png" width="200" /> 
  <img src="charts/chart34.png" width="200" /> 
  <img src="charts/chart35.png" width="200" /> 
</p>

## Taking a look at the Impact of Each Province in Mainland China and the Cruises (Aggregation)

There are 3 visible stages in the graphs:
1) In the initial period the graph concaves upward, showing a exponential growth in # of confirmed cases (usually lasts for approximately 10 days).
2) There's a period of steady growth which looks linear (usually lasts for approximately 10 days).
3) The growth started to slow down and flatten out, showing a dramatic decrease in rate for # of confirmed cases (usually lasts for approximately 10 days).

The breakout cycle is approximately 30 days until the # of confirmed cases get under control.

```python
# plot distribution of corona virus for china and the cruises; individually as well as the aggregated graph  
for region in ["Others", "Mainland China"]:  
    df_selected_region = df[df['Country/Region'] == region]  
    provinces = df_selected_region['Province/State'].unique()  
    x = y = None  
  
    def format_ticks(value, tick_number):  
        return x[tick_number] if tick_number % 3 == 0 else ""  
  
    # ... Code for next section ...
    
    # Code for this section
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
```

![](charts/chart36.png)

## Conclusion
There are a lot of useful information that can be drawn based on the findings in this project, they are as follows:
1. Mainland China accounts for 98% of the all Corona Virus cases and others(which construct of Diamond Princess cruise ship and Cruise Ship) account for 0.89%
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTk1Mzg4NTc2NywxMjM1MzM4OTMxLC0xNT
MwMTQzNzIxLC0yMTA3MjgwOTYzLDU3Mzc4Mzg4OSwtNjAxNjAx
NjAsMTgxNzU1MDM5MSwxMTYwMTYwNDI5LC0xNDI2NjExMzgxLC
0xNjkwOTk4NzAxLC0yOTI0NTM2MSw5MjAyNDEzNzcsMTA1NzA3
ODY3N119
-->