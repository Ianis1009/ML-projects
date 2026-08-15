import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

X = [
    [1, 5],
    [2, 5],
    [3, 6],
    [4, 6],
    [5, 7],
    [6, 7],
    [7, 8],
    [8, 8],
]

y = [50, 54, 60, 64, 69, 74, 81, 85]

model = LinearRegression()
model.fit(X, y)

print("MODEL: ")
print(f"Coefficient for hours: {model.coef_[0]:.2f}")
print(f"Coefficient for sleep: {model.coef_[1]:.2f}")
print(f"Intercept: {model.intercept_:.2f}")


new_student = [[6, 8]]
prediction = model.predict(new_student)
print()
print(f"Predicted grade: {prediction[0]:.2f}")

predictions = model.predict(X)
print()
print("All preditions: ")

for actual, predicted in zip(y, predictions):
    print(f"Actual: {actual:5.1f} " f"| Predicted: {predicted: 5.1f}")

