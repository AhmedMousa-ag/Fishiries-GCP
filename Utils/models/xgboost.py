from xgboost import XGBRegressor
import config
from sklearn.metrics import mean_squared_error as MSE, mean_absolute_error as MAE
import pickle
import os

SAVED_MODEL_PATH = config.SAVED_MODEL_PATH


def build_train_model(x_train, y_train, x_test, y_test, param=None, save_obj=True):
    if param == None:
        model = XGBRegressor()
    else:
        model = XGBRegressor(param)

    model.fit(x_train, y_train)

    mae = MAE(y_test, model.predict(x_test))
    mse = MSE(y_test, model.predict(x_test))
    print(f"XGBoost test result, MAE: {mae}, MSE: {mse}")

    if save_obj:
        save_model(model)

    return model


def save_model(model, path=SAVED_MODEL_PATH):
    save_path = os.path.join(path, "xgboost.pkl")
    pickle.dump(model, open(save_path, 'wb'))


def load_model(path=SAVED_MODEL_PATH):
    save_path = os.path.join(path, "xgboost.pkl")
    model = pickle.load(save_path)
    return model
