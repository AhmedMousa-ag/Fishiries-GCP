import os


PICKLE_OBJ_PATH = os.path.join("Utils","preprocess","pickle_obj")
if not os.path.exists(PICKLE_OBJ_PATH):
    os.makedirs(PICKLE_OBJ_PATH)

TRAINING = True

LABEL = "lat400sqkm"
SCALE_LABEL=False

SAVED_MODEL_PATH = os.path.join("models","xgboost")
if not os.path.exists(SAVED_MODEL_PATH):
    os.makedirs(SAVED_MODEL_PATH)



PREPROCESS_DICT = {"lat400sqkm": "scale",
                  "lon400sqkm": "scale",
                  "gear": "LabelEncoder",
                  "year": "scale",
                  "kg": "scale",
                  "rate": "scale",
                  "species": "LabelEncoder",
                  "sid": "LabelEncoder"}


PROJECT_ID = "fishiries-alaska"
DATASET_ID = 'fishiries_alaska_observer'
TABLE_ID = 'fisheries'