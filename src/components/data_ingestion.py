import os
import sys
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from src.exception import CustomException
from src.logger import logging

filepath = "./data/data.csv"  # Ensure this path and file exist
if not os.path.exists(filepath):
    logging.error(f"File not found: {filepath}")
    raise FileNotFoundError(f"File not found: {filepath}")

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__))))


@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join("artifacts", "train.csv")
    test_data_path: str = os.path.join("artifacts", "test.csv")
    raw_data_path: str = os.path.join("artifacts", "data.csv")


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            # Read the dataset
            df = pd.read_csv(filepath)
            logging.info("Exported the dataset as a dataframe")

            # Create directories for artifacts
            os.makedirs(
                os.path.dirname(self.ingestion_config.raw_data_path), exist_ok=True
            )

            # Save raw data
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            # Split into train and test sets
            logging.info("Train-Test Split initialized")
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=32)

            # Save train and test sets
            train_set.to_csv(
                self.ingestion_config.train_data_path, index=False, header=True
            )
            test_set.to_csv(
                self.ingestion_config.test_data_path, index=False, header=True
            )

            logging.info("Data ingestion completed successfully")
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,
            )
        except Exception as e:
            raise CustomException(e, sys)


if __name__ == "__main__":
    try:
        obj = DataIngestion()
        obj.initiate_data_ingestion()
    except Exception as e:
        logging.error(f"An error occurred: {e}")
