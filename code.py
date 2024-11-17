print("Script started")

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt # data visualization

import seaborn as sns # data visualization
sns.reset_defaults()


##read data

data = "C:\projekt\Andmed\weatherAUS.csv"
df = pd.read_csv(data)
#df.info()


##find categorical variables

categorical = [var for var in df.columns if df[var].dtype=='O']

#print('There are {} categorical variables\n'.format(len(categorical)))

#print('Categorical variables are :', categorical)

## find missing values in categorical variables

#print(df[categorical].isnull().sum())


##frequency of categorical variables

#for var in categorical: 
    
#    print(df[var].value_counts())

##check for cardinality in categorical variables

#for var in categorical:
    
#    print(var, ' contains ', len(df[var].unique()), ' labels')


## date variable contains 3436 labels so needs to be split into year/month/day

#print(df["Date"].dtypes)

df['Date']= pd.to_datetime(df['Date'])

df['Year'] = df['Date'].dt.year

df['Month'] = df['Date'].dt.month

df['Day'] = df['Date'].dt.day

df.drop('Date', axis=1, inplace = True)

#start looking into other categorical variables

#print('Location contains', len(df.Location.unique()), 'labels')

#print(df.Location.unique())

#one-hot encoding for location variables

pd.get_dummies(df.Location, drop_first=True).astype(int).head()

#one-hot encoding for wind gust direction variables, also add dummy for nan values

pd.get_dummies(df.WindGustDir, drop_first=True, dummy_na=True).astype(int).head()

#one-hot encoding for wind dir 9am variables, also add dummy for nan values

pd.get_dummies(df.WindDir9am, drop_first=True, dummy_na=True).astype(int).head()

#one-hot encoding for wind dir 9am variables, also add dummy for nan values

pd.get_dummies(df.WindDir3pm, drop_first=True, dummy_na=True).astype(int).head()

#one-hot encoding for raintoday variable, add dummy for nan values

pd.get_dummies(df.RainToday, drop_first=True, dummy_na=True).astype(int).head()


#explore numerical variables

numerical = [var for var in df.columns if df[var].dtype!='O']

#print('There are {} numerical variables\n'.format(len(numerical)))

#print('The numerical variables are :', numerical)

#19 numerical variables, all continuous type
#check for missing values

print(df[numerical].isnull().sum())

print(round(df[numerical].describe()),2)

# rainfall, evaporation, windspeed9am and windspeed 3pm might contain extreme outliers

plt.figure(figsize=(15,10))


plt.subplot(2, 2, 1)
fig = df.boxplot(column='Rainfall')
fig.set_title('')
fig.set_ylabel('Rainfall')


plt.subplot(2, 2, 2)
fig = df.boxplot(column='Evaporation')
fig.set_title('')
fig.set_ylabel('Evaporation')


plt.subplot(2, 2, 3)
fig = df.boxplot(column='WindSpeed9am')
fig.set_title('')
fig.set_ylabel('WindSpeed9am')


plt.subplot(2, 2, 4)
fig = df.boxplot(column='WindSpeed3pm')
fig.set_title('')
fig.set_ylabel('WindSpeed3pm')


plt.show()
print("Script finished")
