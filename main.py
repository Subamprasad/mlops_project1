from src.mlproject.logger import logger
from src.mlproject.exception import CustomException
from src.mlproject.components.data_ingestion import DataIngestion
from src.mlproject.components.data_ingestion import DataIngestionConfig
from src.mlproject.components.data_validation import DataValidation
from src.mlproject.components.data_transformation import DataTransformation
from src.mlproject.components.model_trainer import ModelTrainer
import sys

if __name__ == "__main__":
    logger.info("The execution has started")
    
    try:
        # Data Ingestion
        data_ingestion = DataIngestion()
        train_data_path, test_data_path = data_ingestion.initiate_data_ingestion()
        print(f"Ingestion completed. Files created at: {train_data_path}, {test_data_path}")

        # Data Validation
        data_validation = DataValidation()
        data_validation.validate_all_columns(train_data_path, test_data_path)
        print("Validation completed.")

        # Data Transformation
        data_transformation = DataTransformation()
        train_arr, test_arr, _ = data_transformation.initiate_data_transformation(train_data_path, test_data_path)
        print("Transformation completed.")

        # Model Training
        model_trainer = ModelTrainer()
        score = model_trainer.initiate_model_trainer(train_arr, test_arr)
        print(f"Model Training completed. Best Model R2 Score: {score}")
        
    except Exception as e:
        logger.error(e)
        raise CustomException(e,sys)