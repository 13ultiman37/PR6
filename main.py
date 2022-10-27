import pandas as pd
import numpy as np
import plotly.graph_objs as go

data = pd.read_csv("ECDCCases.csv", delimiter=',')
print("\n---------- Количество пропущенных значений: ----------")
print(data.isna().sum())
print("\n---------- Количество пропущенных значений, %: ----------")
for column in data.columns:
    missing = np.mean(data[column].isna() * 100)
    print(f"{column} : {round(missing, 1)}%")

data.drop('Cumulative_number_for_14_days_of_COVID-19_cases_per_100000', axis=1, inplace=True)
data.drop('geoId', axis=1, inplace=True)

med = data.popData2019.median()
data.countryterritoryCode.fillna(med, inplace=True)
data.popData2019.fillna('other', inplace=True)

print("\n---------- После обработки данных: ----------")
print(data.isna().sum())
print(data.describe())

cases = data['cases'].values
cases_trace = go.Box(y=cases, name="Cases")
deaths = data['deaths'].values
deaths_trace = go.Box(y=deaths, name="Deaths")
popData = data['popData2019'].values
popData_trace = go.Box(y=popData, name="Population Data")

boxes = [cases_trace, deaths_trace, popData_trace]
figure1 = go.Figure(cases_trace)
figure1.update_layout(title="Проверка выбросов",
                      xaxis=dict(title="Показатель"),
                      yaxis=dict(title="Величина"),
                      width=900,
                      height=900)
figure1.show()

figure2 = go.Figure(deaths_trace)
figure2.update_layout(title="Проверка выбросов",
                      xaxis=dict(title="Показатель"),
                      yaxis=dict(title="Величина"),
                      width=900,
                      height=900)
figure2.show()

figure3 = go.Figure(popData_trace)
figure3.update_layout(title="Проверка выбросов",
                      xaxis=dict(title="Показатель"),
                      yaxis=dict(title="Величина"),
                      width=900,
                      height=900)
figure3.show()

data.loc[data["deaths"] < 0, "deaths"] = abs(data.loc[data["deaths"] < 0, "deaths"])
data.loc[data["cases"] < 0, "cases"] = abs(data.loc[data["cases"] < 0, "cases"])
print("\n---------- Замена отрицательных значений модулем: ----------")
print(data.describe())

deathsOver3k = data.loc[data["deaths"] >= 3000, "countriesAndTerritories"]
print("\n---------- Страны с >3000 смертей в день: ----------")
print(deathsOver3k)
print("\n---------- Количество стран с >3000 смертей в день: ----------")
print(deathsOver3k.value_counts())
print("\n---------- Дубликаты: ----------")
print(data[data.duplicated()])
data = data.drop_duplicates()


