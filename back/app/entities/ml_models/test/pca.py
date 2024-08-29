import numpy as np
from sklearn.decomposition import PCA
from app.interfaces.unlabeled.unlabeled_model import UnLabeledModel

class PcaModel(UnLabeledModel):
    """
    Implementation of a Principal Component Analysis model (PCAModel).
    """

    def __init__(self, n_components=None):
        """
        Initialize the PCA model.

        Args:
        n_components (int or None): Number of components to keep.
                                   If None, all components are kept.
        """
        self.model = PCA(n_components=n_components)

    def train(self, train_data):
        """
        Train the Principal Component Analysis model on the training data.

        Args:
        train_data (array-like): Training data of shape (n_samples, n_features).
        """
        self.model.fit(train_data)
    
    def test(self, test_data):
        """
        Transform the test data using the trained PCA model and compute metrics.

        Args:
        test_data (array-like): Test data of shape (n_samples, n_features).

        Returns:
        dict: Dictionary containing metrics computed from the test data.
              - 'predict': Transformed test data.
              - 'reconstruction_error': Mean reconstruction error of the original data.
              - 'explained_variance_ratio': Variance explained by each principal component.
        """
        transformed_data = self.model.transform(test_data)
        return self.get_metrics(transformed_data, test_data)
    
    def predict(self, data):
        """
        Transform new data using the trained PCA model.

        Args:
        data (array-like): New data to be transformed of shape (n_samples, n_features).

        Returns:
        array-like: Transformed data of shape (n_samples, n_components).
        """
        return self.model.transform(data)

    def get_metrics(self, transformed_data, original_data):
        """
        Calculate metrics based on the transformed and original data.

        Args:
        transformed_data (array-like): Transformed data of shape (n_samples, n_components).
        original_data (array-like): Original data of shape (n_samples, n_features).

        Returns:
        dict: Dictionary containing computed metrics.
              - 'predict': Transformed data.
              - 'reconstruction_error': Mean reconstruction error between original and reconstructed data.
              - 'explained_variance_ratio': Explained variance ratio by each principal component.
        """
        reconstruction_error = np.mean(np.sum(np.square(original_data - self.model.inverse_transform(transformed_data)), axis=1))
        explained_variance_ratio = self.model.explained_variance_ratio_

        metrics_dict = {}
        metrics_dict['predict'] = transformed_data
        metrics_dict['reconstruction_error'] = reconstruction_error
        metrics_dict['explained_variance_ratio'] = explained_variance_ratio

        return metrics_dict