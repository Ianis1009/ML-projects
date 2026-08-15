import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# dataset
hours = [1, 2, 3, 4, 5, 6, 7, 8]
grades = [52, 55, 61, 65, 70, 74, 81, 86]

# sklearn -> X should be 2D

X = [[1], [2], [3], [4], [5], [6], [7], [8]]

y = grades

# model 
model = LinearRegression()

# train model
model.fit(X, y)

# paramenters
print("Slope:", model.coef_[0])
print("Intercept:", model.intercept_)

# prediction for 9 hours
prediction = model.predict([[9]])

print()
print("Predicted grade for 9 hours:")
print(prediction[0])

