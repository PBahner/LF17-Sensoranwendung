class Component:
    __component_id: str
    __connected: bool

    def __init__(self, component_id: str, connected: bool) -> None:
        self.__component_id = component_id
        self.__connected = connected

    def get_id(self) -> str:
        return self.__component_id

    def get_connected(self) -> bool:
        return self.__connected

    def __repr__(self) -> str:
        return f"{self.__component_id}"


class Actor(Component):
    __status: bool

    def __init__(self, component_id: str, connected: bool, status: bool) -> None:
        super().__init__(component_id, connected)

        self.__status = status

    def get_status(self) -> bool:
        return self.__status

    def __repr__(self) -> str:
        return f"{self.get_id()} Status: {self.get_status()}"


class Sensor(Component):
    __value: float
    __unit: str

    def __init__(self, component_id: str, connected: bool, temperature: float, unit: str) -> None:
        super().__init__(component_id, connected)
        self.__unit = unit
        self.__value = temperature

    def get_value(self) -> float:
        return self.__value

    def set_value(self, temp: float) -> None:
        self.__value = temp

    def get_unit(self) -> str:
        return self.__unit

    def set_unit(self, unit: str) -> None:
        self.__unit = unit

    def __repr__(self) -> str:
        return f"{self.get_id()} Wert: {self.__value}{self.__unit}"
