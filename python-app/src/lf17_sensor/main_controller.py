from abc import ABC, abstractmethod
from typing import List

from component import Actor, Sensor, Component
from lf17_sensor.room_heater import RoomHeater


class ControllerInterface(ABC):
    @abstractmethod
    def get_components(self, object):
        pass


class MemController(ControllerInterface):

    def __init__(self):
        super().__init__()
        # self.__component_list = components.copy()

    def get_components(self, room_heater: RoomHeater) -> List[Component]:
        device_components = [room_heater.get_sensor(), room_heater.get_actor()]
        return device_components
