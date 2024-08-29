from sklearn import metrics
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier
from app.interfaces.labeled.labeled_model import LabeledModel

class DecisionTreeModel(LabeledModel):
    """
    Implementation of a decision tree model (DecisionTreeModel).
    """

    def __init__(self, max_depth=15, min_samples_split=10, min_samples_leaf=5):
        """
        Initialize a DecisionTree instance.

        Args:
        max_depth (int, optional): Maximum depth of the decision tree. Defaults to 15.
        min_samples_split (int, optional): Minimum number of samples required to split an internal node. Defaults to 10.
        min_samples_leaf (int, optional): Minimum number of samples required to be at a leaf node. Defaults to 5.
        """
        self.model = DecisionTreeClassifier(max_depth=max_depth, min_samples_split=min_samples_split, min_samples_leaf=min_samples_leaf)

    def train(self, X_train, y_train):
        """
        Train the decision tree model.

        Args:
        X_train (array-like): Training data features.
        y_train (array-like): Training data labels.
        """
        self.model.fit(X_train, y_train)

    def test(self, X_test, y_test):
        """
        Test the decision tree model and return evaluation metrics.

        Args:
        X_test (array-like): Testing data features.
        y_test (array-like): Testing data labels.

        Returns:
        dict: A dictionary containing evaluation metrics (e.g., accuracy).
        """
        y_pred = self.model.predict(X_test)
        metrics_dict = self.get_metrics(y_test, y_pred)

        return metrics_dict
    
    def predict(self, X_predict):
        """
        Predict labels for new data using the trained model.

        Args:
        X_predict (array-like): New data features to predict labels for.

        Returns:
        array-like: Predicted labels.
        """
        return self.model.predict(X_predict)

    def get_metrics(self, y_test, y_pred):
        """
        Calculate and return evaluation metrics based on y_test and y_pred.

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