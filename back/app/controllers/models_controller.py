import sys
import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.dal.proxy import Proxy
from app.interfaces.controller import Controller

# Add parent directory to sys.path to ensure relative imports work correctly
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class ModelsController(Controller):
    """
    Controller class for managing models through FastAPI.
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
        models_db_instance = proxy_instance.model_db

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

        # Endpoint to create a model
        @app.post("/create-model", tags=["Controller Models"], summary="Create Model")
        def create_model(name: str, labeled: bool):
            """
            Endpoint to create a new model.

            Args:
            name (str): The name of the model.
            labeled (bool): Whether the model is labeled.

            Returns:
            dict: A dictionary with a message indicating the success of the operation.

            Raises:
            HTTPException: If there is an error creating the model.
            """
            try:
                models_db_instance.create_model(name, labeled)
                return {"message": "Model created successfully"}
            except Exception as e:
                raise HTTPException(status_code=500, detail=f"Error creating model: {e}")

        # Endpoint to get a model by ID
        @app.get("/get-model/{model_id}", tags=["Controller Models"], summary="Get Model by ID")
        def get_model(model_id: int):
            """
            Endpoint to get model details by ID.

            Args:
            model_id (int): The ID of the model to retrieve.

            Returns:
            dict: A dictionary containing the model information if found.

            Raises:
            HTTPException: If the model with the given ID is not found.
            """
            try:
                model = models_db_instance.get_model_by_id(model_id)
                if model:
                    return model
                else:
                    raise HTTPException(status_code=404, detail="Model not found")
            except Exception as e:
                raise HTTPException(status_code=500, detail=f"Error retrieving model: {e}")

        # Endpoint to update a model
        @app.put("/update-model/{model_id}", tags=["Controller Models"], summary="Update Model")
        def update_model(model_id: int, name: str, labeled: bool):
            """
            Endpoint to update model details.

            Args:
            model_id (int): The ID of the model to update.
            name (str): The updated name of the model.
            labeled (bool): Whether the model is labeled.

            Returns:
            dict: A dictionary with a message indicating the success of the operation.

            Raises:
            HTTPException: If there is an error updating the model.
            """
            try:
                models_db_instance.update_model(model_id, name, labeled)
                return {"message": "Model updated successfully"}
            except Exception as e:
                raise HTTPException(status_code=500, detail=f"Error updating model: {e}")

        # Endpoint to delete a model
        @app.delete("/delete-model/{model_id}", tags=["Controller Models"], summary="Delete Model")
        def delete_model(model_id: int):
            """
            Endpoint to delete a model.

            Args:
            model_id (int): The ID of the model to delete.

            Returns:
            dict: A dictionary with a message indicating the success of the operation.

            Raises:
            HTTPException: If there is an error deleting the model.
            """
            try:
                models_db_instance.delete_model(model_id)
                return {"message": "Model deleted successfully"}
            except Exception as e:
                raise HTTPException(status_code=500, detail=f"Error deleting model: {e}")

        # Endpoint to get all models
        @app.get("/get-all-models", tags=["Controller Models"], summary="Get All Models")
        def get_all_models():
            """
            Endpoint to get all models.

            Returns:
            dict: A dictionary containing all models.

            Raises:
            HTTPException: If there is an error retrieving models.
            """
            try:
                models = models_db_instance.get_all_models()
                if models:
                    return models
                else:
                    raise HTTPException(status_code=404, detail="Models not found")
            except Exception as e:
                raise HTTPException(status_code=500, detail=f"Error retrieving models: {e}")

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