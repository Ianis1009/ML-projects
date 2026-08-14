from pathlib import Path 
import pandas as pd

from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "data" / "cars.csv"
data = pd.read_csv(DATA_PATH) # read csv

print("DATASET:")
print(data.head())

print()
print(f"Number of cars: {len(data)}")

# features
features = ["engine", "doors", "seats", "horsepower"]

X = data[features]
y = data["type"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y) 

print()
print(f"Training samples: {len(X_train)}")
print(f"Test samples: {len(X_test)}")

model = DecisionTreeClassifier(max_depth=3, random_state=42)
model.fit(X_train, y_train)

predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
print()
print(f"Accuracy: {accuracy:.2%}")
print()
print("Report:")
print(classification_report(y_test, predictions))


# Car prediction

print()
print("Car Classifier")

engine = float(input("Engine size (e.g. 2.0)"))
doors = int(input("Number of doors: "))
seats = int(input("Number of seats: "))
horsepower = int(input("Horsepower: "))

new_car = pd.DataFrame([{"engine": engine,"doors": doors, "seats": seats, "horsepower": horsepower}])

prediction = model.predict(new_car)[0]
print()
print(f"Predicted type: {prediction}") # by cars.csv