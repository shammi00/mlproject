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



def save_object(file_path, obj):
    try:
        #import pickle
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'wb') as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)