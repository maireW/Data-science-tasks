#simple linear regression https://stackabuse.com/linear-regression-in-python-with-scikit-learn/
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = pd.read_csv("student_scores.csv")
print(data)
#print numbe rof rows and columns
print(data.shape)
#retrieves the first 5 records from the dataset
print(data.head())
#see statistical details of the dataset
print(data.describe())
#plot data points on 2-D graph 
data.plot(x='Hours', y='Scores', style='o')
plt.title('Hours vs Percentage')
plt.xlabel('Hours Studied')
plt.ylabel('Percentage Score')
plt.show()
#divide the data into "attributes" (independent variables) and "labels" (dependent variables). 
X = data.iloc[:, :-1].values
y = data.iloc[:, 1].values
# split this data into training (80% of the data) and test sets (20% of the data). test_size variable specifies the proportion of test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
#run regression
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)
# retrieve the intercept
print(regressor.intercept_)
#retrieving the slope (coefficient of x)
print(regressor.coef_)
#see how accurately regression predicts the percentage score.
y_pred = regressor.predict(X_test)
df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
print(df)
#evaluate the performance of algorithm by cal three means
from sklearn import metrics
print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))
