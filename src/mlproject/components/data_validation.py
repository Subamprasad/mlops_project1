import os
import sys
from src.mlproject.exception import CustomException
from src.mlproject.logger import logger
import pandas as pd
from dataclasses import dataclass
import yaml

@dataclass
class DataValidationConfig:
    status_file:str=os.path.join('artifacts','validation_status.txt')
    schema_file_path:str=os.path.join('schema.yaml')

class DataValidation:
    def __init__(self):
        self.validation_config = DataValidationConfig()

    def validate_all_columns(self, train_path, test_path):
        try:
            validation_status = None
            
            # Read Schema
            with open(self.validation_config.schema_file_path, 'r') as f:
                schema = yaml.safe_load(f)
                expected_columns = list(schema['columns'].keys())

            # Read Data
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            
            # Helper to check columns
            def check_columns(df, name):
                all_cols = list(df.columns)
                missing_cols = [col for col in expected_columns if col not in all_cols]
                
                if len(missing_cols) > 0:
                    logger.info(f"Validation FAILED for {name}. Missing columns: {missing_cols}")
                    return False
                return True

            train_status = check_columns(train_df, "Train Data")
            test_status = check_columns(test_df, "Test Data")

            validation_status = train_status and test_status

            with open(self.validation_config.status_file, 'w') as f:
                f.write(f"Validation Status: {validation_status}")

            logger.info(f"Data Validation Completed. Status: {validation_status}")
            return validation_status

        except Exception as e:
            raise CustomException(e,sys)
