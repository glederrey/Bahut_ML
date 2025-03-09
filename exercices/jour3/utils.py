import pickle

from sklearn.preprocessing import LabelEncoder

from sklearn.metrics import f1_score
from sklearn.metrics import mean_absolute_error as mae

def results_predictions_satisfaction(y_pred):

    path = '../../data/passenger_satisfaction/y_test.pkl'
    with open(path, 'rb') as f:
        y_test = pickle.load(f)

    if len(y_pred) != len(y_test):
        raise ValueError(f"y_pred and y_test must have the same length ({len(y_pred)} != {len(y_test)})")

    # Check if there are other stuff than 'satisfied' or 'neutral or dissatisfied' in y_pred
    if not all(pred in ['satisfied', 'neutral or dissatisfied'] for pred in y_pred):
        raise ValueError("y_pred must contain only 'satisfied' or 'neutral or dissatisfied' values !")

    # Transform both in 0 and 1
    le = LabelEncoder()
    y_test = le.fit_transform(y_test)
    y_pred = le.transform(y_pred)

    f1_score_val = f1_score(y_test, y_pred)

    print(f"F1 score is: {f1_score_val:.5f}")

    return f1_score_val

def results_predictions_prices(y_pred):

    path = '../../data/flight_prices/y_test.pkl'
    with open(path, 'rb') as f:
        y_test = pickle.load(f)

    if len(y_pred) != len(y_test):
        raise ValueError(f"y_pred and y_test must have the same length ({len(y_pred)} != {len(y_test)})")

    mae_val = mae(y_test, y_pred)

    print(f"MAE is: {mae_val:.5f}")

    return mae_val


