import numpy as np
from sklearn.utils import shuffle
from sklearn.model_selection import KFold
from sklearn.linear_model import LinearRegression, Ridge
from sklearn.metrics import mean_squared_error, mean_absolute_error

data = np.load('./data/training_data.npy')
prices = np.load('./data/prices.npy')
data, prices = shuffle(data, prices, random_state=0)

names = [
    'Year', 'Killometers_Driven', 'Mileage', 'Engine', 'Power', 'Seats', 'Owner_Type',
    'FuelType', 'FuelType', 'FuelType', 'FuelType', 'FuelType',
    'Transmission', 'Transmission'
]


# Ex 1
def norm(train, test):
    std = np.std(train, axis=0)
    std[7:] = 1
    mu = np.mean(train)
    return (train - mu) / std, (test - mu) / std


def cv(model):
    mse, mae = [], []
    for tr, te in KFold(n_splits=3).split(data):
        train, test = data[tr], data[te]
        train_pr, test_pr = prices[tr], prices[te]
        train, test = norm(train, test)
        model.fit(train, train_pr)
        pred = model.predict(test)
        mse.append(mean_squared_error(test_pr, pred))
        mae.append(mean_absolute_error(test_pr, pred))
    return np.mean(mse), np.mean(mae)


# Ex 2
mse, mae = cv(LinearRegression())
print(f"LINEAR\nMSE: {mse:.2f}\nMAE: {mae:.2f}\n")

# Ex 3
best_alpha, mse, mae = 1, 0, float('inf')
for alpha in [1, 10, 100, 1000]:
    m, a = cv(Ridge(alpha=alpha))
    if a < mae:
        best_alpha, mse, mae = alpha, m, a
print(f"RIDGE (alpha={best_alpha})\nMSE: {mse:.2f}\nMAE: {mae:.2f}\n")

# Ex 4
data, _ = norm(data, data)
model = Ridge(alpha=best_alpha)
model.fit(data, prices)

print(f"COEFFICIENTS: {model.coef_}\nBIAS: {model.intercept_}")

order = np.argsort(np.abs(model.coef_))[::-1]
print(f"MOST: {names[order[0]]}")
print(f"SECOND: {names[order[1]]}")
print(f"LEAST: {names[order[-1]]}")
