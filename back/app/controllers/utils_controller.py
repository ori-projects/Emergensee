import sys
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from app.services.utils.utils import Utils
from app.interfaces.controller import Controller

# Add parent directory to sys.path to ensure relative imports work correctly
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class UtilsController(Controller):
    """
    Controller class for managing utility-related functionalities through FastAPI.
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

        # Endpoint to get all enums
        @app.get("/get-enums", tags=["Controller Utils"], summary="Get all enums")
        def get_enums_controller():
            """
            Endpoint to fetch all enums.

            Returns:
            JSONResponse: A JSON response containing selected enums.
            """
            enums = Utils.get_enums()

            selected_enums = {
                "Operative_Procedure": [],
                "Feelings_and_Urge": [],
                "Disease": [],
                "Critical_Feelings": []
            }

            # Extract and organize selected enums
            for enum in enums:
                if "Operative_Procedure" in enum:
                    selected_enums["Operative_Procedure"].extend(enum["Operative_Procedure"])
                if "Feelings_and_Urge" in enum:
                    selected_enums["Feelings_and_Urge"].extend(enum["Feelings_and_Urge"])
                if "Disease" in enum:
                    selected_enums["Disease"].extend(enum["Disease"])
                if "Critical_Feelings" in enum:
                    selected_enums["Critical_Feelings"].extend(enum["Critical_Feelings"])
                    
            return JSONResponse(content={"enums": selected_enums})

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