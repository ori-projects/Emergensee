from sklearn import metrics
from sklearn.linear_model import LinearRegression
from app.interfaces.labeled.labeled_model import LabeledModel

class LinearRegressionModel(LabeledModel):
    """
    Implementation of a linear regression model that handles missing values encoded as NaN natively.
    """

    def __init__(self):
        """
        Initialize a LinearRegressionModel instance.
        """
        self.model = LinearRegression()

    def train(self, X_train, y_train):
        """
        Train the linear regression model.

        Args:
        X_train (array-like): Training data features.
        y_train (array-like): Training data labels.
        """
        self.model.fit(X_train, y_train)

    def test(self, X_test, y_test):
        """
        Test the linear regression model and return evaluation metrics.

        Args:
        X_test (array-like): Testing data features.
        y_test (array-like): Testing data labels.

        Returns:
        dict: A dictionary containing evaluation metrics (e.g., mean absolute error, mean squared error, R^2 score).
        """
        y_prediction = self.model.predict(X_test)
        metrics_dict = self.get_metrics(y_test, y_prediction)
        
        return metrics_dict

    def predict(self, data):
        """
        Predict using the linear regression model.

        Args:
        data (array-like): New data samples to predict.

        Returns:
        array-like: Predicted values.
        """
        return self.model.predict(data)

    def get_metrics(self, y_test, y_pred):
        """
        Calculate and return evaluation metrics based on true labels and predicted labels.

        Args:
        y_test (array-like): True labels from the testing data.
        y_pred (array-like): Predicted labels from the model.

        Returns:
        dict: A dictionary containing evaluation metrics (e.g., mean absolute error, mean squared error, R^2 score).
        """
        metrics_dict = {}
        metrics_dict['predict'] = y_pred
        metrics_dict['mean_absolute_error'] = metrics.mean_absolute_error(y_test, y_pred)
        metrics_dict['mean_squared_error'] = metrics.mean_squared_error(y_test, y_pred)
        metrics_dict['r2_score'] = metrics.r2_score(y_test, y_pred)
        
        return metrics_dict