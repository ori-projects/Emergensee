CREATE_DATASET = "INSERT INTO datasets (name, description) VALUES (%s, %s)"
SELECT_DATASET_BY_ID = "SELECT * FROM datasets WHERE id = %s"
UPDATE_DATASET_DESCRIPTION = "UPDATE datasets SET description = %s WHERE id = %s"
DELETE_DATASET = "DELETE FROM datasets WHERE id = %s"
