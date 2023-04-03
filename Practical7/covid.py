import numpy as np
import matplotlib.pyplot as plt

# Select the rows where the date is '2020-03-31' and the columns 'location', 'new_cases' and 'new_deaths'
new_data = covid_data.loc[covid_data['date'] == '2020-03-31', ['location', 'new_cases', 'new_deaths']]

# Compute the mean new cases and new deaths on 31 March using numpy
mean_new_cases = np.mean(new_data['new_cases'])
mean_new_deaths = np.mean(new_data['new_deaths'])

# Print the mean new cases and new deaths
print("Mean new cases on 31 March:", mean_new_cases)
print("Mean new deaths on 31 March:", mean_new_deaths)

# Compute the proportion of new deaths as a proportion of new cases on 31 March
proportion_new_deaths = new_data['new_deaths'].sum() / new_data['new_cases'].sum()
print("Proportion of new deaths as a proportion of new cases on 31 March:", proportion_new_deaths)

# Plot boxplots of new cases and new deaths on 31 March using matplotlib
fig, ax = plt.subplots()
new_data.boxplot(column=['new_cases', 'new_deaths'], ax=ax)
plt.title("New cases and new deaths on 31 March")
plt.ylabel("Number of cases/deaths")
plt.show()

# Select the rows where the location is 'World' and the columns 'date' and 'new_cases'
world_data = covid_data.loc[covid_data['location'] == 'World', ['date', 'new_cases']]

# Convert the 'date' column to a datetime object and set it as the index
world_data['date'] = pd.to_datetime(world_data['date'])
world_data.set_index('date', inplace=True)

# Resample the data to a weekly frequency and compute the cumulative sum
world_data = world_data.resample('W').sum().cumsum()

# Plot the new cases for the world over time using matplotlib
world_dates = world_data.index
world_new_cases = world_data['new_cases']
plt.plot(world_dates, world_new_cases, 'r+')
plt.title("New cases for the world over time")
plt.xlabel("Date")
plt.ylabel("Number of cases")
plt.show()

# Plot new cases and new deaths for the world over time using matplotlib
world_data = covid_data.loc[covid_data['location'] == 'World', ['date', 'new_cases', 'new_deaths']]
world_data['date'] = pd.to_datetime(world_data['date'])
world_data.set_index('date', inplace=True)
world_data = world_data.resample('W').sum().cumsum()

fig, ax = plt.subplots()
ax.plot(world_data.index, world_data['new_cases'], color='blue', label='New cases')
ax.plot(world_data.index, world_data['new_deaths'], color='red', label='New deaths')
plt.title("New cases and new deaths for the world over time")
plt.xlabel("Date")
plt.ylabel("Number of cases/deaths")
plt.legend()
plt.xticks(world_data.index[0:len(world_data.index):4], rotation=-90)
plt.show()
