
import numpy as np
from sklearn.utils import shuffle
from sklearn.model_selection import KFold, GridSearchCV
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.metrics import mean_squared_error, mean_absolute_error

data = np.load('./data/training_data.npy')
prices = np.load('./data/prices.npy')

data, prices = shuffle(data, prices, random_state=0)

NAMES = [
    'Year', 'Killometers_Driven', 'Mileage',
    'Engine', 'Power', 'Seats', 'Owner_Type',
    'FuelType', 'FuelType', 'FuelType', 'FuelType', 'FuelType',
    'Transmission', 'Transmission'
]


def norm(train, test):
    std = np.std(train, axis=0)
    std[7:] = 1
    mu = np.mean(train)
    train = np.divide(train - mu, std)
    test = np.divide(test - mu, std)
    return train, test


class Model:
    def __init__(self, model):
        self.model = model

    def fit(self, train, prices):
        self.model.fit(train, prices)

    def predict(self, test):
        return self.model.predict(test)

    def errors(self, true, pred):
        return mean_squared_error(true, pred), mean_absolute_error(true, pred)

    def tune(self, train, prices):
        grid = {'alpha': [1, 10, 100, 1000]}
        gs = GridSearchCV(
            estimator=self.model, param_grid=grid, cv=5,
            scoring='neg_mean_absolute_error'
        )
        gs.fit(train, prices)
        return gs.best_params_['alpha']

    def coef(self):
        return self.model.coef_

    def bias(self):
        return self.model.intercept_

    def top_feat(self):
        w = np.abs(self.coef())
        return NAMES[np.argmax(w)]

    def min_feat(self):
        w = np.abs(self.coef())
        return NAMES[np.argmin(w)]


def cv_eval(est):
    kf = KFold(n_splits=3)
    m = Model(est)
    errs = []
    alphas = []

    for tr_idx, te_idx in kf.split(data):
        train, test = data[tr_idx], data[te_idx]
        train_pr, test_pr = prices[tr_idx], prices[te_idx]

        train, test = norm(train, test)

        m.fit(train, train_pr)
        errs.append([*m.errors(test_pr, m.predict(test))])

        if isinstance(m.model, Ridge):
            alphas.append(m.tune(train, train_pr))

    if isinstance(m.model, Ridge):
        print(f"BEST ALPHA: {np.mean(np.array(alphas))}")

    return np.array(errs)


mse, mae = np.mean(cv_eval(LinearRegression()), axis=0)
print(f"LINEAR\nMSE: {mse:.2f}\nMAE: {mae:.2f}\n")

mse, mae = np.mean(cv_eval(Ridge()), axis=0)
print(f"RIDGE\nMSE: {mse:.2f}\nMAE: {mae:.2f}")

mse, mae = np.mean(cv_eval(Lasso()), axis=0)
print(f"LASSO\nMSE: {mse:.2f}\nMAE: {mae:.2f}")

m = Model(Ridge(alpha=100))
m.fit(data, prices)

print(f"COEFFICIENTS: {m.coef()}\nBIAS: {m.bias()}")

print(f"MOST: {m.top_feat()}\nLEAST: {m.min_feat()}")
