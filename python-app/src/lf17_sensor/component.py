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


class Actor(Component):
    __status: bool

    def __init__(self, component_id: str, connected: bool, status: bool) -> None:
        super().__init__(component_id, connected)

        self.__status = status

    def get_status(self) -> bool:
        return self.__status


class Sensor(Component):
    __temperature: float

    def __init__(self, component_id: str, connected: bool, temperature: float) -> None:
        super().__init__(component_id, connected)

        self.__temperature = temperature

    def get_temperature(self) -> float:
        return self.__temperature

    def set_temperature(self, temp):
        self.__temperature = temp