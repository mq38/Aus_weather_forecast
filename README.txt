This repostiory is a project for the course Introduction to Data science 2024/25 fall semester.

The authors of this project are Mihkel Paal and Laura Heleene Tirkkonen.

B2_report.pdf gives a more detailed report on the goals and motivations of this project

code_weather.ipynb is the code itself. The aim of this project  is to use logistic regression to forecast the probability of rain for the next day to improve accuracy of traditional forecasting
Create a simple and automated weather forecast with map output
Create climate diagrams and various interpolated maps


WeatherAUS.csv is the file for the data. The data used are 10 years of weather observations  in Australia from 2007 to 2017. Over 20 variables are recorded, but this project uses mostly Location, Date, Max temp, Min Temp and Rainfall

The first part of the code focuses on importing libraries and encoding variables

The next part is about plotting weather variables and data exploration

Then calculating the probability of rain for the next day

The next part is about creating different kinds of maps, average temperature for a month, interpolation

Then we get into the part where we do the sliding window forecast, and kriging interpolation

After that there is code to create climate  diagrams for different locations, to see the trends in climate during the observed period

