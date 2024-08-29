from abc import ABC, abstractmethod

class UnLabeledModel(ABC):
    """
    Abstract base class for machine learning models.
    """

    @abstractmethod
    def train(self, df):
        """
        Abstract method to train the model.

        Args:
        df (DataFrame): The training data.

        Returns:
        None
        """
        pass

    @abstractmethod
    def test(self, df):
        """
        Abstract method to test the model.

        Args:
        df (DataFrame): The testing data.

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
        array-like: The predicted values or clusters.
        """
        pass
    
    @abstractmethod
    def get_metrics(self, test_data, test_labels):
        """
        Abstract method to get metrics of the model.

        Args:
        test_data (array-like): The data used for testing.
        test_labels (array-like): The true labels or values for the test data.

        Returns:
        dict: A dictionary containing various performance metrics.
        """
        pass