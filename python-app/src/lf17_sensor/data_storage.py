from abc import ABC, abstractmethod
from .component import Component


class DataStorageInterface(ABC):

    @abstractmethod
    def write_measurement(self, component: Component) -> None:
        pass


class DataStoragePrinter(DataStorageInterface):
    def write_measurement(self, component: Component) -> None:
        print(component)


class DataStorageFileWriter(DataStorageInterface):
    def write_measurement(self, component: Component) -> None:
        with open("measurement.txt", "a", encoding="utf-8") as measurement_file:
            measurement_file.write(f"{component}\n")

