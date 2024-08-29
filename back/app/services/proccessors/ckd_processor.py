from app.interfaces.labeled.labeled_processor import LabeledProcessor

class CkdProcessor(LabeledProcessor):
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
    
    def predict_models(self, models, ckd_row):
        """
        Predict risk levels using the trained models for a given row of CKD data.

        Args:
        models (list): List of model instances.
        ckd_row (array-like): Row of data to predict.

        Returns:
        dict: Dictionary containing model names as keys and their predicted risk levels as values.
        """
        results = {}

        for model in models:
            metrics = model.predict(ckd_row)

            abs_metrics = abs(metrics[0]) * 100
            if abs_metrics >= 75:
                abs_metrics = [100]
            else:
                abs_metrics = [0]

            results[type(model).__name__] = abs_metrics

        return results