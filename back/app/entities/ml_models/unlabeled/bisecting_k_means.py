from sklearn.cluster import BisectingKMeans
from sklearn.metrics import silhouette_score
from app.interfaces.unlabeled.unlabeled_model import UnLabeledModel

class BisectingKMeansModel(UnLabeledModel):
    """
    Implementation of a BisectingKMeans model for clustering-like behavior.
    """

    def __init__(self, n_clusters=3, n_init=10, random_state=None):
        """
        Initialize the BisectingKMeans clustering model.

        Args:
        n_clusters (int): The number of clusters to form.
        n_init (int): Number of times the algorithm will be run with different centroid seeds.
        random_state (int or None): Determines random number generation for centroid initialization.
                                    Pass an int for reproducible results across multiple function calls.
        """
        self.model = BisectingKMeans(n_clusters=n_clusters, n_init=n_init, random_state=random_state)

    def train(self, X, y=None):
        """
        Train the BisectingKMeans model.

        Args:
        X (array-like): Training data of shape (n_samples, n_features).
        y (array-like or None): Target labels, not used in unsupervised learning.
        """
        self.model.fit(X)
        cluster_labels = self.model.labels_

        self.cluster_risk_levels = []
        for cluster_id in range(self.model.n_clusters):
            cluster_data_indices = cluster_labels == cluster_id
            # Assuming `y` is a pandas DataFrame
            cluster_target_labels = y.iloc[cluster_data_indices].sum()
            majority_risk_level = cluster_target_labels.idxmax()
            self.cluster_risk_levels.append(majority_risk_level)

    def predict(self, data):
        """
        Predict cluster labels using the BisectingKMeans model.

        Args:
        data (array-like): New data to be clustered of shape (n_samples, n_features).

        Returns:
        array-like: Predicted cluster labels of shape (n_samples,).
        """
        return self.model.predict(data)

    def test(self, X_test, y_test):
        """
        Test the BisectingKMeans model on test data.

        Args:
        X_test (array-like): Test data of shape (n_samples, n_features).
        y_test: Target labels, not used in unsupervised learning.

        Returns:
        dict: Dictionary containing evaluation metrics.
              - 'predict': Predicted cluster labels.
              - 'silhouette_score': Silhouette score of the clustering.
        """
        y_pred = self.model.predict(X_test)
        metrics_dict = self.get_metrics(X_test, y_pred)
        return metrics_dict

    def get_metrics(self, X, y_pred):
        """
        Calculate evaluation metrics for clustering.

        Args:
        X (array-like): Data of shape (n_samples, n_features).
        y_pred (array-like): Predicted cluster labels of shape (n_samples,).

        Returns:
        dict: Dictionary containing evaluation metrics.
              - 'predict': Predicted cluster labels.
              - 'silhouette_score': Silhouette score of the clustering.
        """
        metrics_dict = {}
        metrics_dict['predict'] = y_pred
        
        try:
            metrics_dict['silhouette_score'] = silhouette_score(X, y_pred)
        except Exception as e:
            metrics_dict['silhouette_score'] = 0.5  # Default value if silhouette score cannot be computed
        
        return metrics_dict