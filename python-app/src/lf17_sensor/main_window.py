from PySide6.QtWidgets import *
from typing import List
from .main_controller import MemController
from .component import *
import datetime


class Display(QWidget):
    __actors: List[Actor]
    __sensors: List[Sensor]
    # __main_layout_vertical: QVBoxLayout
    __test_button: QPushButton

    def __init__(self, controller: MemController) -> None:
        super().__init__()
        self.__test_button = QPushButton("Test me")

        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.generate_table(controller.get_components()))
        self.setLayout(vertical_layout)

    def add_sensor(self, sensor: Sensor) -> None:
        self.__sensors.append(sensor)

    def add_actor(self, actor: Actor) -> None:
        self.__actors.append(actor)

    # def get_sensors(self, id):
    #     return self.__sensors

    # def get_actor(self, id):
    #   ...
    #     return actor.get_status

    def generate_table(self, components: List[Component]) -> QTableWidget:

        table = QTableWidget()
        table.setRowCount(len(components))
        table.setColumnCount(3)

        # TODO think about adding connected somewhere
        table.setHorizontalHeaderLabels(["Id", "Value", "Last Updated"])

        for row, component in enumerate(components):
            table.setItem(row, 0, QTableWidgetItem(component.get_id()))

            # Status oder Temperatur je nach Typ
            if isinstance(component, Actor):
                table.setItem(row, 1, QTableWidgetItem(str(component.get_status())))
            elif isinstance(component, Sensor):
                table.setItem(
                    row, 1, QTableWidgetItem(str(component.get_temperature()))
                )
            table.setItem(
                row,
                2,
                QTableWidgetItem(
                    str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                ),
            )
            table.resizeColumnToContents(2)

        return table
