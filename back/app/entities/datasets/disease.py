import pandas as pd

from app.entities.configs.datasets import Datasets
from app.entities.configs.models import Models
from app.services.preprocesses.disease_preprocessor import DiseasePreprocessor
from app.services.proccessors.disease_processor import DiseaseProcessor

class Disease:
    """
    A class representing the Disease dataset processing pipeline.

    Attributes:
    _instance (Disease): Singleton instance of the Disease class.
    path (str): Path to the raw Disease dataset.
    df (DataFrame or None): Processed DataFrame of Disease dataset.
    df_raw (DataFrame or None): Raw DataFrame loaded from Disease dataset.
    X_train (DataFrame or None): Features for training.
    y_train (DataFrame or None): Labels for training.
    X_test (DataFrame or None): Features for testing.
    y_test (DataFrame or None): Labels for testing.
    preprocessor (DiseasePreprocessor): Instance of DiseasePreprocessor for data preprocessing.
    processor (DiseaseProcessor): Instance of DiseaseProcessor for model processing.
    models (list): List of labeled machine learning model instances.
    metrics (list): List to store evaluation metrics.
    min_max (None): Placeholder for min-max scaling parameters (not used in current implementation).
    frequencies (None): Placeholder for feature frequencies (not used in current implementation).
    rows (int or None): Number of rows in the processed dataset.
    risk_weight (int): Weight for risk assessment (default is 0).

    Methods:
    __new__(): Singleton pattern to ensure only one instance of Disease class exists.
    initialize(): Initializes instance attributes and sets up necessary objects.
    preprocess(): Executes data preprocessing steps using DiseasePreprocessor.
    process(): Trains models and evaluates their performance using DiseaseProcessor.
    predict(row_to_predict): Predicts using trained models on a new input row.
    preprocess_row(input_row): Preprocesses a single input row for prediction.
    """

    _instance = None

    def __new__(cls):
        """
        Ensures only one instance of Disease class exists (Singleton pattern).

        Returns:
        Disease: The single instance of the Disease class.
        """
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.initialize()
        return cls._instance

    def initialize(self):
        """
        Initializes instance attributes and sets up necessary objects.
        """
        self.path = Datasets.raw_disease
        self.df = None
        self.df_raw = None
        self.X_train = None
        self.y_train = None
        self.X_test = None
        self.y_test = None
        self.preprocessor = DiseasePreprocessor()
        self.processor = DiseaseProcessor()
        self.models = Models.get_labeled_ml_models()
        self.metrics = []
        self.min_max = None  # Placeholder for min-max scaling (not used)
        self.frequencies = None  # Placeholder for feature frequencies (not used)
        self.rows = None
        self.risk_weight = 0

    def preprocess(self):
        """
        Executes data preprocessing steps using DiseasePreprocessor.
        """
        self.df_raw = self.preprocessor.load(self.path)
        self.df = self.preprocessor.clean(self.df_raw)
        self.df = self.preprocessor.convert(self.df)
        self.df.to_csv(Datasets.disease, index=False)
        self.rows = len(self.df)
        self.X_train, self.X_test, self.y_train, self.y_test = self.preprocessor.get_train_test(self.df)

    def process(self):
        """
        Trains models and evaluates their performance using DiseaseProcessor.
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
        df_row['Critical'] = 0  # Adding a placeholder column 'Critical' with default value 0
        df_row = self.preprocessor.convert(df_row)
        df_row = df_row.drop(columns=['Critical'])  # Dropping the 'Critical' column
        df_row = df_row.reindex(columns=self.X_train.columns, fill_value=0)  # Reindexing to match training data columns
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
                "type": "Labeled"
            })

        return {
            "dataset_name": "Disease Dataset",
            "relative_weight": self.risk_weight,
            "number_of_lines": len(self.preprocessor.load(self.path)),
            "models": model_info
        }