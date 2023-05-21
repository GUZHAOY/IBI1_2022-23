import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

pd.set_option('display.max_columns', None)
# show all columns
os.chdir("D:/2023Grade1/IBI1")
os.getcwd()
os.listdir()
covid_data = pd.read_csv("full_data.csv")
# the second column from every 100th row from the first 1000 rows (inclusive)
print(covid_data.iloc[0:1001:100, 1])

# "total cases" for all rows corresponding to Afghanistan.
my_rows = []
for i in range(len(covid_data)):
    if covid_data.loc[i, "location"] == "Afghanistan":
        my_rows.append(True)
    else:
        my_rows.append(False)
print(covid_data.loc[my_rows, "total_cases"])

# the mean number of new cases and new deaths on 31 March 2020.
new_data1 = covid_data.loc[covid_data["location"] != "World", ["date", "location", "new_cases", "new_deaths"]]
new_data = new_data1.loc[new_data1["date"] == "2020-03-31", ["location", "new_cases", "new_deaths"]]
new_cases_mean = np.mean(new_data["new_cases"])
new_deaths_mean = np.mean(new_data["new_deaths"])
print(f"This mean has already exclude the rows called 'world'. The mean number for new cases "
      f"on 2020-3-31 is {new_cases_mean},and the mean number for new deaths "
      f"on 2020-3-31 is {new_deaths_mean}")

# boxplot of new cases and new deaths on 31 March 2020. The rows "World" are excluded.
plt.boxplot(x=new_data["new_deaths"])
plt.title("new deaths on 2020-03-31")
plt.show()
plt.boxplot(x=new_data["new_cases"])
plt.title("new cases on 2020-03-31")
plt.show()

data = pd.DataFrame({'new_cases': new_data["new_cases"], 'new_deaths': new_data["new_deaths"]})
data.boxplot(column=['new_cases', 'new_deaths'])
plt.title("new cases and deaths on 2020-03-31")
plt.show()

# plot both new cases and new deaths worldwide over time.
world_data = covid_data.loc[covid_data["location"] == "World", "new_cases"]
world_data1 = covid_data.loc[covid_data["location"] == "World", "new_deaths"]
world_dates = covid_data.loc[covid_data["location"] == "World", "date"]

plt.plot(figsize=(30, 5))
plt.plot(world_dates, world_data, 'b--', label='new cases')
plt.plot(world_dates, world_data1, 'r--', label='new deaths')
plt.xticks(world_dates.iloc[0:len(world_dates):4])
# show x ticks every 4 days.
plt.xticks(rotation=90, fontsize=6)
# rotate the ticks
plt.ylabel('Number')
plt.title("worldwide COVID-19 new deaths and new cases overtime")
plt.legend()
plt.show()

# question
china_data = covid_data.loc[covid_data['location'] == 'China', ['total_cases', 'total_deaths']]
china_rate = china_data.apply(lambda china_data: china_data['total_deaths'] / china_data['total_cases'], axis=1)
# let the value of total death / total cases write into each row.
plt.plot(world_dates, china_rate, 'bo')
plt.xticks(world_dates.iloc[0:len(world_dates):4])
plt.xticks(rotation=90, fontsize=6)
plt.title("China COVID-19 death rate overtime")
plt.ylabel('Total death rate')

plt.show()
