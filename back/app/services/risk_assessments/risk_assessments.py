import math
import numpy as np
from collections import OrderedDict
from app.entities.configs.error_messages import ErrorMessages

class RiskAssessments:
    @staticmethod
    def calculate_risk_assessment(predictions, weights):
        """
        Calculate the risk assessment based on predictions and weights.

        Args:
        predictions (dict): Dictionary containing predictions from different datasets.
                           Keys are dataset names, values are dictionaries mapping model names to predictions.
        weights (list): List of weights corresponding to each dataset.

        Returns:
        OrderedDict: Ordered dictionary containing dataset names and their mean scores,
                     including the final weighted assessment.
        """
        mean_scores = OrderedDict()
        dataset_scores = []

        # Calculate mean scores for each dataset
        for i, (dataset, models) in enumerate(predictions.items()):
            scores = []

            for _, prediction in models.items():
                scores.append(np.mean(prediction))
                
            # Handle case where no scores are available
            if not scores:
                mean_scores[dataset] = ErrorMessages.empty_percentage_list
                continue

            # Remove NaN values from scores
            scores = [score for score in scores if not math.isnan(score)]
            
            if scores:
                total_score = sum(scores)
                num_scores = len(scores)
                average_score = (total_score / num_scores)
                mean_scores[dataset] = f'{average_score:.2f}%'
                dataset_scores.append((average_score, weights[i]))

        # Calculate the final weighted assessment
        if dataset_scores:
            total_weight = sum(weight for _, weight in dataset_scores)
            weighted_sum = sum(score * weight for score, weight in dataset_scores)
            final_assessment = weighted_sum / total_weight
        else:
            final_assessment = 0

        # Add final assessment to the ordered dictionary
        mean_scores["Final Assessment"] = f'{final_assessment:.2f}%'
        mean_scores.move_to_end("Final Assessment", last=False)

        return mean_scores