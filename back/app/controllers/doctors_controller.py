import sys
import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.dal.proxy import Proxy
from app.interfaces.controller import Controller

# Add parent directory to sys.path to ensure relative imports work correctly
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class DoctorsController(Controller):
    """
    Controller class for managing doctors through FastAPI.
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
        account_db_instance = proxy_instance.account_db

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

        # Endpoint to create a doctor
        @app.post("/create-doctor", tags=["Controller Doctors"], summary="Create Doctor")
        def create_doctor(user_id: int, rank: str, phoneNumber: str, numberOfPatients: int, active: bool, dateOfBirth: str):
            """
            Endpoint to create a new doctor.

            Args:
            user_id (int): The ID of the doctor.
            rank (str): The rank of the doctor.
            phoneNumber (str): The phone number of the doctor.
            numberOfPatients (int): The number of patients of the doctor.
            active (bool): The active status of the doctor.
            dateOfBirth (str): The date of birth of the doctor.

            Returns:
            dict: A dictionary with a message indicating the success of the operation.

            Raises:
            HTTPException: If there is an error creating the doctor.
            """
            try:
                account_db_instance.create_doctor(user_id, rank, phoneNumber, numberOfPatients, active, dateOfBirth)
                return {"message": "Doctor created successfully"}
            except Exception as e:
                raise HTTPException(status_code=500, detail=f"Error creating doctor: {e}")

        # Endpoint to get a doctor by user ID
        @app.get("/get-doctor/{user_id}", tags=["Controller Doctors"], summary="Get Doctor by User ID")
        def get_doctor_by_user_id(user_id: int):
            """
            Endpoint to get doctor details by user ID.

            Args:
            user_id (int): The ID of the doctor to retrieve.

            Returns:
            dict: A dictionary containing the doctor information if found.

            Raises:
            HTTPException: If the doctor with the given ID is not found.
            """
            try:
                doctor = account_db_instance.get_doctor_by_user_id(user_id)
                if doctor:
                    return doctor
                else:
                    raise HTTPException(status_code=404, detail="Doctor not found")
            except Exception as e:
                raise HTTPException(status_code=500, detail=f"Error retrieving doctor: {e}")

        # Endpoint to update a doctor
        @app.put("/update-doctor/{user_id}", tags=["Controller Doctors"], summary="Update Doctor")
        def update_doctor(user_id: int, rank: str, phoneNumber: str, numberOfPatients: int, active: bool, dateOfBirth: str):
            """
            Endpoint to update doctor details.

            Args:
            user_id (int): The ID of the doctor to update.
            rank (str): The updated rank of the doctor.
            phoneNumber (str): The updated phone number of the doctor.
            numberOfPatients (int): The updated number of patients of the doctor.
            active (bool): The updated active status of the doctor.
            dateOfBirth (str): The updated date of birth of the doctor.

            Returns:
            dict: A dictionary with a message indicating the success of the operation.

            Raises:
            HTTPException: If there is an error updating the doctor.
            """
            try:
                account_db_instance.update_doctor(user_id, rank, phoneNumber, numberOfPatients, active, dateOfBirth)
                return {"message": "Doctor updated successfully"}
            except Exception as e:
                raise HTTPException(status_code=500, detail=f"Error updating doctor: {e}")

        # Endpoint to delete a doctor
        @app.delete("/delete-doctor/{user_id}", tags=["Controller Doctors"], summary="Delete Doctor")
        def delete_doctor(user_id: int):
            """
            Endpoint to delete a doctor.

            Args:
            user_id (int): The ID of the doctor to delete.

            Returns:
            dict: A dictionary with a message indicating the success of the operation.

            Raises:
            HTTPException: If there is an error deleting the doctor.
            """
            try:
                account_db_instance.delete_doctor(user_id)
                return {"message": "Doctor deleted successfully"}
            except Exception as e:
                raise HTTPException(status_code=500, detail=f"Error deleting doctor: {e}")

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