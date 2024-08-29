from sklearn.cluster import Birch
from sklearn.metrics import silhouette_score
from app.interfaces.unlabeled.unlabeled_model import UnLabeledModel

class BirchClusteringModel(UnLabeledModel):
    def __init__(self, threshold=0.1, branching_factor=50, n_clusters=3):
        self.threshold = threshold
        self.branching_factor = branching_factor
        self.n_clusters = n_clusters
        self.model = Birch(
            threshold=self.threshold, 
            branching_factor=self.branching_factor, 
            n_clusters=self.n_clusters
        )
        
    def train(self, X, y):
        """
        Train the Birch Clustering model and calculate metrics.
        """
        self.model.fit(X)
        cluster_labels = self.model.labels_

        self.cluster_risk_levels = []
        for cluster_id in range(3):
            cluster_data_indices = cluster_labels == cluster_id
            cluster_target_labels = y.iloc[cluster_data_indices].sum()
            majority_risk_level = cluster_target_labels.idxmax()
            self.cluster_risk_levels.append(majority_risk_level)
    
    def test(self, X_test, y_test):
        """
        Test the Birch Clustering model on unlabeled data and return the metrics.
        """
        prediction = self.model.predict(X_test)
        metrics_dict = self.get_metrics(X_test, prediction)
        
        return metrics_dict
    
    def predict(self, data):
        return self.model.predict(data)

    def get_metrics(self, X, y_pred):
        """
        Calculate and return evaluation metrics for clustering.
        """
        metrics_dict = {}
        metrics_dict['predict'] = y_pred
        
        try:
            metrics_dict['silhouette_score'] = silhouette_score(X, y_pred)
        except:
            metrics_dict['silhouette_score'] = 0.5
        
        return metrics_dict