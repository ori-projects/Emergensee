from app.interfaces.unlabeled.unlabeled_processor import UnLabeledProcessor

class CassiProcessor(UnLabeledProcessor):
    def train_models(self, models, X_train, y_train):
        """
        Train models using the provided training data.

        Args:
        models (list): List of model instances.
        X_train (array-like): Training data features.
        y_train (array-like): Training data labels.

        Returns:
        None
        """
        for model in models:
            model.train(X_train, y_train)

    def test_models(self, models, X_test, y_test):
        """
        Test models using the provided testing data.

        Args:
        models (list): List of model instances.
        X_test (array-like): Testing data features.
        y_test (array-like): Testing data labels.

        Returns:
        dict: Dictionary containing model names as keys and their corresponding metrics as values.
        """
        results = {}

        for model in models:
            metrics = model.test(X_test, y_test)
            results[type(model).__name__] = metrics

        return results
    
    def predict_models(self, models, cassi_row):
        """
        Predict risk levels using the trained models for a given row of data.

        Args:
        models (list): List of model instances.
        cassi_row (array-like): Row of data to predict.

        Returns:
        dict: Dictionary containing model names as keys and their predicted risk levels as values.
        """
        results = {}
        for model in models:
            prediction = model.predict(cassi_row)
            cluster_value = model.cluster_risk_levels[prediction[0]]
            prediction = [self.get_risk_level_value(cluster_value)]
            results[type(model).__name__] = prediction

        return results
    
    def get_risk_level_value(self, risk_level):
        """
        Map cluster risk levels to numeric risk values.

        Args:
        risk_level (str): Cluster risk level.

        Returns:
        int: Numeric risk value.
        """
        if risk_level == 'SIR_Low':
            return 0
        elif risk_level == 'SIR_Mid':
            return 50
        else:
            return 100