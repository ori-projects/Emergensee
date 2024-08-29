import sys
import os
from fastapi.responses import JSONResponse
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.services.utils.mapper import Mapper
from app.entities.requests.risk_assessment_request import RiskAssessmentRequest
from app.services.dataset_ops.dataset_operation_service import DatasetOperationService
from app.interfaces.controller import Controller

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class DatasetPperationsController(Controller):
    """
    Controller class for managing dataset operations through FastAPI.
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
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["GET", "POST", "PUT", "DELETE"],
            allow_headers=["Content-Type", "Authorization"],
        )

        # Endpoint to preprocess all datasets
        @app.post("/preprocess_datasets", tags=["Controller DatasetOps"], summary="Preprocess all datasets")
        def preprocess_datasets_controller():
            """
            Endpoint to preprocess all datasets.

            Returns:
            JSONResponse: A JSON response with a message indicating the result of the preprocessing.
            """
            message = DatasetOperationService.preprocess_datasets()
            return JSONResponse(content={"message": message})

        # Endpoint to process all datasets
        @app.post("/process_datasets", tags=["Controller DatasetOps"], summary="Process all datasets")
        def process_datasets_controller():
            """
            Endpoint to process all datasets.

            Returns:
            JSONResponse: A JSON response with a message indicating the result of the processing.
            """
            message = DatasetOperationService.process_datasets()
            return JSONResponse(content={"message": message})

        # Endpoint to get risk assessment
        @app.post("/get-risk-assessment", tags=["Controller DatasetOps"], summary="Get risk assessment")
        def get_risk_assessment_controller(data: RiskAssessmentRequest):
            """
            Endpoint to get risk assessment.

            Args:
            data (RiskAssessmentRequest): The risk assessment request data.

            Returns:
            JSONResponse: A JSON response with details of the risk assessment calculations.
            """
            request = Mapper().map_to_risk_assessment_request(data)

            result = DatasetOperationService.get_risk_assessment(request)

            message = ""

            for key, value in result.items():
                message += f"- {key}: {value}\n"

            return JSONResponse(content={"message": message})
    
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