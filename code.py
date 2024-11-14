import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt # data visualization
import seaborn as sns # statistical data visualization

data = "C:\projekt\Andmed\weatherAUS.csv"
df = pd.read_csv(data)


print(df.head())
