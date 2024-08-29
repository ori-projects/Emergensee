from app.services.utils.datasets_tools import DatasetsTools

class Utils:
    _instance = None
    _cached_enums = None

    def __new__(cls, *args, **kwargs):
        """
        Singleton instance creation for Utils class.

        Returns:
        Utils: The singleton instance of Utils.
        """
        if not cls._instance:
            cls._instance = super(Utils, cls).__new__(cls, *args, **kwargs)
        return cls._instance
    
    @classmethod
    def get_instance(cls):
        """
        Retrieve the singleton instance of Utils class.

        Returns:
        Utils: The singleton instance of Utils.
        """
        if not cls._instance:
            cls._instance = cls()
        return cls._instance
    
    @classmethod
    def get_enums(cls):
        """
        Retrieve enums from datasets using DatasetsTools.

        Returns:
        list: List of enums retrieved from datasets.
        """
        if cls._cached_enums:
            return cls._cached_enums
        
        dataset_tools_instance = DatasetsTools.get_instance()
        datasets_instances = dataset_tools_instance.get_datasets_instances()
        enums_list = []

        for dataset in datasets_instances:
            enums = dataset_tools_instance.get_categorical_enums(dataset)
            if enums:
                enums_list.append(enums)
        
        cls._cached_enums = enums_list
        return enums_list