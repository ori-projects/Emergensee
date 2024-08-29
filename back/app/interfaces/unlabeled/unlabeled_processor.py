from abc import ABC, abstractmethod

class UnLabeledProcessor(ABC):
    """
    Abstract base class for processing machine learning models without labeled data.
    """

    @abstractmethod
    def train_models(self, models, X_train, y_train):
        """
        Abstract method to train multiple models.

        Args:
        models (dict): A dictionary containing model names as keys and model instances as values.
        X_train (array-like): The training data features.
        y_train (array-like): The training data labels (though typically not used for true unsupervised models).

        Returns:
        dict: A dictionary containing trained model instances.
        """
        pass
        
    @abstractmethod
    def test_models(self, models, X_test):
        """
        Abstract method to test multiple models.

        Args:
        models (dict): A dictionary containing model names as keys and model instances as values.
        X_test (array-like): The testing data features.

        Returns:
        dict: A dictionary containing model names as keys and their corresponding performance metrics.
        """
        pass