class Component:
    __id: str
    __connected: bool

    def __init__(self, id: str, connected: bool):
        self.__id = id
        self.__connected = connected

    def get_id(self):
        return self.__id

    def get_connected(self):
        return self.__connected


class Actor(Component):
    __status: bool

    def __init__(self, id, connected, status: bool):
        super().__init__(id, connected)

        self.__status = status

    def get_status(self):
        return self.__status


class Sensor(Component):
    __temperature: float

    def __init__(self, id, connected, temperature: float):
        super().__init__(id, connected)

        self.__temperature = temperature

    def get_temperature(self):
        return self.__temperature
