import { PatientModule } from "../Modules/patient/patient.module";

export class PatientMapper {
    static mapToPatient(data: any[]): PatientModule {
        const description = ""; // Example: Initialize with default values or leave empty
        const imagePath = data[5] || ""; // Example: Initialize with default values or leave empty
        const name = data[3] || ""; // Assuming name is at index 2 in your data array
        const email = data[1] || ""; // Assuming email is at index 1 in your data array
        const phoneNumber = data[2] || ""; // Assuming phoneNumber is at index 3 in your data array
        const age = data[4] || ""; // Assuming age is at index 4 in your data array
        const image = null; // Initialize with default value or leave empty
        const bloodPressure = ""; // Initialize with default value or leave empty
        const bloodSugar = ""; // Initialize with default value or leave empty
        const procedureCount = ""; // Initialize with default value or leave empty
        const infectionsReported = ""; // Initialize with default value or leave empty
        const bodyTemperature = ""; // Initialize with default value or leave empty
        const heartRate = ""; // Initialize with default value or leave empty
        const operativeProcedure = ""; // Initialize with default value or leave empty
        const feelingsAndUrge = ""; // Initialize with default value or leave empty
        const disease = ""; // Initialize with default value or leave empty
        const criticalFeelings = ""; // Initialize with default value or leave empty

        // Create and return a new instance of PatientModule with mapped data
        return new PatientModule(
            description,
            imagePath,
            image,
            name,
            email,
            phoneNumber,
            age,
            bloodPressure,
            bloodSugar,
            procedureCount,
            infectionsReported,
            bodyTemperature,
            heartRate,
            operativeProcedure,
            feelingsAndUrge,
            disease,
            criticalFeelings
        );
    }
}
