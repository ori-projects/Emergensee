import { Widgets } from "../Modules/widgets/widgets";

export class WidgetsMapper {
    static mapToWidgets(data: any[]): Widgets {
        const [
            totalUsers,
            activeUsers,
            nonActiveUsers,
            totalAdmins,
            totalDoctors,
            totalPatients,
            totalAlgorithms,
            averageRankOfSuccess,
            totalUsages,
            labeledModels,
            unlabeledModels
        ] = data;

        // Create and return the Widgets object
        return new Widgets({
            totalUsers,
            activeUsers,
            nonActiveUsers,
            totalAdmins,
            totalDoctors,
            totalPatients,
            totalAlgorithms,
            rankOfSuccess: averageRankOfSuccess,
            totalUsages,
            labeledModels,
            unlabeledModels
        });
    }
}