CREATE_ALGORITHM_QUERY = """
    INSERT INTO Algorithms (algorithm_name, success_rank, num_uses) 
    VALUES (%s, %s, %s)
    RETURNING id;
"""

DELETE_ALGORITHM_QUERY = """
    DELETE FROM Algorithms 
    WHERE id = %s;
"""

GET_ALGORITHMS = """
    SELECT * FROM Algorithms;
"""

GET_ALGORITHM_BY_ID_QUERY = """
    SELECT * FROM Algorithms 
    WHERE id = %s;
"""

UPDATE_ALGORITHM_QUERY = """
    UPDATE Algorithms 
    SET algorithm_name = %s, success_rank = %s, num_uses = %s 
    WHERE id = %s;
"""

GET_STATS_QUERY = """
    SELECT 
        AVG(success_rank) AS average_success_rank, 
        SUM(num_uses) AS total_num_uses, 
        COUNT(*) AS total_num_algorithms 
    FROM Algorithms;
"""