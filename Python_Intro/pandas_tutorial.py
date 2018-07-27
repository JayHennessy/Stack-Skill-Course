# Python Pandas tutorial (stackSkill)
import pandas as pd
import matplotlib.pyplot as plt 
from matplotlib import style
data = pd.read_csv('C:/Users/JAY/Desktop/Machine_Learning_Course/KaggleCompetions/titanic_comp/data/test.csv')

# shows data on screen
print(data.head())
data.tail()

#print the number of rows (incldues the header)
print(len(data.index))

# return rows that meet a certain condition
# here we get the date value for all the days that have rain in the event column
rainy_days = data['Date'][df['Events']=='Rain']

# plot the results with matplotlib
style.use('classic')
data['Max.TemperatureC'].plot()
plt.show()