from pathlib import Path 
import pandas as pd

from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "data" / "cars.csv"

data = pd.read_csv(DATA_PATH)

print("Dataset:")
print(data.head())

print()
print(f"Number of cars: {len(data)}")


features = ["year", "engine", "horsepower", "torque", "weight", "doors", "seats","mileage"]

X = data[features]
y = data["body_type"] # prediction for body type

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,random_state=42, stratify=y)

print()
print(f"Training samples: {len(X_train)}")
print(f"Test samples: {len(X_test)}")

model = DecisionTreeClassifier(max_depth=5, random_state=42)
model.fit(X_train, y_train)


predictions = model.predict(X_test)

accuracy = accuracy_score(y_test,predictions)

print()
print("Model evaluation")
print(f"Accuracy: {accuracy:.2%}")

print()
print("Classification report:")
print(classification_report(y_test, predictions))


# Car prediction

print()
print("Car Classifier")

year = int(input("Year: "))
engine = float(input("Engine size (e.g. 2.0): "))
horsepower = int(input("Horsepower: "))
torque = int(input("Torque (Nm): "))
weight = int(input("Weight (kg): "))
doors = int(input("Number of doors: "))
seats = int(input("Number of seats: "))
mileage = int(input("Mileage (km): "))



new_car = pd.DataFrame(
    [
        {
            "year": year,
            "engine": engine,
            "horsepower": horsepower,
            "torque": torque,
            "weight": weight,
            "doors": doors,
            "seats": seats,
            "mileage": mileage,
        }
    ]
)


prediction = model.predict(new_car)[0] # by cars.csv


print()
print(f"Predicted body type: {prediction}")