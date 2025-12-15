import logging
import sys
from src.mlproject.exception import CustomException
from src.mlproject.logger import logger
import pandas as pd
import sqlite3
import os

def read_sql_data():
    logging.info("Reading SQL database started")
    try:
        db_path = os.path.join(os.getcwd(), "student.db")
        mydb = sqlite3.connect(db_path)
        logging.info(f"Connection Established to {db_path}")
        
        df = pd.read_sql_query('Select * from student_performance', mydb)
        print(df.head())

        return df

    except Exception as e:
        raise CustomException(e,sys)

import pickle
import numpy as np

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)

from sklearn.metrics import r2_score

def evaluate_models(X_train, y_train,X_test,y_test,models):
    try:
        report = {}

        for i in range(len(list(models))):
            model = list(models.values())[i]

            model.fit(X_train,y_train)

            y_train_pred = model.predict(X_train)

            y_test_pred = model.predict(X_test)

            train_model_score = r2_score(y_train, y_train_pred)

            test_model_score = r2_score(y_test, y_test_pred)

            report[list(models.keys())[i]] = test_model_score

        return report

    except Exception as e:
        raise CustomException(e, sys)

def load_object(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj)

    except Exception as e:
        raise CustomException(e, sys)
