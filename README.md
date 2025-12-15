# Student Performance Prediction MLOps Project

This is an end-to-end Machine Learning project to predict student performance (Final Grade G3) based on various demographic and academic attributes from the Portuguese school dataset.

The project demonstrates a complete MLOps pipeline including Data Ingestion, Validation, Transformation, Model Training, and Deployment via a Flask Web Application.

## 🚀 Features

*   **End-to-End Pipeline**: Modular code structure for reproducibility.
*   **Data Validation**: Ensures data schema consistency (`schema.yaml`).
*   **Data Transformation**: Pipelines for scaling numerical and encoding categorical features.
*   **Model Training**: Trains multiple regression models (Linear, XGBoost, CatBoost, RandomForest, etc.) and picks the best one.
*   **Experiment Tracking**: Integrated with **MLflow** and **DagsHub** for tracking metrics and parameters.
*   **Web Application**: User-friendly interface built with **Flask** and **Tailwind CSS**.
*   **Data Version Control**: configured with **DVC**.

## 📂 Project Structure

```
├── artifacts/          # Stores generated files (data, models, preprocessors)
├── notebook/           # Jupyter notebooks for EDA and Model Training
├── src/
│   └── mlproject/
│       ├── components/ # Core logic (Ingestion, Transformation, Trainer)
│       ├── pipeline/   # Prediction pipeline
│       ├── logger.py   # Logging configuration
│       ├── exception.py# Custom exception handling
│       └── utils.py    # Helper functions (save/load objects)
├── templates/          # HTML templates for the web app
├── app.py              # Flask application entry point
├── main.py             # MLOps pipeline entry point
├── requirements.txt    # Project dependencies
└── schema.yaml         # Data validation schema
```

## 🛠️ Installation & Usage

1.  **Clone the Repository**
    ```bash
    git clone https://github.com/Subamprasad/mlops1.git
    cd mlops1
    ```

2.  **Create a Virtual Environment**
    ```bash
    conda create -p venv python==3.8 -y
    conda activate venv/
    ```

3.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

## 🏃‍♂️ Running the Project

### 1. Training the Pipeline
To run the full data ingestion, transformation, and model training pipeline:

```bash
python main.py
```
*This will process the data in `artifacts/` and save the best model as `artifacts/model.pkl`.*

### 2. Running the Web App
To start the prediction interface:

```bash
python app.py
```
Open **http://localhost:5000** in your browser.

## 📊 MLflow Experiment Tracking
This project logs experiments to MLflow (configured for DagsHub).
To view experiments, ensure `MLFLOW_TRACKING_URI` is set (or configured in `model_trainer.py`).

## 📓 Notebooks
*   `notebook/1_EDA.ipynb`: Exploratory Data Analysis.
*   `notebook/2_MODEL_TRAINING.ipynb`: Model training experiments.

## 📝 License
This project is for educational purposes.
