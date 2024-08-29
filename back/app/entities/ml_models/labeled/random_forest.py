from sklearn import metrics
from sklearn.ensemble import RandomForestClassifier
from app.interfaces.labeled.labeled_model import LabeledModel

class RandomForestModel(LabeledModel):
    """
    Implementation of a random forest classifier model (RandomForestModel).
    """

    CONST_N_ESTIMATORS = 500  # Increased number of estimators
    CONST_CRITERION = 'entropy'  # Trying a different criterion
    CONST_MAX_DEPTH = 20  # Limiting the maximum depth
    CONST_MIN_SAMPLES_SPLIT = 5  # Adjusting minimum samples required to split
    CONST_MIN_SAMPLES_LEAF = 2  # Adjusting minimum samples required at a leaf node

    def __init__(self, n_estimators=CONST_N_ESTIMATORS, criterion=CONST_CRITERION, max_depth=CONST_MAX_DEPTH, min_samples_split=CONST_MIN_SAMPLES_SPLIT, min_samples_leaf=CONST_MIN_SAMPLES_LEAF):
        """
        Initialize a RandomForestModel instance.

        Args:
        n_estimators (int, optional): Number of trees in the forest. Defaults to 500.
        criterion (str, optional): Function to measure the quality of a split ('gini' or 'entropy'). Defaults to 'entropy'.
        max_depth (int, optional): Maximum depth of the trees. Defaults to 20.
        min_samples_split (int, optional): Minimum number of samples required to split an internal node. Defaults to 5.
        min_samples_leaf (int, optional): Minimum number of samples required to be at a leaf node. Defaults to 2.
        """
        self.model = RandomForestClassifier(
            n_estimators=n_estimators,
            criterion=criterion,
            max_depth=max_depth,
            min_samples_split=min_samples_split,
            min_samples_leaf=min_samples_leaf
        )

    def train(self, X_train, y_train):
        """
        Train the random forest classifier model.

        Args:
        X_train (array-like): Training data features.
        y_train (array-like): Training data labels.
        """
        self.model.fit(X_train, y_train)

    def test(self, X_test, y_test):
        """
        Test the random forest classifier model and return evaluation metrics.

        Args:
        X_test (array-like): Testing data features.
        y_test (array-like): Testing data labels.

        Returns:
        dict: A dictionary containing evaluation metrics (e.g., accuracy).
        """
        y_pred = self.model.predict(X_test)
        metrics_dict = self.get_metrics(y_test, y_pred)
        
        return metrics_dict
    
    def predict(self, data):
        """
        Predict using the random forest classifier model.

        Args:
        data (array-like): New data samples to predict.

        Returns:
        array-like: Predicted labels.
        """
        return self.model.predict(data)

    def get_metrics(self, y_test, y_pred):
        """
        Calculate and return evaluation metrics based on true labels and predicted labels.

        Args:
        y_test (array-like): True labels from the testing data.
        y_pred (array-like): Predicted labels from the model.

        Returns:
        dict: A dictionary containing evaluation metrics (e.g., accuracy).
        """
        metrics_dict = {}
        metrics_dict['predict'] = y_pred
        
        try:
            metrics_dict['accuracy'] = metrics.accuracy_score(y_test, y_pred)
        except Exception as e:
            print(f"An error occurred while calculating accuracy: {e}")
            metrics_dict['accuracy'] = 50
        
        return metrics_dict