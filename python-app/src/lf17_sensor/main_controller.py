from abc import ABC, abstractmethod
from typing import List, Sequence, Optional

from .component import Component
from .data_storage import DataStorageInterface


class ControllerInterface(ABC):
    @abstractmethod
    def get_components(self) -> List[Component]:
        pass


class MemController(ControllerInterface):
    __component_list: List[Component]
    __data_storage: Optional[DataStorageInterface]

    def __init__(self, components: Sequence[Component], data_storage: Optional[DataStorageInterface] = None):
        super().__init__()
        self.__component_list = list(components)
        self.__data_storage = data_storage

    def get_components(self) -> List[Component]:
        return self.__component_list.copy()

    def write_to_storage(self) -> None:
        if self.__data_storage is None:
            return

        for component in self.__component_list:
            self.__data_storage.write_measurement(component)
