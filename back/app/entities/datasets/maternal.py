import pandas as pd

from app.entities.configs.datasets import Datasets
from app.entities.configs.models import Models
from app.services.preprocesses.maternal_preprocessor import MaternalPreprocessor
from app.services.proccessors.maternal_processor import MaternalProcessor

class Maternal:
    """
    A class representing the Maternal Health Risk dataset processing pipeline.

    Attributes:
    _instance (Maternal): Singleton instance of the Maternal class.
    path (str): Path to the raw Maternal Health Risk dataset.
    df (DataFrame or None): Processed DataFrame of Maternal Health Risk dataset.
    df_raw (DataFrame or None): Raw DataFrame loaded from Maternal Health Risk dataset.
    X_train (DataFrame or None): Features for training.
    y_train (DataFrame or None): Labels for training.
    X_test (DataFrame or None): Features for testing.
    y_test (DataFrame or None): Labels for testing.
    preprocessor (MaternalPreprocessor): Instance of MaternalPreprocessor for data preprocessing.
    processor (MaternalProcessor): Instance of MaternalProcessor for model processing.
    models (list): List of unlabeled machine learning model instances.
    metrics (list): List to store evaluation metrics.
    min_max (None): Placeholder for min-max scaling parameters (not used in current implementation).
    frequencies (None): Placeholder for feature frequencies (not used in current implementation).
    rows (int or None): Number of rows in the processed dataset.
    risk_weight (int): Weight for risk assessment (default is 0).

    Methods:
    __new__(): Singleton pattern to ensure only one instance of Maternal class exists.
    initialize(): Initializes instance attributes and sets up necessary objects.
    preprocess(): Executes data preprocessing steps using MaternalPreprocessor.
    process(): Trains models and evaluates their performance using MaternalProcessor.
    predict(row_to_predict): Predicts using trained models on a new input row.
    preprocess_row(input_row): Preprocesses a single input row for prediction.
    """

    _instance = None

    def __new__(cls):
        """
        Ensures only one instance of Maternal class exists (Singleton pattern).

        Returns:
        Maternal: The single instance of the Maternal class.
        """
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.initialize()
        return cls._instance

    def initialize(self):
        """
        Initializes instance attributes and sets up necessary objects.
        """
        self.path = Datasets.raw_maternal
        self.df = None
        self.df_raw = None
        self.X_train = None
        self.y_train = None
        self.X_test = None
        self.y_test = None
        self.preprocessor = MaternalPreprocessor()
        self.processor = MaternalProcessor()
        self.models = Models.get_unlabeled_ml_models()
        self.metrics = []
        self.min_max = None  # Placeholder for min-max scaling (not used)
        self.frequencies = None  # Placeholder for feature frequencies (not used)
        self.rows = None
        self.risk_weight = 0

    def preprocess(self):
        """
        Executes data preprocessing steps using MaternalPreprocessor.
        """
        self.df_raw = self.preprocessor.load(self.path)
        self.df = self.preprocessor.clean(self.df_raw)
        self.df = self.preprocessor.convert(self.df)
        self.df.to_csv(Datasets.maternal, index=False)
        self.rows = len(self.df)
        self.X_train, self.X_test, self.y_train, self.y_test = self.preprocessor.get_train_test(self.df)

    def process(self):
        """
        Trains models and evaluates their performance using MaternalProcessor.
        """
        self.processor.train_models(self.models, self.X_train, self.y_train)
        self.metrics.append(self.processor.test_models(self.models, self.X_test, self.y_test))

    def predict(self, row_to_predict):
        """
        Predicts using trained models on a new input row.

        Args:
        row_to_predict (DataFrame): Input row to predict.

        Returns:
        list: Predicted values from each model.
        """
        return self.processor.predict_models(self.models, row_to_predict)

    def preprocess_row(self, input_row):
        """
        Preprocesses a single input row for prediction.

        Args:
        input_row (dict or list): Input row to preprocess.

        Returns:
        DataFrame: Preprocessed input row as DataFrame.
        """
        df_row = pd.DataFrame([input_row])
        df_row = self.preprocessor.convert(df_row)
        df_row = df_row.reindex(columns=self.X_train.columns, fill_value=0)
        return df_row
    
    def get_dataset_info(self):
        """
        Returns information about the dataset and models.

        Returns:
        dict: A dictionary containing dataset information and model details.
        """
        model_info = []
        for model in self.models:
            model_info.append({
                "name": model.__class__.__name__,
                "type": "Unlabeled"
            })

        return {
            "dataset_name": "Maternal Health Risk Dataset",
            "relative_weight": self.risk_weight,
            "number_of_lines": len(self.preprocessor.load(self.path)),
            "models": model_info
        }