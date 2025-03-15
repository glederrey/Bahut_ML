import pickle

from sklearn.preprocessing import LabelEncoder

from sklearn.metrics import f1_score
from sklearn.metrics import mean_absolute_error as mae

def results_predictions_satisfaction(y_pred):

    names = ['y_test_20.pkl', 'y_test_50.pkl', 'y_test.pkl']

    found_corresponding_file = False
    for n in names:
        path = f'../../data/passenger_satisfaction/{n}'
        with open(path, 'rb') as f:
            y_test = pickle.load(f)

        if len(y_test) == len(y_pred):
            found_corresponding_file = True
            break

    if not found_corresponding_file:
        raise ValueError("Aucun fichier y_test correspondant à y_pred trouvé !")   

    # Check if there are other stuff than 'satisfied' or 'neutral or dissatisfied' in y_pred
    if not all(pred in ['satisfied', 'neutral or dissatisfied'] for pred in y_pred):
        raise ValueError("y_pred must contain only 'satisfied' or 'neutral or dissatisfied' values !")

    # Transform both in 0 and 1
    le = LabelEncoder()
    y_test = le.fit_transform(y_test)
    y_pred = le.transform(y_pred)

    f1_score_val = f1_score(y_test, y_pred)

    return f1_score_val

def results_predictions_prices(y_pred):

    names = ['y_test_20.pkl', 'y_test_50.pkl', 'y_test.pkl']

    found_corresponding_file = False
    for n in names:
        path = f'../../data/flight_prices/{n}'
        with open(path, 'rb') as f:
            y_test = pickle.load(f)

        if len(y_test) == len(y_pred):
            found_corresponding_file = True
            break

    if not found_corresponding_file:
        raise ValueError("Aucun fichier y_test correspondant à y_pred trouvé !")   

    mae_val = mae(y_test, y_pred)

    return mae_val