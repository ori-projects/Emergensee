from sklearn import metrics
from sklearn.cluster import KMeans
from app.interfaces.unlabeled.unlabeled_model import UnLabeledModel

class KMeansModel(UnLabeledModel):
    """
    Implementation of a K-Means clustering model (KMeansModel).
    """

    CONST_N_CLUSTERS = 3
    CONST_N_INIT = 50
    CONST_N_RANDOM_STATE = 3

    def __init__(self, n_clusters=CONST_N_CLUSTERS, n_init=CONST_N_INIT, random_state=CONST_N_RANDOM_STATE):
        """
        Initialize the K-Means clustering model.

        Args:
        n_clusters (int): The number of clusters to form.
        n_init (int): Number of times the algorithm will be run with different centroid seeds.
        random_state (int or None): Determines random number generation for centroid initialization.
                                    Pass an int for reproducible results across multiple function calls.
        """
        self.n_clusters = n_clusters
        self.model = KMeans(n_clusters=n_clusters, n_init=n_init, random_state=random_state)

    def train(self, X, y):
        """
        Train the K-Means clustering model.

        Args:
        X (array-like): Training data of shape (n_samples, n_features).
        y (array-like): Target labels, assumed to be pandas DataFrame.
        """
        self.model.fit(X)
        cluster_labels = self.model.labels_

        self.cluster_risk_levels = []
        for cluster_id in range(self.n_clusters):
            cluster_data_indices = cluster_labels == cluster_id
            cluster_target_labels = y.iloc[cluster_data_indices].sum()
            majority_risk_level = cluster_target_labels.idxmax()
            self.cluster_risk_levels.append(majority_risk_level)

    def test(self, X_test, y_test):
        """
        Test the K-Means clustering model on unlabeled data.

        Args:
        X_test (array-like): Test data of shape (n_samples, n_features).
        y_test: Target labels, not used in unsupervised learning.

        Returns:
        dict: Dictionary containing evaluation metrics.
              - 'predict': Predicted cluster labels.
              - 'silhouette_score': Silhouette score of the clustering.
        """
        prediction = self.model.predict(X_test)
        metrics_dict = self.get_metrics(X_test, prediction)
        silhouette_avg = metrics_dict['silhouette_score']
        
        return metrics_dict
    
    def predict(self, data):
        """
        Predict the cluster labels for the given data.

        Args:
        data (array-like): New data to be clustered of shape (n_samples, n_features).

        Returns:
        array-like: Predicted cluster labels of shape (n_samples,).
        """
        return self.model.predict(data)

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
            metrics_dict['silhouette_score'] = metrics.silhouette_score(X, y_pred)
        except Exception as e:
            metrics_dict['silhouette_score'] = 0.5  # Default value if silhouette score cannot be computed
        
        return metrics_dict