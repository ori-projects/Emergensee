from app.dal.proxys.account_proxy import AccountProxy
from app.dal.proxys.algorithm_proxy import AlgorithmProxy
from app.dal.proxys.dataset_proxy import DatasetProxy
from app.dal.proxys.model_proxy import ModelProxy
from app.dal.proxys.widget_proxy import WidgetProxy

class Proxy:
    """
    Singleton class representing a proxy for accessing various data entities using different proxies.
    """

    _instance = None

    def __new__(cls):
        """
        Overrides the __new__ method to ensure Proxy class is a singleton.

        Returns:
        Proxy: The singleton instance of Proxy class.
        """
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.dataset_db = DatasetProxy()
            cls._instance.account_db = AccountProxy()
            cls._instance.algorithm_db = AlgorithmProxy()
            cls._instance.model_db = ModelProxy()
            cls._instance.widget_db = WidgetProxy()
        return cls._instance