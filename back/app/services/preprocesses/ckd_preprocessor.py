import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from app.entities.configs.datasets import Datasets
from app.interfaces.preprocessor import Preprocessor

class CkdPreprocessor(Preprocessor):
    def load(self, file_path):
        """
        Load the dataset from the file path.

        Args:
        file_path (str): File path to the dataset.

        Returns:
        pandas.DataFrame: Loaded dataset.
        """
        return pd.read_csv(file_path)

    def clean(self, df):
        """
        Perform data cleaning operations on the dataset.

        Args:
        df (pandas.DataFrame): Input dataset.

        Returns:
        pandas.DataFrame: Cleaned dataset.
        """
        # Replace '?' with NaN and drop rows with NaN values
        df.replace('?', np.nan, inplace=True)
        df.dropna(inplace=True)

        return df

    def convert(self, df):
        """
        Perform data conversion operations on the dataset.

        Args:
        df (pandas.DataFrame): Input dataset.

        Returns:
        pandas.DataFrame: Converted dataset with categorical variables one-hot encoded and target variable encoded as binary.
        """
        # Define categorical columns for one-hot encoding
        categorical_cols = ['rcb', 'pc', 'pcc', 'ba', 'htn', 'dm', 'cad', 'appet', 'pe', 'ane']
        df = pd.get_dummies(df, columns=categorical_cols)  # One-hot encode categorical variables

        # Encode the target variable 'ckd' as binary (ckd: 1, notckd: 0)
        df['ckd'] = df['ckd'].map({'ckd': 1, 'notckd': 0})
        
        return df
    
    def get_train_test(self, df):
        """
        Split the dataset into training and testing sets.

        Args:
        df (pandas.DataFrame): Input dataset.

        Returns:
        tuple: Four arrays X_train, X_test, y_train, y_test containing features and labels respectively.
        """
        X = df.drop(columns=[Datasets.ckd_train])  # Features are all columns except the target variable
        y = df[Datasets.ckd_train]  # Target variable 'ckd'
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=10)
        
        return X_train, X_test, y_train, y_test