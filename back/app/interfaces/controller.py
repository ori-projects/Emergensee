from abc import ABC, abstractmethod

class Controller(ABC):
    """
    Abstract base class for defining controller interfaces.
    """

    @abstractmethod
    def health_check(self):
        """
        Abstract method to perform a health check.

        This method should be implemented to verify the health status of the controller or the system it manages.

        Returns:
        bool: True if the health check is successful, False otherwise.
        """
        pass