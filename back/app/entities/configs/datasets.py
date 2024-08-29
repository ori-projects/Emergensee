class Datasets:
    """
    Class to define paths to various datasets.
    """

    raw_ckd = r'app\\datasets\\raw\\ckd.csv'
    raw_disease = r'app\\datasets\\raw\\disease.csv'
    raw_cassi = r'app\\datasets\\raw\\ca_ssi_adult_odp_2022.csv'
    raw_maternal = r'app\\datasets\\raw\\maternal_health_risk.csv'

    ckd = r'app\\datasets\\clean\\ckd.csv'
    disease = r'app\\datasets\\clean\\disease.csv'
    cassi = r'app\\datasets\\clean\\ca_ssi_adult_odp_2022.csv'
    maternal = r'app\\datasets\\clean\\maternal_health_risk.csv'

    ckd_train = 'ckd'
    disease_train = 'Critical'
    cassi_train = 'SIR'
    maternal_train = 'RiskLevel'

    @classmethod
    def get_raw_dataset(cls, dataset_name):
        """
        Method to retrieve the path of a raw dataset based on its name.

        Args:
        dataset_name (str): The name of the raw dataset.

        Returns:
        str: The path to the raw dataset.
        """
        return getattr(cls, f'raw_{dataset_name.lower()}')

    @classmethod
    def get_clean_dataset(cls, dataset_name):
        """
        Method to retrieve the path of a clean dataset based on its name.

        Args:
        dataset_name (str): The name of the clean dataset.

        Returns:
        str: The path to the clean dataset.
        """
        return getattr(cls, dataset_name.lower())

    @classmethod
    def get_train_label(cls, dataset_name):
        """
        Method to retrieve the training label for a dataset.

        Args:
        dataset_name (str): The name of the dataset.

        Returns:
        str: The training label for the dataset.
        """
        return getattr(cls, f'{dataset_name.lower()}_train')