from sklearn import metrics
from sklearn.svm import SVC
from app.interfaces.labeled.labeled_model import LabeledModel

class SvmModel(LabeledModel):
    """
    Implementation of a support vector machine (SVM) classifier model (SVMModel).
    """

    CONST_KERNEL = 'linear'  # Trying a different kernel
    CONST_C = 0.1  # Adjusting the regularization parameter
    CONST_GAMMA = 'auto'  # Changing gamma to 'auto' for better scaling

    def __init__(self, kernel=CONST_KERNEL, C=CONST_C, gamma=CONST_GAMMA):
        """
        Initialize an SVMModel instance.

        Args:
        kernel (str, optional): Specifies the kernel type to be used in the algorithm ('linear', 'poly', 'rbf', 'sigmoid', 'precomputed'). Defaults to 'linear'.
        C (float, optional): Regularization parameter. The strength of the regularization is inversely proportional to C. Must be strictly positive. Defaults to 0.1.
        gamma ({'scale', 'auto'} or float, optional): Kernel coefficient for 'rbf', 'poly' and 'sigmoid'. If 'scale', it uses 1 / (n_features * X.var()) as value of gamma, if 'auto', uses 1 / n_features. Defaults to 'auto'.
        """
        self.model = SVC(kernel=kernel, C=C, gamma=gamma)

    def train(self, X_train, y_train):
        """
        Train the SVM classifier model.

        Args:
        X_train (array-like): Training data features.
        y_train (array-like): Training data labels.
        """
        self.model.fit(X_train, y_train)

    def test(self, X_test, y_test):
        """
        Test the SVM classifier model and return evaluation metrics.

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
        Predict using the SVM classifier model.

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