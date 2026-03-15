# Importing necessary libraries

#system libraries
import os
import sys

#custom modules
from src.logger import logging
from src.exception import CustomException
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer

#third party libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

# Creating a data ingestion component
@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join("artifacts", "train.csv")
    test_data_path: str = os.path.join("artifacts", "test.csv")
    raw_data_path: str = os.path.join("artifacts", "raw.csv")

# The above code defines a data class `DataIngestionConfig` that contains three
# attributes: `train_data_path`, `test_data_path`, and `raw_data_path`. Each
# attribute is initialized with a default value that specifies the file path
# for the respective data files. The paths are constructed using the
# `os.path.join` function to ensure compatibility across different operating
# systems. This configuration class will be used to manage the file paths for
# the raw, training, and testing datasets during the data ingestion process.


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            df = pd.read_csv(os.path.join("notebook/data", "stud.csv"))
            logging.info("Read the dataset as dataframe")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            logging.info("Train test split initiated")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info("Ingestion of the data is completed")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            raise CustomException(e, sys)

# The `DataIngestion` class is responsible for handling the data ingestion process.
# It initializes an instance of the `DataIngestionConfig` class to manage the file
# paths for the raw, training, and testing datasets. The `initiate_data_ingestion`
# method reads a dataset from a specified location, creates necessary directories
# if they do not exist, saves the raw dataset, performs a train-test split, and
# saves the resulting training and testing datasets to their respective file
# paths. If any exceptions occur during this process, they are caught and raised
# as a `CustomException` with the relevant error information.

if __name__ == "__main__":

    data_ingestion = DataIngestion()
    train_data_path, test_data_path = data_ingestion.initiate_data_ingestion()

    data_transformation = DataTransformation()
    train_arr, test_arr,_ = data_transformation.initiate_data_transformation(train_data_path, test_data_path)

    model_trainer = ModelTrainer()
    print(model_trainer.initiate_model_trainer(train_arr, test_arr))


# The above code block checks if the script is being run as the main program. If it
# is, it creates an instance of the `DataIngestion` class and calls the
# `initiate_data_ingestion` method to start the data ingestion process. This
# allows the script to be executed directly, and the data ingestion will be
# performed when the script is run.