import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

data_file = 'C:/Users/JAY/Desktop/Machine_Learning_Course/StackSkill/ML_scikit_intro/mlintro/data/winequality-white.csv'

wine_data = pd.read_csv(data_file,    
	names= ['Fixed Acidity','Volatile Acidity','Citric Acid',
	'Residual Sugar','Chlorides','Free Sulfur Dioxide','Total Sulfur Dioxide','Density',
	'pH','Sulphates','Alcohol','Quality'],
	skiprows= 1,
	sep= r'\s*;\s*', 
	engine= 'python')

print(wine_data.head())

#create a correlation matrix to view the data
corrmat = wine_data.corr()
f, ax = plt.subplots(figsize=(7,7))
sns.heatmap(corrmat, vmax= .8, square= True, annot= True, fmt= '.2f')
plt.show()

# set features and target
X = wine_data.drop('Quality', axis=1)
y = wine_data['Quality']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 0.2, random_state= 0)

model = DecisionTreeClassifier()
model.fit(X_train, y_train)

score = model.score(X_test, y_test)
print('Accuracy score is: ', score)

