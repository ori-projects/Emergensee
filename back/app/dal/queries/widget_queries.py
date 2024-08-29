GET_WIDGETS_QUERY = """
SELECT 
    (SELECT COUNT(*) FROM Users) AS totalUsers,
    (SELECT COUNT(*) FROM Users WHERE isActive = TRUE) AS activeUsers,
    (SELECT COUNT(*) FROM Users WHERE isActive = FALSE) AS nonActiveUsers,
    (SELECT COUNT(*) FROM Admins) AS totalAdmins,
    (SELECT COUNT(*) FROM Doctors) AS totalDoctors,
    (SELECT COUNT(*) FROM Patients) AS totalPatients,
    (SELECT COUNT(*) FROM Algorithms) AS totalAlgorithms,
    (SELECT AVG(success_rank) FROM Algorithms) AS AverageRankOfSuccess,
    (SELECT SUM(num_uses) FROM Algorithms) AS totalUsages,
    (SELECT COUNT(*) FROM Models WHERE labeled = TRUE) AS labeledModels,
    (SELECT COUNT(*) FROM Models WHERE labeled = FALSE) AS unlabeledModels;
"""