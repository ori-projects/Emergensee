CREATE_DOCTOR_QUERY = "INSERT INTO users (email, name, password, role) VALUES (%s, %s, %s, 1)"
CREATE_ADMIN_QUERY = "INSERT INTO users (email, name, password, role) VALUES (%s, %s, %s, 2)"
CREATE_PATIENT_QUERY = "INSERT INTO Patients (full_name, age, phone_number, photo, email, doctor_id) VALUES (%s, %s, %s, %s, %s, %s)"

GET_ADMIN_BY_USER_ID_QUERY = """
SELECT U.id, U.name, U.imagePath, U.email, U.password, U.role, U.isActive
FROM Admins A
JOIN Users U ON U.id = A.user_id
WHERE A.user_id = %s
"""
GET_DOCTOR_BY_USER_ID_QUERY = """
SELECT U.id, U.name, U.imagePath, U.email, U.password, U.role, U.isActive, D.rank, D.phoneNumber, D.numberOfPatients, D.active, D.dateOfBirth
FROM Doctors D
JOIN Users U ON U.id = D.user_id
WHERE D.user_id = %s
"""
GET_PATIENTS_BY_DOCTOR_ID_QUERY = "SELECT * FROM Patients WHERE doctor_id = %s"

LOGIN = """
SELECT *
FROM Users
WHERE email = %s AND password = %s
"""

GET_ACCOUNTS = """
SELECT *
FROM Users
WHERE id <> %s
"""

UPDATE_DOCTOR_QUERY = "UPDATE Doctors SET rank = %s, phoneNumber = %s, numberOfPatients = %s, active = %s, dateOfBirth = %s WHERE user_id = %s"
UPDATE_PATIENT_QUERY = "UPDATE Patients SET name = %s, description = %s, imagePath = %s, email = %s, doctor_id = %s WHERE id = %s"

DELETE_ADMIN_QUERY = "DELETE FROM Admins WHERE user_id = %s"
DELETE_DOCTOR_QUERY = "DELETE FROM Doctors WHERE user_id = %s"
DELETE_PATIENT_QUERY = "DELETE FROM Patients WHERE id = %s"

DELETE_ACCOUNT_QUERY = "DELETE FROM Users WHERE email = %s AND name = %s AND password = %s AND role = %s"
DELETE_DOCTOR_PATIENTS_QUERY = "DELETE FROM Patients WHERE doctor_id = %s"