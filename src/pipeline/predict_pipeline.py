import sys
from dataclasses import dataclass

import pandas as pd
from src.components.data_transformation import DataTransformationConfig
from src.exception import CustomException
from src.utils import load_object


class PredictPipeline:
    def __init__(self):
        pass

    def predict(self, features):
        try:
            preprocessor_path = 'artifacts/preprocessor.pkl'
            model_path = 'artifacts/model.pkl'

            preprocessor = load_object(preprocessor_path)
            model = load_object(model_path)

            data_scaled = preprocessor.transform(features)

            pred = model.predict(data_scaled)

            return pred

        except Exception as e:
            raise CustomException(e, sys)

@dataclass
class CustomData:
    gender: str
    race_ethnicity: str
    parental_level_of_education: str
    lunch: str
    test_preparation_course: str
    writing_score: float
    reading_score: float

class Dataframe:
    def __init__(self,data:CustomData):
        self.values =data

    def get_data_as_dataframe(self):
        try:
            custom_data_input_dict = { 
                "gender": [self.values.gender],
                "race_ethnicity": [self.values.race_ethnicity],
                "parental_level_of_education": [self.values.parental_level_of_education],
                "lunch": [self.values.lunch],
                "test_preparation_course": [self.values.test_preparation_course],
                "writing_score": [self.values.writing_score],
                "reading_score": [self.values.reading_score]
            }
            return pd.DataFrame(custom_data_input_dict)
        
        except Exception as e:
            raise CustomException(e, sys)