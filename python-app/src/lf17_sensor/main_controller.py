from abc import ABC, abstractmethod
from typing import List

from component import Actor, Sensor, Component


class ControllerInterface(ABC):
    @abstractmethod
    def get_components(self):
        pass


class MemController(ControllerInterface):
    __component_list: List

    def __init__(self, components: List):
        super().__init__()
        self.__component_list = components.copy()

    def get_components(self) -> List[Component]:
        return self.__component_list
