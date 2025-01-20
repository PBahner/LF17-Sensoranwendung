from PySide6.QtWidgets import QApplication
from .main_window import Display
from .main_controller import MemController
from .data_storage import DataStoragePrinter, DataStorageFileWriter
from .component import *


def main() -> None:
    sensor0 = Sensor("Sensor0", True, 25.0, "°C")
    sensor1 = Sensor("Sensor1", True, 22.0, "°C")
    actor0 = Actor("Actor0", True, True)

    components = sensor0, sensor1, actor0

    app = QApplication()
    controller = MemController(components, DataStorageFileWriter())
    window = Display(controller)

    # TODO somehow adjust this to the Table
    window.setFixedSize(400, 400)

    window.show()
    app.exec()


if __name__ == "__main__":
    main()
