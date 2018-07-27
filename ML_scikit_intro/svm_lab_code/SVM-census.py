import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
import sklearn.preprocessing as preprocessing
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

#%matplotlib inline

#
# This tutorial uses SVM to predict where income is above or below $50k

data_file = 'C:/Users/JAY/Desktop/Machine_Learning_Course/StackSkill/ML_scikit_intro/mlintro/data/adult.csv'

original_data = pd.read_csv(
	data_file,
	names=[
		'Age','Workclass','fnlwgt','Education','Education-Num','Marital Status',
		'Occupation','Relationship','Race','Gender','Capital Gain','Capital Loss',
		'Hours Per Week','Country','Target'],
		sep=r'\s*,\s*',
		engine='python',
		na_values='?')

print(original_data.head())

fig = plt.figure(figsize=(20,20))
cols = 3
rows = math.ceil(float(original_data.shape[1]) / cols)

# #plot the features
# for i, column in enumerate(['Age','Workclass','Education','Occupation','Race','Gender']):
# 	ax = fig.add_subplot(rows, cols, i+1)
# 	ax.set_title(column)
# 	if original_data.dtypes[column] == np.object:
# 		original_data[column].value_counts().plot(kind='bar', axes=ax)
# 	else:
# 		original_data[column].hist(axes=ax)
# 		plt.xticks(rotation='vertical')
# 	plt.subplots_adjust(hspace=0.7, wspace=0.2)
# 	plt.show()

# use labelEncoder to transform text to numbers

# switch occupation strings to numbers
le = preprocessing.LabelEncoder()
original_data['Occupation'] = le.fit_transform(original_data['Occupation'].astype(str))

# switch Target feature to numbers
original_data['Target'] = le.fit_transform(original_data['Target'].astype(str))
original_data.tail()

original_data.groupby('Education-Num').Target.mean().plot(kind='bar')
#plt.show()


#
# End of tutorial 1
#

#
# Start of tutorial 2
#

# since we saw in from the plots in tutorial 1 that the education and occupation 
# look the most correlated with income so that is what we will use

# get important features
X = original_data[['Education-Num','Occupation']]

y = original_data['Target']

# plit the data into training data and test data (80/20)
X_train, x_test, y_train, y_test = train_test_split(X,y,test_size=0.2, random_state=0)

# declare svc with no tuning
classifier = SVC()

# train (fit) our model
classifier.fit(X_train, y_train)

# predicting the result and giving the accuracy
score = classifier.score(x_test, y_test)

print('Accuracy : ', score*100)

# convert non-numeric fields to numeric
original_data['Race'] = le.fit_transform(original_data['Race'].astype(str))
original_data['Gender'] = le.fit_transform(original_data['Gender'].astype(str))
original_data['Marital Status'] = le.fit_transform(original_data['Marital Status'].astype(str))
original_data['Education'] = le.fit_transform(original_data['Education'].astype(str))

#correlation matrix
corrmat = original_data.corr()
f, ax = plt.subplots(figsize=(7,7))

# plot the correlation matrix
sns.heatmap(corrmat, vmax=0.8, square=True);
#plt.show()

# reset the features
X = original_data[['Education-Num','Occupation','Age','Gender']]
y = original_data['Target']

# re-train the model
# X_train, x_test, y_train, y_test = train_test_split(X,y,test_size=0.2, random_state=0)
# classifier = SVC()
# classifier.fit(X_train, y_train)
# score = classifier.score(x_test, y_test)

# print('Accuracy : ', score*100)

# Set the kernel to radial basis function with penalty parameter c=1.0
X_train, x_test, y_train, y_test = train_test_split(X,y,test_size=0.2, random_state=0)
classifier = SVC(kernel='rbf', C=1.0)
classifier.fit(X_train, y_train)
score = classifier.score(x_test, y_test)
print('Accuracy : ', score*100)
