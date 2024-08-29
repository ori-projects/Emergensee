import pandas as pd
from sklearn.model_selection import train_test_split
from app.interfaces.preprocessor import Preprocessor

class MaternalPreprocessor(Preprocessor):
    def load(self, file_path):
        """
        Load the dataset from the file path.

        Args:
        file_path (str): File path to the dataset.

        Returns:
        pandas.DataFrame: Loaded dataset.
        """
        return pd.read_csv(file_path, header=0)

    def clean(self, df):
        """
        Perform any necessary data cleaning operations on the dataset.

        Args:
        df (pandas.DataFrame): Input dataset.

        Returns:
        pandas.DataFrame: Cleaned dataset.
        """
        return df
    
    def convert(self, df):
        """
        Perform data conversion operations on the dataset, specifically one-hot encoding categorical variables.

        Args:
        df (pandas.DataFrame): Input dataset.

        Returns:
        pandas.DataFrame: Converted dataset with categorical variables one-hot encoded.
        """
        return pd.get_dummies(df)  # One-hot encode categorical variables
    
    def get_train_test(self, df):
        """
        Split the dataset into training and testing sets.

        Args:
        df (pandas.DataFrame): Input dataset.

        Returns:
        tuple: Four arrays X_train, X_test, y_train, y_test containing features and labels respectively.
        """
        X = df.filter(regex='^(?!RiskLevel_)')  # Select features excluding RiskLevel_ columns
        y = df[['RiskLevel_high_risk', 'RiskLevel_low_risk', 'RiskLevel_mid_risk']]  # Select RiskLevel_ columns as labels
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=10)
        
        return X_train, X_test, y_train, y_test
    
    @staticmethod
    def get_row_to_predict(row, X):
        """
        Prepare a row of data to be predicted by ensuring it has the same columns as X.

        Args:
        row (pandas.Series): Row of data to predict.
        X (pandas.DataFrame): DataFrame with columns that row should match.

        Returns:
        pandas.DataFrame: Row prepared for prediction.
        """
        return row