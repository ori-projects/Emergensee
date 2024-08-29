from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.entities.requests.create_account_request import CreateAccountRequest
from app.entities.requests.delete_account_request import DeleteAccountRequest
from app.entities.requests.get_accounts_request import GetAccountsRequest
from app.entities.requests.login_request import LoginRequest
from app.entities.requests.patient_request import PatientRequest
from app.interfaces.controller import Controller
from app.dal.proxy import Proxy

class AccountsController(Controller):
    """
    Controller class for managing accounts through FastAPI.
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

        # Initialize Proxy and access account database
        proxy_instance = Proxy()
        account_db_instance = proxy_instance.account_db

        # Configure CORS middleware for cross-origin requests
        app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["GET", "POST", "PUT", "DELETE"],
            allow_headers=["Content-Type", "Authorization"],
        )

        @app.post("/create-account", tags=["Controller Accounts"], summary="Create Account")
        async def create_account(create_account_request: CreateAccountRequest):
            """
            Create a new account.

            Args:
            create_account_request: CreateAccountRequest

            Returns:
            dict: A message indicating success or failure.
            
            Raises:
            HTTPException: If there's an error creating the admin (status code 500).
            """
            try:
                if create_account_request.role == 'doctor':
                    account_db_instance.create_doctor(create_account_request)
                    return {"success": True}
                elif create_account_request.role == 'admin':
                    account_db_instance.create_admin(create_account_request)
                    return {"success": True}
                else:
                    return {"success": False}
            except Exception as e:
                raise HTTPException(status_code=500, detail=f"Error creating admin: {e}")

        @app.post("/delete-account", tags=["Controller Accounts"], summary="Delete Account")
        async def delete_account(delete_account_request: DeleteAccountRequest):
            """
            Delete a new account.

            Args:
            delete_account_request: DeleteAccountRequest

            Returns:
            dict: A message indicating success or failure.
            
            Raises:
            HTTPException: If there's an error creating the admin (status code 500).
            """
            try:
                account_db_instance.delete_account(delete_account_request)
                return {"success": True}
            except Exception as e:
                raise HTTPException(status_code=500, detail=f"Error creating admin: {e}")

        # Endpoint to handle login
        @app.post("/login", tags=["Controller Accounts"], summary="Login to the app")
        def login(data: LoginRequest):
            """
            Auth account to perform login to the database.

            Args:
            data (LoginRequest): Request object containing email and password.

            Returns:
            dict: Success message or error message.

            Raises:
            HTTPException: If login fails due to invalid credentials or server error.
            """
            try:
                # Call the login method from AccountProxy
                account = account_db_instance.login(data.email, data.password)
                if account:
                    return {"success": True, "account": account[0]}
                else:
                    return {"success": False}
            except Exception as e:
                raise HTTPException(status_code=500, detail=f"Error retrieving accounts: {e}")

        # Endpoint for health check
        @app.get("/health", tags=["Health Check"], summary="Health Check")
        def health_check():
            """
            Endpoint to perform a health check.

            Returns:
            dict: A dictionary indicating the health status of the service.
            """
            return {"status": "ok", "message": "Service is up and running"}
        # Endpoint to create a new patient
        
        @app.post("/get-accounts", tags=["Accounts"], summary="Get all the accounts")
        def get_accounts(account_data: GetAccountsRequest):
            """
            Get all the accounts from the database.

            Args:
            - account_data (GetAccountsRequest): Contains the id field.

            Returns:
            - dict: Success message or error message with the accounts.
            """
            try:
                account_list = account_db_instance.get_accounts(account_data.id)
                if account_list:
                    return {"success": True, "accounts": account_list}
                else:
                    return {"success": False}
            except Exception as e:
                raise HTTPException(status_code=500, detail=f"Error retrieving accounts: {e}")

        return app