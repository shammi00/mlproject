# standard library imports
import os
import sys

# third-party imports
import pandas as pd
import numpy as np
import dill

# local application imports
# custom modules
from src.logger import logging
from src.exception import CustomException

# sklearn libraries
#for model training
#evaluation metrics 
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV


def save_object(file_path, obj):
    try:
        #import pickle
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'wb') as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)

# method 2
def evaluate_models(X_train, y_train, X_test, y_test, models, params):
    try:
        report = {}
        for model_name, model in models.items():
                para=params[model_name]
    
                # hyperparameter tuning
                gs = GridSearchCV(model, para, cv=3)
                gs.fit(X_train, y_train)
    
                # update model with best parameters
                model.set_params(**gs.best_params_)
                # train final model
                model.fit(X_train, y_train)
                # predict training data
                y_train_pred = model.predict(X_train)
                # predict testing data
                y_test_pred = model.predict(X_test)
                # train and test model score
                train_model_score = r2_score(y_train, y_train_pred)
                test_model_score = r2_score(y_test, y_test_pred)
                # save the best model score in report dictionary
                report[model_name] = test_model_score

                return report

    except Exception as e:
        raise CustomException(e, sys)   

#method 1

# def evalute_model(model, X_train, y_train, X_test, y_test,models,params):
#     try:
#         report = {}
       
#         for i in range(len(list(model))):
           
#             model = list(model.values())[i]
#             para=params[list(model.keys())[i]]
            
#             # hyperparameter tuning
#             gs = GridSearchCV(model, para, cv=3)
#             gs.fit(X_train, y_train)

#             # update model with best parameters
#             model.set_params(**gs.best_params_)
#             # train final model
#             model.fit(X_train, y_train)
#             # predict training data
#             y_train_pred = model.predict(X_train)
#             # predict testing data
#             y_test_pred = model.predict(X_test)
#             #train and test model score
#             train_model_score = r2_score(y_train, y_train_pred)
#             test_model_score = r2_score(y_test, y_test_pred)
#         # save the best model score in report dictionary
#         report[list(model.keys())[i]] = test_model_score
      
#         return report

    except Exception as e:
        raise CustomException(e, sys)
    

def load_object(file_path):
    try:
        with open(file_path, 'rb') as file_obj:
            return dill.load(file_obj)

    except Exception as e:
        raise CustomException(e, sys)

