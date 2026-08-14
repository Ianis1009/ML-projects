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

