from PySide6.QtWidgets import QApplication

from lf17_sensor.room_heater import RoomHeater
from main_window import Display
from main_controller import MemController
from component import *


def main() -> None:
    sensor0 = Sensor("Sensor0", True, 25.0)
    actor0 = Actor("Actor0", True, True)

    device = RoomHeater(actor0, sensor0)

    app = QApplication()
    controller = MemController()
    window = Display(controller, device)

    #TODO somehow adjust this to the Table
    window.setFixedSize(400, 400)

    window.show()
    app.exec()


if __name__ == "__main__":
    main()
