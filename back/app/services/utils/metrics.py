class Metrics:
    def calculate_percentage(prediction):
        """
        Calculates percentages based on prediction values.

        Args:
        prediction (list): List of prediction values.

        Returns:
        list: List of percentages corresponding to each prediction value.
        """
        percentages = []
        for pred in prediction:
            if pred >= 1:
                percentages.append(100)
            elif pred < 0:  # -1 predict didn't succeed (happens in Gaussian once in a while) We can log it as well
                continue  # Skip negative predictions
            else:
                percentages.append(pred * 100)
        return percentages