from app.entities.ml_models.labeled.decision_tree import DecisionTreeModel
from app.entities.ml_models.labeled.linear_regression import LinearRegressionModel
from app.entities.ml_models.labeled.logistic_regression import LogisticRegressionModel
from app.entities.ml_models.labeled.neural_network import NeuralNetworkModel
from app.entities.ml_models.labeled.random_forest import RandomForestModel
from app.entities.ml_models.labeled.svm import SvmModel
from app.entities.ml_models.test.pca import PcaModel
from app.entities.ml_models.unlabeled.birch_clustering import BirchClusteringModel
from app.entities.ml_models.unlabeled.bisecting_k_means import BisectingKMeansModel
from app.entities.ml_models.unlabeled.k_means import KMeansModel
from app.entities.ml_models.unlabeled.k_means_plus import KMeansPlusModel
from app.entities.ml_models.unlabeled.mini_batch_k_means import MiniBatchKMeansModel
from app.entities.ml_models.unlabeled.mini_batch_plus_k_means import MiniBatchPlusKMeansModel

class Models:
    @staticmethod
    def get_labeled_ml_models():
        """
        Static method to retrieve a list of labeled machine learning models.

        Returns:
        list: A list of labeled machine learning model instances.
        """
        return [DecisionTreeModel(), 
                LinearRegressionModel(), 
                LogisticRegressionModel(), 
                NeuralNetworkModel(), 
                RandomForestModel(), 
                SvmModel()
                ]
    
    @staticmethod
    def get_unlabeled_ml_models():
        """
        Static method to retrieve a list of unlabeled machine learning models.

        Returns:
        list: A list of unlabeled machine learning model instances.
        """
        return [BirchClusteringModel(),
                BisectingKMeansModel(),
                KMeansModel(),
                KMeansPlusModel(),
                MiniBatchKMeansModel(),
                MiniBatchPlusKMeansModel()
                ]  
    
    @staticmethod
    def get_test_ml_models():
        """
        Static method to retrieve a list of test machine learning models.

        Returns:
        list: A list of test machine learning model instances.
        """
        return [PcaModel()
                ]