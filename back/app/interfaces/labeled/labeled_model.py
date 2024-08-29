from abc import ABC, abstractmethod

class LabeledModel(ABC):
    """
    Abstract base class for machine learning models.
    """

    @abstractmethod
    def train(self, X_train, y_train):
        """
        Abstract method to train the model.

        Args:
        X_train (array-like): The training data features.
        y_train (array-like): The training data labels.

        Returns:
        None
        """
        pass

    @abstractmethod
    def test(self, X_test, y_test):
        """
        Abstract method to test the model.

        Args:
        X_test (array-like): The testing data features.
        y_test (array-like): The testing data labels.

        Returns:
        dict: A dictionary containing model performance metrics.
        """
        pass

    @abstractmethod
    def predict(self, df):
        """
        Abstract method to make predictions using the model.

        Args:
        df (DataFrame): The data to predict on.

        Returns:
        array-like: The predicted labels or values.
        """
        pass
    
    @abstractmethod
    def get_metrics(self, y_test, y_pred):
        """
        Abstract method to get metrics of the model.

        Args:
        y_test (array-like): The true labels.
        y_pred (array-like): The predicted labels.

        Returns:
        dict: A dictionary containing various performance metrics.
        """
        pass