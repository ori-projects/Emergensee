class Endpoint:
    """
    Class to define endpoint configuration.
    """
    host = "127.0.0.1"
    port = 8001

    @classmethod
    def get_host(cls):
        """
        Method to retrieve the host address.

        Returns:
        str: The host address.
        """
        return cls.host

    @classmethod
    def get_port(cls):
        """
        Method to retrieve the port number.

        Returns:
        int: The port number.
        """
        return cls.port

    @classmethod
    def get_endpoint(cls):
        """
        Method to retrieve the full endpoint URL.

        Returns:
        str: The full endpoint URL.
        """
        return f"http://{cls.host}:{cls.port}"