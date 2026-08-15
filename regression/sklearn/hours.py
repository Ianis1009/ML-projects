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

predicted_grades = model.predict(X)

# plot
plt.scatter(hours, grades)
plt.plot(hours, predicted_grades)
plt.xlabel("Hours studied")
plt.ylabel("Grade")
plt.title("Hours graph")
plt.grid(True)
plt.savefig("regression.png", dpi=150, bbox_inches="tight")
plt.close()
print()
print("Graph saved -> regression.png")

####

# prediction for 9 hours
prediction = model.predict([[12]])

print()
print("Predicted grade for 12 hours:")
print(prediction[0])

predicted_grades = model.predict(X)

# plot
plt.scatter(hours, grades)
plt.plot(hours, predicted_grades)
plt.xlabel("Hours studied")
plt.ylabel("Grade")
plt.title("Hours graph")
plt.grid(True)
plt.savefig("regression.png", dpi=150, bbox_inches="tight")
plt.close()
print()
print("Graph saved -> regression.png")