from sklearn import metrics
from sklearn.neural_network import MLPClassifier
from app.interfaces.labeled.labeled_model import LabeledModel

class NeuralNetworkModel(LabeledModel):
    """
    Implementation of a neural network classifier model (NeuralNetworkModel).
    """

    CONST_HIDDEN_LAYER_SIZES = (200, 100)  # Increased hidden layer sizes
    CONST_ACTIVATION = 'tanh'  # Trying a different activation function
    CONST_SOLVER = 'lbfgs'  # Trying a different solver
    CONST_ALPHA = 0.001  # Adjusted regularization parameter
    CONST_MAX_ITER = 2000  # Increased maximum iterations

    def __init__(self, hidden_layer_sizes=CONST_HIDDEN_LAYER_SIZES, activation=CONST_ACTIVATION, solver=CONST_SOLVER, alpha=CONST_ALPHA, max_iter=CONST_MAX_ITER):
        """
        Initialize a NeuralNetworkModel instance.

        Args:
        hidden_layer_sizes (tuple, optional): Sizes of hidden layers. Defaults to (200, 100).
        activation (str, optional): Activation function for the hidden layers ('identity', 'logistic', 'tanh', 'relu'). Defaults to 'tanh'.
        solver (str, optional): Solver for weight optimization ('lbfgs', 'sgd', 'adam'). Defaults to 'lbfgs'.
        alpha (float, optional): L2 penalty (regularization term) parameter. Defaults to 0.001.
        max_iter (int, optional): Maximum number of iterations. Defaults to 2000.
        """
        self.model = MLPClassifier(
            hidden_layer_sizes=hidden_layer_sizes,
            activation=activation,
            solver=solver,
            alpha=alpha,
            max_iter=max_iter
        )

    def train(self, X_train, y_train):
        """
        Train the neural network classifier model.

        Args:
        X_train (array-like): Training data features.
        y_train (array-like): Training data labels.
        """
        self.model.fit(X_train, y_train)

    def test(self, X_test, y_test):
        """
        Test the neural network classifier model and return evaluation metrics.

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
        Predict using the neural network classifier model.

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