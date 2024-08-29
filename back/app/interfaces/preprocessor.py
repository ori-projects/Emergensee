from abc import ABC, abstractmethod

class Preprocessor(ABC):
    @abstractmethod
    def load(self, file_path):
        """
        Abstract method to load a dataset.

        Args:
        file_path (str): The path to the dataset file.

        Returns:
        DataFrame or similar: The loaded dataset.
        """
        pass

    @abstractmethod
    def clean(self, df):
        """
        Abstract method to clean a dataset.

        Args:
        df (DataFrame or similar): The dataset to be cleaned.

        Returns:
        DataFrame or similar: The cleaned dataset.
        """
        pass

    @abstractmethod
    def convert(self, df):
        """
        Abstract method to convert categorical variables in a dataset to numerical labels.

        Args:
        df (DataFrame or similar): The dataset containing categorical variables.

        Returns:
        DataFrame or similar: The dataset with categorical variables converted to numerical labels.
        """
        pass

    @abstractmethod
    def get_train_test(self, df):
        """
        Abstract method to split a dataset into training and testing sets.

        Args:
        df (DataFrame or similar): The dataset containing features and labels.

        Returns:
        tuple: A tuple containing the training and testing sets for features and labels,
               in the order (X_train, X_test, y_train, y_test).
        """
        pass
