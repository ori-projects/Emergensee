from abc import ABC, abstractmethod

class LabeledProcessor(ABC):
    @abstractmethod
    def train_models(self, models, X_train, y_train):
        """
        Abstract method to train models.

        Args:
        models (dict): A dictionary containing model names as keys and model instances as values.
        X_train (array-like): The training data features.
        y_train (array-like): The training data labels.

        Returns:
        dict: A dictionary containing trained model instances.
        """
        pass
        
    @abstractmethod
    def test_models(self, models, X_test, y_test):
        """
        Abstract method to test models.

        Args:
        models (dict): A dictionary containing model names as keys and model instances as values.
        X_test (array-like): The testing data features.
        y_test (array-like): The testing data labels.

        Returns:
        dict: A dictionary containing model names as keys and their corresponding accuracy scores.
        """
        pass