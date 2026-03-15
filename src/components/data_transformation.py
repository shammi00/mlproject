# Importing necessary libraries
#system libraries
import os
import sys
from dataclasses import dataclass

#custom modules
from src.logger import logging
from src.exception import CustomException
from src.utils import save_object

#third party libraries
import pandas as pd
import numpy as np

#sklearn libraries
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler



@dataclass
class DataTransformationConfig:
    prepossor_obj_file_path = os.path.join("artifacts", "preprocessor.pkl")

# The above code defines a data class `DataTransformationConfig` that contains a single attribute `prepossor_obj_file_path`.
# This attribute is initialized with a default value that specifies the file path for the preprocessor object, which is set to "artifacts/preprocessor.pkl".
# This configuration class will be used to manage the file path for saving the preprocessor object during the data transformation process.

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformer_object(self):
        '''
        This function is responsible for data transformation
        
        '''
        try:
            numerical_columns = ['writing_score', 'reading_score']
            categorical_columns = [
                'gender',
                'race_ethnicity',
                'parental_level_of_education', 
                'lunch', 
                'test_preparation_course'
                ]

            numerical_pipeline = Pipeline(steps=[
                ('imputer', SimpleImputer(strategy='median')),
                ('scaler', StandardScaler())
            ])
            
            categorical_pipeline = Pipeline(steps=[
                ('imputer', SimpleImputer(strategy='most_frequent')),
                ('one_hot_encoder', OneHotEncoder(drop='first')),
                ('scaler', StandardScaler(with_mean=False))
            ])

            logging.info(f"Categorical columns: {categorical_columns}")
            logging.info(f"Numerical columns: {numerical_columns}")
            

            preprocessor = ColumnTransformer(
                transformers=[
                    ('numerical_transformer', numerical_pipeline, numerical_columns),
                    ('categorical_transformer', categorical_pipeline, categorical_columns)
                ]
            )
    
            logging.info(f"Categorical columns encoding completed")
            logging.info(f"Numerical columns scaling completed")

            return preprocessor
        
        except Exception as e:
            raise CustomException(e, sys)

# The `get_data_transformer_object` method is responsible for creating and returning a data transformer object that can be used to preprocess the data.
# It defines separate pipelines for numerical and categorical features, which include imputation and scaling steps.
# The method also logs the columns being processed and any exceptions that occur during the creation of the preprocessor object.


    
    def initiate_data_transformation(self, train_path, test_path):
        
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logging.info("Read train and test data completed")
            logging.info("Obtaining preprocessor object")

            preprocessor_obj = self.get_data_transformer_object()

            target_column_name = "math_score"

            input_feature_train_df = train_df.drop(columns=[target_column_name], axis=1)
            target_feature_train_df = train_df[target_column_name]

            input_feature_test_df = test_df.drop(columns=[target_column_name], axis=1)
            target_feature_test_df = test_df[target_column_name]

            logging.info("Applying preprocessing object on training and testing dataframe")

            input_feature_train_arr = preprocessor_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocessor_obj.transform(input_feature_test_df)

            train_arr = np.c_[input_feature_train_arr, np.array(target_feature_train_df)]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

            save_object(
                file_path=self.data_transformation_config.prepossor_obj_file_path,
                obj=preprocessor_obj
                )
            
            logging.info("Saved preprocessor object")

            return (
                train_arr,
                test_arr,
                self.data_transformation_config.prepossor_obj_file_path
            )
        except Exception as e:
            raise CustomException(e, sys)

# The `initiate_data_transformation` method is responsible for performing the data transformation process.
# It reads the training and testing data from the specified file paths, obtains the preprocessor object, and applies the preprocessing steps to both the training and testing data.
# The method then combines the transformed input features with the target variable to create the final training and testing arrays.
# Finally, it saves the preprocessor object to the specified file path and returns the transformed training and testing arrays along with the preprocessor file path. 
# If any exceptions occur during this process, they are caught and raised as a `CustomException` with the relevant error information.            
            
