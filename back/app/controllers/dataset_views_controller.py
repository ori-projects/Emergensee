import sys
import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.dal.proxy import Proxy
from app.entities.datasets.cassi import Cassi
from app.entities.datasets.ckd import Ckd
from app.entities.datasets.disease import Disease
from app.entities.datasets.maternal import Maternal
from app.interfaces.controller import Controller

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class DatasetViewsController(Controller):
    """
    Controller class for managing dataset views through FastAPI.
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

        proxy_instance = Proxy()
        ds_db_instance = proxy_instance.dataset_db

        # Configure CORS middleware for cross-origin requests
        app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],  # Replace "*" with your specific origins if needed
            allow_credentials=True,
            allow_methods=["GET", "POST", "PUT", "DELETE"],
            allow_headers=["Content-Type", "Authorization"],
        )

        # Summary explaining the controllers
        """
        This FastAPI application provides endpoints for various functionalities including account management, dataset management, preprocessing, model training, and patient risk assessment. Each controller is categorized based on its functionality.
        """

        # Endpoint to create a dataset
        @app.post("/create-dataset", tags=["Controller Datasets"], summary="Create Dataset")
        async def create_dataset(name: str, description: str):
            """
            Endpoint to create a new dataset.

            Args:
            name (str): The name of the dataset.
            description (str): The description of the dataset.

            Returns:
            dict: A dictionary with a message indicating the success of the operation.
            """
            try:
                ds_db_instance.create_dataset(name, description)
                return {"message": "Dataset created successfully"}
            except Exception as e:
                raise HTTPException(status_code=500, detail=f"Error creating dataset: {e}")

        # Endpoint to get a dataset by ID
        @app.get("/get-dataset/{dataset_id}", tags=["Controller Datasets"], summary="Get Dataset by ID")
        async def get_dataset(dataset_id: int):
            """
            Endpoint to get a dataset by its ID.

            Args:
            dataset_id (int): The ID of the dataset to retrieve.

            Returns:
            dict: A dictionary containing the dataset information if found.

            Raises:
            HTTPException: If the dataset with the given ID is not found.
            """
            try:
                dataset = ds_db_instance.get_dataset_by_id(dataset_id)
                if dataset:
                    return dataset
                else:
                    raise HTTPException(status_code=404, detail="Dataset not found")
            except Exception as e:
                raise HTTPException(status_code=500, detail=f"Error retrieving dataset: {e}")

        # Endpoint to update a dataset description
        @app.put("/update-dataset-description/{dataset_id}", tags=["Controller Datasets"], summary="Update Dataset Description")
        async def update_dataset_description(dataset_id: int, new_description: str):
            """
            Endpoint to update the description of a dataset.

            Args:
            dataset_id (int): The ID of the dataset to update.
            new_description (str): The new description for the dataset.

            Returns:
            dict: A dictionary with a message indicating the success of the operation.

            Raises:
            HTTPException: If there is an error updating the dataset description.
            """
            try:
                ds_db_instance.update_dataset_description(dataset_id, new_description)
                return {"message": "Dataset description updated successfully"}
            except Exception as e:
                raise HTTPException(status_code=500, detail=f"Error updating dataset description: {e}")

        # Endpoint to delete a dataset
        @app.delete("/delete-dataset/{dataset_id}", tags=["Controller Datasets"], summary="Delete Dataset")
        async def delete_dataset(dataset_id: int):
            """
            Endpoint to delete a dataset.

            Args:
            dataset_id (int): The ID of the dataset to delete.

            Returns:
            dict: A dictionary with a message indicating the success of the operation.

            Raises:
            HTTPException: If there is an error deleting the dataset.
            """
            try:
                ds_db_instance.delete_dataset(dataset_id)
                return {"message": "Dataset deleted successfully"}
            except Exception as e:
                raise HTTPException(status_code=500, detail=f"Error deleting dataset: {e}")
            
        # Endpoint for health check
        @app.get("/get-datasets", tags=["Get Datasets"], summary="Get Datasets Information")
        def get_datasets():
            disease = Disease()
            ckd = Ckd()
            cassi = Cassi()
            maternal = Maternal()

            datasets = {
                        'disease' : disease.get_dataset_info(),
                        'ckd' : ckd.get_dataset_info(),
                        'cassi' : cassi.get_dataset_info(),
                        'maternal' : maternal.get_dataset_info()
                        }

            return {"datasets": datasets}

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