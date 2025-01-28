import random
from PySide6.QtWidgets import *
from PySide6 import QtCore
from typing import List
from .main_controller import MemController
from .component import *
from .data_getter import DataGetter
import datetime


class ComponentTableModel(QtCore.QAbstractTableModel):
    def __init__(self, components: List[Component], parent=None):
        super().__init__(parent)
        self.__components = components

    def rowCount(self, parent=QtCore.QModelIndex()) -> int:
        return len(self.__components)

    def columnCount(self, parent=QtCore.QModelIndex()) -> int:
        return 3

    def data(self, index: QtCore.QModelIndex, role: int = QtCore.Qt.DisplayRole):
        if not index.isValid():
            return None

        component = self.__components[index.row()]

        if role == QtCore.Qt.DisplayRole:
            if index.column() == 0:
                return component.get_id()
            elif index.column() == 1:
                if isinstance(component, Actor):
                    return str(component.get_status())
                elif isinstance(component, Sensor):
                    return str(component.get_value()) + component.get_unit()
            elif index.column() == 2:
                return str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        return None

    def update_data(self, components: List[Component]):
        self.beginResetModel()
        self.__components = components
        self.endResetModel()


class Display(QWidget):
    def __init__(self, controller: MemController) -> None:
        super().__init__()
        self.__controller = controller

        self.__vertical_layout_main = QVBoxLayout()

        self.__component_button = QPushButton("Refresh Components")
        self.__component_button.clicked.connect(self._on_component_button)

        # QTableView statt QTableWidget
        self.__table_view = QTableView()
        self.__model = ComponentTableModel(self.__controller.get_components())
        self.__table_view.setModel(self.__model)

        self.__exit_button = QPushButton("Exit")
        self.__exit_button.clicked.connect(self._on_exit_button)

        self.setWindowTitle("Room Heater")
        self.__vertical_layout_main.addWidget(self.__component_button)
        self.__vertical_layout_main.addWidget(self.__table_view)
        self.__vertical_layout_main.addWidget(self.__exit_button)
        self.setLayout(self.__vertical_layout_main)

        self._on_component_button()

    @QtCore.Slot()
    def _on_component_button(self):
        self.__controller.update_sensors()
        self.__model.update_data(self.__controller.get_components())

    @QtCore.Slot()
    def _on_exit_button(self) -> None:
        self.close()
        return
