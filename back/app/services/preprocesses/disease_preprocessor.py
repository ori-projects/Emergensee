import pandas as pd
from sklearn.model_selection import train_test_split
from app.interfaces.preprocessor import Preprocessor
from app.entities.configs.datasets import Datasets

class DiseasePreprocessor(Preprocessor):
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
        df.dropna(inplace=True)  # Drop rows with NaN values
        return df
    
    def convert(self, df):
        """
        Perform data conversion operations on the dataset.

        Args:
        df (pandas.DataFrame): Input dataset.

        Returns:
        pandas.DataFrame: Converted dataset with categorical variables one-hot encoded and target variable encoded as binary.
        """
        # One-hot encode specified categorical columns
        df = pd.get_dummies(df, columns=['Critical_Feelings', 'Discharge', 'Feelings_and_Urge', 'Pain_and_Infection', 'Physical_Conditions', 'Disease'])
        
        # Encode the target variable 'Critical' as binary (Critical: 1, Not Critical: 0)
        df['Critical'] = df['Critical'].map({'Critical': 1, 'Not Critical': 0})
        
        return df

    def get_train_test(self, df):
        """
        Split the dataset into training and testing sets.

        Args:
        df (pandas.DataFrame): Input dataset.

        Returns:
        tuple: Four arrays X_train, X_test, y_train, y_test containing features and labels respectively.
        """
        X = df.drop(Datasets.disease_train, axis=1)  # Features are all columns except the target variable
        y = df[Datasets.disease_train]  # Target variable 'Critical'
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=10)
        
        return X_train, X_test, y_train, y_test