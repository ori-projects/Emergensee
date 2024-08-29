from app.services.utils.utils import Utils
from app.services.utils.datasets_tools import DatasetsTools

class Startup:
    _instance = None

    def __new__(cls):
        """
        Singleton implementation ensuring only one instance of Startup exists.

        Returns:
        Startup: The singleton instance of Startup class.
        """
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        """
        Initializes the Startup instance if not already initialized.

        This method initializes necessary datasets and enums using DatasetsTools and Utils.
        """
        if not self._initialized:
            self._initialized = True
            # Obtain singleton instance of DatasetsTools
            datasets_tools_instance = DatasetsTools.get_instance()
            # Get instances of datasets from DatasetsTools
            datasets_instances = datasets_tools_instance.get_datasets_instances()
            # Preprocess each dataset and set attributes
            for dataset in datasets_instances:
                dataset.preprocess()
                dataset.min_max = datasets_tools_instance.get_min_max_columns(dataset.df_raw)
                dataset.frequencies = datasets_tools_instance.get_categorical_frequencies(dataset.df_raw)
                dataset.process()
            # Set relative weights for datasets
            datasets_tools_instance.set_relative_weights(datasets_instances)
            # Obtain enums using Utils
            enums = Utils.get_enums()