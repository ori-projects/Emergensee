import asyncio
import uvicorn
import sys
from app.controllers.accounts_controller import AccountsController
from app.controllers.admins_controller import AdminsController
from app.controllers.algorithms_controller import AlgorithmsController
from app.controllers.dataset_operations_controller import DatasetPperationsController
from app.controllers.dataset_views_controller import DatasetViewsController
from app.controllers.doctors_controller import DoctorsController
from app.controllers.models_controller import ModelsController
from app.controllers.patients_controller import PatientsController
from app.controllers.tools_controller import ToolsController
from app.controllers.utils_controller import UtilsController
from app.controllers.widgets_controller import WidgetsController
from app.entities.configs.endpoint import Endpoint
from app.services.utils.startup import Startup

sys.path.append(".Controllers")

async def start():
    controllers = [
        AccountsController.get_app(),
        AdminsController.get_app(),
        AlgorithmsController.get_app(),
        DatasetPperationsController.get_app(),
        DatasetViewsController.get_app(),
        DoctorsController.get_app(),
        ModelsController.get_app(),
        PatientsController.get_app(),
        WidgetsController.get_app(),
        UtilsController.get_app(),
        ToolsController.get_app()
    ]

    tasks = []
    for current_port, controller in enumerate(controllers, start = Endpoint.port):
        print(f"Starting server for {controller.__class__.__name__} on port {current_port}...")
        config = uvicorn.Config(controller, host = Endpoint.host, port = current_port)
        server = uvicorn.Server(config)
        task = asyncio.create_task(server.serve())
        tasks.append(task)

    await asyncio.gather(*tasks)

if __name__ == "__main__":
    Startup()
    asyncio.run(start())