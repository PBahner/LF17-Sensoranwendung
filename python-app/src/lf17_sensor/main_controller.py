from typing import List, Sequence, Optional

from .component import Component, Sensor
from .data_storage import DataStorageInterface
from .data_getter import DataGetter


class MemController:
    __component_list: List[Component]
    __data_storage: Optional[DataStorageInterface]
    __data_getter: DataGetter

    def __init__(self, components: Sequence[Component], data_getter: DataGetter, data_storage: Optional[DataStorageInterface] = None):
        super().__init__()
        self.__component_list = list(components)
        self.__data_storage = data_storage
        self.__data_getter = data_getter

    def get_components(self) -> List[Component]:
        return self.__component_list.copy()

    def __write_to_storage(self) -> None:
        if self.__data_storage is None:
            return

        for component in self.__component_list:
            self.__data_storage.write_measurement(component)

    def update_sensors(self) -> None:
        components = self.get_components()

        for sensor in components:
            if isinstance(sensor, Sensor):
                sensor.set_value(self.__data_getter.get_sensor_value())

        self.__write_to_storage()
