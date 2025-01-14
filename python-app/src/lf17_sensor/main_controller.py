from abc import ABC, abstractmethod
from typing import List, Sequence

from .component import Component


class ControllerInterface(ABC):
    @abstractmethod
    def get_components(self) -> List[Component]:
        pass


class MemController(ControllerInterface):
    __component_list: List[Component]

    def __init__(self, components: Sequence[Component]):
        super().__init__()
        self.__component_list = list(components)

    def get_components(self) -> List[Component]:
        return self.__component_list.copy()
