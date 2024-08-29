from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.entities.requests.create_account_request import CreateAccountRequest
from app.interfaces.controller import Controller
from app.dal.proxy import Proxy

class AdminsController(Controller):
    """
    Controller class for managing admins through FastAPI.
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
        account_db_instance = proxy_instance.account_db

        # Configure CORS middleware for cross-origin requests
        app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],  # Replace "*" with your specific origins if needed
            allow_credentials=True,
            allow_methods=["GET", "POST", "PUT", "DELETE"],
            allow_headers=["Content-Type", "Authorization"],
        )

        # Endpoint to create a new admin
        @app.post("/create-admin", tags=["Controller Admins"], summary="Create Admin")
        async def create_admin(user_id: int):
            """
            Create a new admin.

            Args:
            user_id (int): The user ID of the admin to create.

            Returns:
            dict: A message indicating success or failure.
            
            Raises:
            HTTPException: If there's an error creating the admin (status code 500).
            """
            try:
                account_db_instance.create_admin(user_id)
                return {"message": "Admin created successfully"}
            except Exception as e:
                raise HTTPException(status_code=500, detail=f"Error creating admin: {e}")

        # Endpoint to retrieve admin details by user ID
        @app.get("/get-admin/{user_id}", tags=["Controller Admins"], summary="Get Admin by User ID")
        async def get_admin_by_user_id(user_id: int):
            """
            Get admin details by user ID.

            Args:
            user_id (int): The user ID of the admin to retrieve.

            Returns:
            dict: Details of the admin.
            
            Raises:
            HTTPException: If admin is not found (status code 404) or if there's an error retrieving admin (status code 500).
            """
            try:
                admin = account_db_instance.get_admin_by_user_id(user_id)
                if admin:
                    return admin
                else:
                    raise HTTPException(status_code=404, detail="Admin not found")
            except Exception as e:
                raise HTTPException(status_code=500, detail=f"Error retrieving admin: {e}")

        # Endpoint to delete an admin by user ID
        @app.delete("/delete-admin/{user_id}", tags=["Controller Admins"], summary="Delete Admin")
        async def delete_admin(user_id: int):
            """
            Delete an admin.

            Args:
            user_id (int): The user ID of the admin to delete.

            Returns:
            dict: A message indicating success or failure.
            
            Raises:
            HTTPException: If there's an error deleting the admin (status code 500).
            """
            try:
                account_db_instance.delete_admin(user_id)
                return {"message": "Admin deleted successfully"}
            except Exception as e:
                raise HTTPException(status_code=500, detail=f"Error deleting admin: {e}")

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