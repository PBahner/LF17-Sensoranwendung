from abc import ABC, abstractmethod
import requests
import random


class DataGetter(ABC):
    @abstractmethod
    def get_sensor_value(self) -> float:
        pass


class RandomDataGetter(DataGetter):
    __old_value: float

    def __init__(self) -> None:
        self.__old_value = 0

    def get_sensor_value(self) -> float:
        change = random.randint(0, 5)

        if random.choice([True, False]):
            return self.__old_value + change
        return self.__old_value - change


# Folgende Klasse soll implementiert werden, um echte Wetterdaten zu erhalten.
class ApiDataGetter(DataGetter):
    def get_sensor_value(self) -> float:
        return requests.get("https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m").json()["current"]["temperature_2m"]

