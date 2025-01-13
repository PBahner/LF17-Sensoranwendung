from PySide6.QtWidgets import *
from PySide6 import QtCore
from PySide6.QtGui import QIcon
from typing import List
from component import *


class Display(QWidget):
    __actors: List
    __sensors: List
    # __main_layout_vertical: QVBoxLayout
    __test_button: QPushButton

    def __init__(self, controller):
        super().__init__()
        self.__test_button = QPushButton("Test me")

        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.__test_button)
        self.setLayout(vertical_layout)

    def add_sensor(self, sensor: Sensor):
        self.__sensors.append(sensor)

    def add_actor(self, actor: Actor):
        self.__actors.append(actor)

    # def get_sensors(self, id):
    #     return self.__sensors

    # def get_actor(self, id):
    #   ...
    #     return actor.get_status
