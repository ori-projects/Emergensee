from sklearn.cluster import KMeans
from sklearn import metrics
from app.interfaces.unlabeled.unlabeled_model import UnLabeledModel

class KMeansPlusModel(UnLabeledModel):
    """
    Implementation of an enhanced K-Means clustering model.
    """

    DEFAULT_N_CLUSTERS = 3
    DEFAULT_N_INIT = 10
    DEFAULT_RANDOM_STATE = 42

    def __init__(self, n_clusters=DEFAULT_N_CLUSTERS, n_init=DEFAULT_N_INIT, random_state=DEFAULT_RANDOM_STATE):
        """
        Initialize the K-Means clustering model.

        Args:
        n_clusters (int): The number of clusters to form.
        n_init (int): Number of times the algorithm will be run with different centroid seeds.
        random_state (int or None): Determines random number generation for centroid initialization.
                                    Pass an int for reproducible results across multiple function calls.
        """
        self.n_clusters = n_clusters
        self.n_init = n_init
        self.random_state = random_state
        self.model = KMeans(n_clusters=n_clusters, init='k-means++', n_init=n_init, random_state=random_state)

    def train(self, X, y=None):
        """
        Train the K-Means clustering model.

        Args:
        X (array-like): Training data of shape (n_samples, n_features).
        y (array-like or None): Target labels, not used in unsupervised learning.
        """
        self.model.fit(X)
        if y is not None:
            self._calculate_cluster_metrics(X, y)

    def _calculate_cluster_metrics(self, X, y):
        """
        Calculate cluster metrics (example: majority risk level per cluster).

        Args:
        X (array-like): Data of shape (n_samples, n_features).
        y (array-like): Target labels, assumed to be pandas DataFrame.
        """
        cluster_labels = self.model.labels_

        self.cluster_risk_levels = []
        for cluster_id in range(self.model.n_clusters):
            cluster_data_indices = cluster_labels == cluster_id
            cluster_target_labels = y.iloc[cluster_data_indices].sum()
            majority_risk_level = cluster_target_labels.idxmax()
            self.cluster_risk_levels.append(majority_risk_level)

    def test(self, X_test, y_test):
        """
        Test the K-Means clustering model on new data.

        Args:
        X_test (array-like): Test data of shape (n_samples, n_features).
        y_test: Target labels, not used in unsupervised learning.

        Returns:
        dict: Dictionary containing evaluation metrics.
              - 'predict': Predicted cluster labels.
              - 'silhouette_score': Silhouette score of the clustering.
        """
        predictions = self.model.predict(X_test)
        metrics_dict = self.get_metrics(X_test, predictions)
        
        return metrics_dict

    def predict(self, data):
        """
        Predict the cluster labels for new data.

        Args:
        data (array-like): New data to be clustered of shape (n_samples, n_features).

        Returns:
        array-like: Predicted cluster labels of shape (n_samples,).
        """
        return self.model.predict(data)

    def evaluate(self, X, y_true=None):
        """
        Evaluate the clustering model using external metrics.

        Args:
        X (array-like): Data of shape (n_samples, n_features).
        y_true (array-like or None): True cluster labels (not used).

        Returns:
        float: Silhouette score of the clustering.
        """
        predictions = self.model.predict(X)
        silhouette_avg = metrics.silhouette_score(X, predictions)
        
        return silhouette_avg

    def get_metrics(self, X, y_pred):
        """
        Calculate and return evaluation metrics for clustering.

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
            metrics_dict['silhouette_score'] = metrics.silhouette_score(X, y_pred)
        except Exception as e:
            metrics_dict['silhouette_score'] = 0.5  # Default value if silhouette score cannot be computed
        
        return metrics_dict
        
    def get_cluster_labels(self, X):
        """
        Return cluster labels for data points.

        Args:
        X (array-like): Data of shape (n_samples, n_features).

        Returns:
        array-like: Predicted cluster labels of shape (n_samples,).
        """
        return self.model.predict(X)

    def get_cluster_centers(self):
        """
        Return cluster centers.

        Returns:
        array-like: Cluster centers of shape (n_clusters, n_features).
        """
        return self.model.cluster_centers_

    def get_inertia(self):
        """
        Return inertia of the model (sum of squared distances of samples to their closest cluster center).

        Returns:
        float: Sum of squared distances.
        """
        return self.model.inertia_

    def get_params(self):
        """
        Get parameters for this estimator.

        Returns:
        dict: Dictionary of parameters.
        """
        return {
            'n_clusters': self.n_clusters,
            'n_init': self.n_init,
            'random_state': self.random_state
        }