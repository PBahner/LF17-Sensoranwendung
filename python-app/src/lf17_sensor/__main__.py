from PySide6.QtWidgets import QApplication
from .main_window import Display
from .main_controller import MemController
from .component import *


def main() -> None:
    sensor0 = Sensor("Sensor0", True, 25.0)
    sensor1 = Sensor("Sensor1", True, 21.0)
    actor0 = Actor("Actor0", True, True)

    components = sensor0, sensor1, actor0

    app = QApplication()
    controller = MemController(components)
    window = Display(controller)

    window.show()
    app.exec()


if __name__ == "__main__":
    main()
