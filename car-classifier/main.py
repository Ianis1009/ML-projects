from pathlib import Path

import pandas as pd

from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "data" / "cars.csv"

data = pd.read_csv(DATA_PATH)
print(f"Number of cars: {len(data)}")
print()
print("Columns:")
print(data.columns.tolist())

print()
print(data["body_type"].value_counts())

MIN_SAMPLES_PER_CLASS = 2

class_counts = data["body_type"].value_counts()

valid_classes = class_counts[class_counts >= MIN_SAMPLES_PER_CLASS].index

data = data[data["body_type"].isin(valid_classes)].copy()

print()
print(f"Number of cars: {len(data)}")

print()
print(data["body_type"].value_counts())

features = [
    "year",
    "engine",
    "horsepower",
    "torque",
    "weight",
    "doors",
    "seats",
    "mileage",
]

X = data[features]

y = data["body_type"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)


print()
print(f"Training samples: {len(X_train)}")
print(f"Test samples: {len(X_test)}")

model = DecisionTreeClassifier(max_depth=5, random_state=42)
model.fit(X_train, y_train) # train model

predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
print()

print("Classification report:") #report 