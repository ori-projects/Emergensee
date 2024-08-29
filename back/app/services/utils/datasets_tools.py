from collections import Counter
import math
import pandas as pd
from app.entities.datasets.disease import Disease
from app.entities.datasets.ckd import Ckd
from app.entities.datasets.cassi import Cassi
from app.entities.datasets.maternal import Maternal

class DatasetsTools():
    _instance = None

    @staticmethod
    def get_instance():
        """
        Get singleton instance of DatasetsTools.

        Returns:
        DatasetsTools: Singleton instance of DatasetsTools.
        """
        if DatasetsTools._instance is None:
            DatasetsTools._instance = DatasetsTools._initialize_instance()
        return DatasetsTools._instance

    @staticmethod
    def _initialize_instance():
        """
        Initialize the singleton instance with dataset instances.

        Returns:
        DatasetsTools: Initialized instance of DatasetsTools.
        """
        ckd_instance = Ckd()
        disease_instance = Disease()
        cassi_adult_odp_2022_instance = Cassi()
        maternal_health_risk_instance = Maternal()
        instance = DatasetsTools()
        instance._datasets = [ckd_instance, disease_instance, maternal_health_risk_instance, cassi_adult_odp_2022_instance]
        return instance

    def get_datasets_instances(self):
        """
        Get a list of instances of all datasets.

        Returns:
        list: List of dataset instances.
        """
        return self._datasets
    
    def get_min_max_columns(self, df):
        """
        Get minimum and maximum values for numerical columns in a DataFrame.

        Args:
        df (pd.DataFrame): Input DataFrame.

        Returns:
        dict: Dictionary where keys are column names and values are tuples (min_value, max_value).
        """
        min_max_values = {}

        for col in df:
            try:
                min_val = df[col].min()
                max_val = df[col].max()
                min_max_values[col] = (min_val, max_val)
            except:
                continue

        return min_max_values
    
    def get_categorical_frequencies(self, df):
        """
        Get frequency counts for categorical columns in a DataFrame.

        Args:
        df (pd.DataFrame): Input DataFrame.

        Returns:
        dict: Dictionary where keys are column names and values are dictionaries of value counts.
        """
        categorical_cols = df.select_dtypes(include=['object']).columns
        categorical_frequencies = {}

        for col in categorical_cols:
            value_counts = df[col].value_counts().to_dict()
            categorical_frequencies[col] = value_counts

        return categorical_frequencies

    def get_categorical_enums(self, dataset):
        """
        Get unique categorical values for each categorical column in a dataset.

        Args:
        dataset: Instance of a dataset class (e.g., Ckd, Disease, Cassi, Maternal).

        Returns:
        dict: Dictionary where keys are column names and values are sets of unique categorical values.
        """
        categorical_info = {}

        for _, data_row in dataset.df_raw.iterrows():
            data_row_dict = data_row.to_dict()

            for key, value in data_row_dict.items():
                if pd.api.types.is_string_dtype(dataset.df_raw[key]):
                    if key not in categorical_info:
                        categorical_info[key] = set([value])
                    else:
                        categorical_info[key].add(value)
        return categorical_info

    def mix_distance(self, dataset_row, input_row_dict, min_max, frequencies):
        """
        Calculate mixed distance between a dataset row and an input row.

        Args:
        dataset_row (dict): Dictionary representing a row from a dataset.
        input_row_dict (dict): Dictionary representing an input row.
        min_max (dict): Dictionary of minimum and maximum values for numerical columns.
        frequencies (dict): Dictionary of categorical frequencies.

        Returns:
        float: Mixed distance between the dataset row and the input row.
        """
        numerical_sum = 0
        categorical_sum = 0
        
        for key, value in dataset_row.items():

            if key not in input_row_dict or value is None or input_row_dict[key] is None:
                continue

            input_value = input_row_dict[key]
            
            try:
                value = float(value)
                input_value = float(input_value)
                min_val, max_val = min_max.get(key, (None, None))

                if min_val is None or max_val is None:
                    continue

                numerical_sum += ((value - input_value) / (max_val - min_val)) ** 2

            except:
                if value == input_value:
                    categorical_sum += 0

                else:
                    input_freq = frequencies[key].get(input_value, 0)
                    freq_array = [freq_value for freq_value in frequencies[key].values() if freq_value != input_freq]
                    max_freq = max(input_freq, max(freq_array))
                    min_freq = min(input_freq, min(freq_array))
                    categorical_sum += (abs(input_freq - max_freq) + min_freq) / max(max_freq, input_freq)
        
        return math.sqrt(numerical_sum + categorical_sum)

    def find_nearest_rows(self, dataset, input_row_dict, K):
        """
        Find K nearest rows in a dataset to an input row.

        Args:
        dataset: Instance of a dataset class (e.g., Ckd, Disease, Cassi, Maternal).
        input_row_dict (dict): Dictionary representing an input row.
        K (int): Number of nearest rows to find.

        Returns:
        list: List of dictionaries representing K nearest rows.
        """
        nearest_rows = []
        distances = []
    
        for _, data_row in dataset.df_raw.iterrows():
            data_row_dict = data_row.to_dict()
            distance = self.mix_distance(data_row_dict, input_row_dict, dataset.min_max, dataset.frequencies)
    
            nearest_rows.append(data_row_dict)
            distances.append(distance)
    
        nearest_rows_sorted = [row for _, row in sorted(zip(distances, nearest_rows), key=lambda pair: pair[0])]
        return self.get_nearest_row(nearest_rows_sorted[:K])

    def get_nearest_row(self, nearest_rows):
        """
        Get the nearest row in terms of mode for each column from a list of rows.

        Args:
        nearest_rows (list): List of dictionaries representing rows.

        Returns:
        dict: Dictionary representing the nearest row in terms of mode for each column.
        """
        if not nearest_rows:
            return {} 

        mode_dict = {}

        for key in nearest_rows[0]:
            if isinstance(nearest_rows[0][key], (int, float)):
                mean_value = sum(d[key] for d in nearest_rows) / len(nearest_rows)
                mode_dict[key] = mean_value
            else:
                mode_value = self.calculate_mode([d[key] for d in nearest_rows])
                mode_dict[key] = mode_value

        return mode_dict

    def calculate_mode(self, values):
        """
        Calculate the mode of a list of values.

        Args:
        values (list): List of values.

        Returns:
        int or float or str: Mode value.
        """
        value_counts = Counter(values)
        mode_value = value_counts.most_common(1)[0][0]
        return mode_value

    def set_relative_weights(self, datasets):
        """
        Set relative weights for datasets based on their number of rows.

        Args:
        datasets (list): List of dataset instances.
        """
        total_datasets_rows = 0
        for dataset in datasets:
            total_datasets_rows += dataset.rows

        for dataset in datasets:
            dataset.risk_weight = dataset.rows / total_datasets_rows