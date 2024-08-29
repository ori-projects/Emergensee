import sys
import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.interfaces.controller import Controller
from app.dal.proxy import Proxy

# Add parent directory to sys.path to ensure relative imports work correctly
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class WidgetsController(Controller):
    """
    Controller class for managing widget-related functionalities through FastAPI.
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

        # Initialize proxy instance for widget database
        proxy_instance = Proxy()
        widgets_db_instance = proxy_instance.widget_db

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

        # Endpoint to get widgets
        @app.get("/get-widgets", tags=["Controller Widgets"], summary="Get Widgets")
        def get_widgets():
            """
            Endpoint to fetch all widgets.

            Returns:
            list: A list of widgets fetched from the widget database.
            """
            try:
                widgets = widgets_db_instance.get_widgets()
                if widgets:
                    return widgets
                else:
                    raise HTTPException(status_code=404, detail="Widgets not found")
            except Exception as e:
                raise HTTPException(status_code=500, detail=f"Error retrieving widgets: {e}")

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