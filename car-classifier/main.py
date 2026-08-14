from pathlib import Path 
import pandas as pd

from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "data" / "cars.csv"
data = pd.read_csv(DATA_PATH)

print("DATASET:")
print(data.head())

print()
print(f"Number of cars: {len(data)}")
