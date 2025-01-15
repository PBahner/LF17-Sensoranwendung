import random
from PySide6.QtWidgets import *
from PySide6 import QtCore
from typing import List
from .main_controller import MemController
from .component import *
import datetime


class Display(QWidget):
    __vertical_layout_main: QVBoxLayout
    __table: QTableWidget
    __component_button: QPushButton
    __exit_button: QPushButton

    def __init__(self, controller: MemController) -> None:
        super().__init__()
        self.__controller = controller
        self.__vertical_layout_main = QVBoxLayout()

        self.__component_button = QPushButton("Refresh Components")
        self.__component_button.clicked.connect(self._on_component_button)

        self.__table = self.generate_table(self.__controller.get_components())

        self.__exit_button = QPushButton("Exit")
        self.__exit_button.clicked.connect(self._on_exit_button)

        self.setWindowTitle("Room Heater")
        self.__vertical_layout_main.addWidget(self.__component_button)
        self.__vertical_layout_main.addWidget(self.__table)
        self.__vertical_layout_main.addWidget(self.__exit_button)
        self.setLayout(self.__vertical_layout_main)


    # def add_sensor(self, sensor: Sensor) -> None:
    #     self.__sensors.append(sensor)

    # def add_actor(self, actor: Actor) -> None:
    #     self.__actors.append(actor)

    # def get_sensors(self, id) -> None:
    #     return self.__sensors

    # def get_actor(self, id) -> None:
    #   ...
    #     return actor.get_status

    def generate_table(self, components: List[Component]) -> QTableWidget:

        table = QTableWidget()
        table.setRowCount(len(components))
        table.setColumnCount(3)

        # TODO think about adding connection somewhere
        table.setHorizontalHeaderLabels(["Id", "Value", "Last Updated"])

        #TODO fix table height
        for row, component in enumerate(components):
            table.setItem(row, 0, QTableWidgetItem(component.get_id()))

            if isinstance(component, Actor):
                table.setItem(row, 1, QTableWidgetItem(str(component.get_status())))
            elif isinstance(component, Sensor):
                table.setItem(
                    row, 1, QTableWidgetItem(str(component.get_value()) + component.get_unit())
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

    @QtCore.Slot()
    def _on_component_button(self):
        components = self.__controller.get_components()

        for sensor in components:
            if isinstance(sensor, Sensor):

                change = random.randint(0, 5)

                if random.choice([True, False]):
                   sensor.set_temperature(sensor.get_temperature() + change)
                else:
                   sensor.set_temperature(sensor.get_temperature() - change)

        table = self.generate_table(components)
        self.__vertical_layout_main.replaceWidget(self.__table, table)
        self.__table = table

    @QtCore.Slot()
    def _on_exit_button(self) -> None:
        self.close()
        return
