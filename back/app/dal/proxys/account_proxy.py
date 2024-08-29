from fastapi.responses import FileResponse
from app.dal.databases.postgresql_connection import PostgresqlConnection
from app.dal.queries.account_queries import (
    CREATE_ADMIN_QUERY, CREATE_DOCTOR_QUERY, CREATE_PATIENT_QUERY, DELETE_ACCOUNT_QUERY,
    DELETE_ADMIN_QUERY, DELETE_DOCTOR_PATIENTS_QUERY, DELETE_DOCTOR_QUERY, DELETE_PATIENT_QUERY, GET_ACCOUNTS,
    GET_ADMIN_BY_USER_ID_QUERY, GET_DOCTOR_BY_USER_ID_QUERY,
    GET_PATIENTS_BY_DOCTOR_ID_QUERY, LOGIN
)

class AccountProxy:
    """
    Proxy class for interacting with the database through PostgreSQL queries.
    """

    def __init__(self):
        """
        Initializes the AccountProxy instance by obtaining a PostgreSQL database connection instance.
        """
        self.db = PostgresqlConnection.get_instance()

    def create_admin(self, request):
        """
        Creates a new admin in the database.

        Args:
        user_id (str): User ID of the admin.

        Raises:
        Exception: If there's an error while executing the SQL query.
        """
        try:
            cursor = self.db.cursor()
            cursor.execute(CREATE_ADMIN_QUERY, (request.email, request.username, request.password))
            self.db.commit()
            print("Admin created successfully")
        except Exception as e:
            print(f"Error creating admin: {e}")

    def create_doctor(self, request):
        """
        Creates a new doctor in the database.

        Args:

        Raises:
        Exception: If there's an error while executing the SQL query.
        """
        try:
            cursor = self.db.cursor()
            cursor.execute(CREATE_DOCTOR_QUERY, (request.email, request.username, request.password))
            self.db.commit()
            print("Doctor created successfully")
        except Exception as e:
            print(f"Error creating doctor: {e}")

    def create_patient(self, name, age, phoneNumber, imagePath, email, doctorId):
        """
        Creates a new patient in the database.

        Args:
        name (str): Name of the patient.
        age (int): Age of the patient.
        phoneNumber (str): Phone number of the patient.
        imagePath (str): Image path of the patient.
        email (str): Email address of the patient.
        doctor_id (int): ID of the doctor associated with the patient.

        Raises:
        Exception: If there's an error while executing the SQL query.
        """
        try:
            saved = FileResponse(imagePath)

            if saved.status_code != 200:
                print(f"Error creating patient: {e}")
                return
            
            cursor = self.db.cursor()
            cursor.execute(CREATE_PATIENT_QUERY, (name, age, phoneNumber, imagePath, email, doctorId))
            self.db.commit()
            print("Patient created successfully")
        except Exception as e:
            print(f"Error creating patient: {e}")

    def get_admin_by_user_id(self, user_id):
        """
        Retrieves admin information from the database based on user ID.

        Args:
        user_id (str): User ID of the admin.

        Returns:
        tuple: Admin information fetched from the database.

        Raises:
        Exception: If there's an error while executing the SQL query.
        """
        try:
            cursor = self.db.cursor()
            cursor.execute(GET_ADMIN_BY_USER_ID_QUERY, (user_id,))
            return cursor.fetchone()
        except Exception as e:
            print(f"Error retrieving admin: {e}")

    def get_doctor_by_user_id(self, user_id):
        """
        Retrieves doctor information from the database based on user ID.

        Args:
        user_id (str): User ID of the doctor.

        Returns:
        tuple: Doctor information fetched from the database.

        Raises:
        Exception: If there's an error while executing the SQL query.
        """
        try:
            cursor = self.db.cursor()
            cursor.execute(GET_DOCTOR_BY_USER_ID_QUERY, (user_id,))
            return cursor.fetchone()
        except Exception as e:
            print(f"Error retrieving doctor: {e}")

    def get_patients_by_doctor_id(self, doctor_id):
        """
        Retrieves patients associated with a doctor from the database based on doctor ID.

        Args:
        doctor_id (int): ID of the doctor.

        Returns:
        list: List of patients associated with the specified doctor.

        Raises:
        Exception: If there's an error while executing the SQL query.
        """
        try:
            cursor = self.db.cursor()
            cursor.execute(GET_PATIENTS_BY_DOCTOR_ID_QUERY, (doctor_id,))
            return cursor.fetchall()
        except Exception as e:
            print(f"Error retrieving patients: {e}")

    def delete_admin(self, user_id):
        """
        Deletes admin from the database based on user ID.

        Args:
        user_id (str): User ID of the admin.

        Raises:
        Exception: If there's an error while executing the SQL query.
        """
        try:
            cursor = self.db.cursor()
            cursor.execute(DELETE_ADMIN_QUERY, (user_id,))
            self.db.commit()
            print("Admin deleted successfully")
        except Exception as e:
            print(f"Error deleting admin: {e}")

    def delete_doctor(self, user_id):
        """
        Deletes doctor from the database based on user ID.

        Args:
        user_id (str): User ID of the doctor.

        Raises:
        Exception: If there's an error while executing the SQL query.
        """
        try:
            cursor = self.db.cursor()
            cursor.execute(DELETE_DOCTOR_QUERY, (user_id,))
            self.db.commit()
            print("Doctor deleted successfully")
        except Exception as e:
            print(f"Error deleting doctor: {e}")

    def delete_patient(self, patient_id):
        """
        Deletes patient from the database based on patient ID.

        Args:
        patient_id (int): ID of the patient.

        Raises:
        Exception: If there's an error while executing the SQL query.
        """
        try:
            cursor = self.db.cursor()
            cursor.execute(DELETE_PATIENT_QUERY, (patient_id,))
            self.db.commit()
            print("Patient deleted successfully")
        except Exception as e:
            print(f"Error deleting patient: {e}")

    def login(self, email, password):
        """
        Get account by email and password.

        Args:
        email (str): The email of the user.
        password (str): The password of the user.

        Returns:
        list: List of accounts fetched from the database.

        Raises:
        Exception: If there's an error while executing the SQL query.
        """
        try:
            cursor = self.db.cursor()
            cursor.execute(LOGIN, (email, password))
            accounts = cursor.fetchall()
            return accounts
        except Exception as e:
            print(f"Error retrieving accounts: {e}")
        finally:
            cursor.close()


    def get_accounts(self, id):
        """
        Get all accounts except the account with the id.

        Args:
        id (int): The id of the user.

        Returns:
        list: List of accounts fetched from the database.

        Raises:
        Exception: If there's an error while executing the SQL query.
        """
        try:
            cursor = self.db.cursor()
            cursor.execute(GET_ACCOUNTS, (id,))
            accounts = cursor.fetchall()
            return accounts
        except Exception as e:
            print(f"Error retrieving accounts: {e}")
        finally:
            cursor.close()

    def delete_account(self, request):
        """
        Deletes account from the database.

        Args:
        request (DeleteAccountRequest): delete account request.

        Raises:
        Exception: If there's an error while executing the SQL query.
        """
        try:
            cursor = self.db.cursor()
            if request.role == 2:
                cursor.execute(DELETE_ACCOUNT_QUERY, (request.email, request.name, request.password, 2))
                self.db.commit()
                print("Admin deleted successfully")
            else:
                cursor.execute(DELETE_ACCOUNT_QUERY, (request.email, request.name, request.password, 1))
                cursor.execute(DELETE_DOCTOR_PATIENTS_QUERY, (request.id,))
                self.db.commit()
                print("Doctor deleted successfully")

        except Exception as e:
            print(f"Error deleting admin: {e}")
