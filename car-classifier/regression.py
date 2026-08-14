from pathlib import Path

import matplotlib.pyplot as plt
from scipy import stats

#data

x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6]
y = [99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86]

slope, intercept, r, p, std_err = stats.linregress(x, y)


def myfunc(x):
    return slope * x + intercept


mymodel = list(map(myfunc, x))

print(f"Slope: {slope:.4f}")
print(f"Intercept: {intercept:.4f}")
print(f"R: {r:.4f}")
print(f"R^2: {r ** 2:.4f}")
print(f"P-value: {p:.4f}")
print(f"Standard error: {std_err:.4f}")

BASE_DIR = Path(__file__).resolve().parent

IMG_DIR = BASE_DIR / "img"

IMG_DIR.mkdir(exist_ok=True)



# graph

plt.scatter(x, y)

plt.plot(x, mymodel)

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Simple Linear Regression")

plt.grid(True)

output_path = IMG_DIR / "linear_regression.png"

plt.savefig(output_path, dpi=150, bbox_inches="tight")

plt.close()


print()
print(f"Graph saved to: {output_path}")