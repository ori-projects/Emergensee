from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.dal.proxy import Proxy
from app.interfaces.controller import Controller

class AlgorithmsController(Controller):
    """
    Controller class for managing algorithms through FastAPI.
    """

    _instance = None

    @classmethod
    def get_app(cls):
        """
        Singleton method to get or create an instance of the FastAPI application.

        Returns:
        FastAPI: An instance of the FastAPI application.
        """
        if cls._instance is None:
            cls._instance = cls._create_instance()
        return cls._instance

    @classmethod
    def _create_instance(cls):
        """
        Private method to create a new instance of the FastAPI application.

        Returns:
        FastAPI: A new instance of the FastAPI application.
        """
        app = FastAPI(debug=True)

        # Initialize Proxy and access necessary databases
        proxy_instance = Proxy()
        algorithm_db_instance = proxy_instance.algorithm_db

        # Configure CORS middleware for cross-origin requests
        app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],  # Replace "*" with your specific origins if needed
            allow_credentials=True,
            allow_methods=["GET", "POST", "PUT", "DELETE"],
            allow_headers=["Content-Type", "Authorization"],
        )

        # Endpoint to create a new algorithm
        @app.post("/create-algorithm", tags=["Controller Algorithms"], summary="Create Algorithm")
        def create_algorithm(algorithm_name: str, success_rank: int, num_uses: int):
            """
            Create a new algorithm.

            Args:
            algorithm_name (str): The name of the algorithm.
            success_rank (int): The success rank of the algorithm.
            num_uses (int): The number of times the algorithm has been used.

            Returns:
            dict: A message indicating success or failure.
            
            Raises:
            HTTPException: If there's an error creating the algorithm (status code 500).
            """
            try:
                algorithm_db_instance.create_algorithm(algorithm_name, success_rank, num_uses)
                return {"message": "Algorithm created successfully"}
            except Exception as e:
                raise HTTPException(status_code=500, detail=f"Error creating algorithm: {e}")

        # Endpoint to get all algorithms
        @app.get("/get-algorithms", tags=["Controller Algorithms"], summary="Get All Algorithms")
        def get_algorithms():
            """
            Get all algorithms.

            Returns:
            list: A list of all algorithms.
            
            Raises:
            HTTPException: If algorithms are not found (status code 404) or if there's an error retrieving algorithms (status code 500).
            """
            try:
                algorithms = algorithm_db_instance.get_algorithms()
                if algorithms:
                    return algorithms
                else:
                    raise HTTPException(status_code=404, detail="Algorithms not found")
            except Exception as e:
                raise HTTPException(status_code=500, detail=f"Error retrieving algorithms: {e}")

        # Endpoint to get an algorithm by ID
        @app.get("/get-algorithm/{algorithm_id}", tags=["Controller Algorithms"], summary="Get Algorithm by ID")
        def get_algorithm_by_id(algorithm_id: int):
            """
            Get an algorithm by ID.

            Args:
            algorithm_id (int): The ID of the algorithm to retrieve.

            Returns:
            dict: Details of the algorithm.
            
            Raises:
            HTTPException: If algorithm is not found (status code 404) or if there's an error retrieving algorithm (status code 500).
            """
            try:
                algorithm = algorithm_db_instance.get_algorithm_by_id(algorithm_id)
                if algorithm:
                    return algorithm
                else:
                    raise HTTPException(status_code=404, detail="Algorithm not found")
            except Exception as e:
                raise HTTPException(status_code=500, detail=f"Error retrieving algorithm: {e}")

        # Endpoint to update an algorithm
        @app.put("/update-algorithm/{algorithm_id}", tags=["Controller Algorithms"], summary="Update Algorithm")
        def update_algorithm(algorithm_id: int, algorithm_name: str, success_rank: int, num_uses: int):
            """
            Update an existing algorithm.

            Args:
            algorithm_id (int): The ID of the algorithm to update.
            algorithm_name (str): The updated name of the algorithm.
            success_rank (int): The updated success rank of the algorithm.
            num_uses (int): The updated number of times the algorithm has been used.

            Returns:
            dict: A message indicating success or failure.
            
            Raises:
            HTTPException: If there's an error updating the algorithm (status code 500).
            """
            try:
                algorithm_db_instance.update_algorithm(algorithm_id, algorithm_name, success_rank, num_uses)
                return {"message": "Algorithm updated successfully"}
            except Exception as e:
                raise HTTPException(status_code=500, detail=f"Error updating algorithm: {e}")

        # Endpoint to delete an algorithm
        @app.delete("/delete-algorithm/{algorithm_id}", tags=["Controller Algorithms"], summary="Delete Algorithm")
        def delete_algorithm(algorithm_id: int):
            """
            Delete an algorithm.

            Args:
            algorithm_id (int): The ID of the algorithm to delete.

            Returns:
            dict: A message indicating success or failure.
            
            Raises:
            HTTPException: If there's an error deleting the algorithm (status code 500).
            """
            try:
                algorithm_db_instance.delete_algorithm(algorithm_id)
                return {"message": "Algorithm deleted successfully"}
            except Exception as e:
                raise HTTPException(status_code=500, detail=f"Error deleting algorithm: {e}")

        # Endpoint to get statistics related to algorithms
        @app.get("/get-algorithm-statistics", tags=["Controller Algorithms"], summary="Get Algorithm Statistics")
        def get_algorithm_statistics():
            """
            Get statistics related to algorithms.

            Returns:
            dict: Statistics related to algorithms.
            
            Raises:
            HTTPException: If algorithm statistics are not found (status code 404) or if there's an error retrieving algorithm statistics (status code 500).
            """
            try:
                statistics = algorithm_db_instance.get_statistics()
                if statistics:
                    return statistics
                else:
                    raise HTTPException(status_code=404, detail="Algorithm statistics not found")
            except Exception as e:
                raise HTTPException(status_code=500, detail=f"Error retrieving algorithm statistics: {e}")

        # Endpoint for health check
        @app.get("/health", tags=["Health Check"], summary="Health Check")
        def health_check():
            """
            Health check endpoint to verify the service is running.

            Returns:
            dict: A dictionary indicating the health status of the service.
            """
            return {"status": "ok", "message": "Service is up and running"}

        return app