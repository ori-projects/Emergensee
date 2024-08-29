from app.interfaces.labeled.labeled_processor import LabeledProcessor

class DiseaseProcessor(LabeledProcessor):
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
    
    def predict_models(self, models, disease_row):
        """
        Predict risk levels using the trained models for a given row of Disease data.

        Args:
        models (list): List of model instances.
        disease_row (array-like): Row of data to predict.

        Returns:
        dict: Dictionary containing model names as keys and their predicted risk levels as values.
        """
        results = {}

        for model in models:
            metrics = model.predict(disease_row)

            abs_metrics = abs(metrics[0]) * 100
            if abs_metrics >= 50:
                abs_metrics = [100]
            else:
                abs_metrics = [0]

            results[type(model).__name__] = abs_metrics

        return results