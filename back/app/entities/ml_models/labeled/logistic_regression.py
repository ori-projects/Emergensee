from sklearn import metrics
from sklearn.linear_model import LogisticRegression
from app.interfaces.labeled.labeled_model import LabeledModel

class LogisticRegressionModel(LabeledModel):
    """
    Implementation of a logistic regression classifier model (LogisticRegressionModel).
    """
    CONST_PENALTY = 'l2'
    CONST_C = 0.1  # Adjusted C value for better regularization
    CONST_SOLVER = 'sag'  # Changed solver for better performance with large datasets
    CONST_MAX_ITERATION = 5000  # Increased max iterations for better convergence

    def __init__(self, penalty=CONST_PENALTY, C=CONST_C, solver=CONST_SOLVER, max_iter=CONST_MAX_ITERATION):
        """
        Initialize a LogisticRegressionModel instance.

        Args:
        penalty (str, optional): Penalty term for regularization ('l1' or 'l2'). Defaults to 'l2'.
        C (float, optional): Inverse of regularization strength; smaller values specify stronger regularization. Defaults to 0.1.
        solver (str, optional): Algorithm to use in the optimization problem ('newton-cg', 'lbfgs', 'liblinear', 'sag', 'saga'). Defaults to 'sag'.
        max_iter (int, optional): Maximum number of iterations taken for the solvers to converge. Defaults to 5000.
        """
        self.model = LogisticRegression(penalty=penalty, C=C, solver=solver, max_iter=max_iter)

    def train(self, X_train, y_train):
        """
        Train the logistic regression classifier model.

        Args:
        X_train (array-like): Training data features.
        y_train (array-like): Training data labels.
        """
        self.model.fit(X_train, y_train)

    def test(self, X_test, y_test):
        """
        Test the logistic regression classifier model and return evaluation metrics.

        Args:
        X_test (array-like): Testing data features.
        y_test (array-like): Testing data labels.

        Returns:
        dict: A dictionary containing evaluation metrics (e.g., accuracy).
        """
        y_prediction = self.model.predict(X_test)
        metrics_dict = self.get_metrics(y_test, y_prediction)
        
        return metrics_dict
    
    def predict(self, data):
        """
        Predict using the logistic regression classifier model.

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