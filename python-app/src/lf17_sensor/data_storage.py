from abc import ABC, abstractmethod
from .component import Component


class DataStorageInterface(ABC):

    @abstractmethod
    def write_measurement(self, component: Component) -> None:
        pass


class DataStoragePrinter(DataStorageInterface):
    def write_measurement(self, component: Component) -> None:
        print(component)


# Folgende Klasse soll implementiert werden, um die Messwerte in eine Datei zu schreiben.
class DataStorageFileWriter(DataStorageInterface):
    pass

