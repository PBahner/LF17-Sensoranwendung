class Component:
    __id: str
    __connected: bool

    def __init__(self, id, connected):
        self.__id = id
        self.__connected = connected


class Actor(Component):
    __status: bool

    def __init__(self, id, connected, status=False):
        super().__init__(id, connected)

        self.__status = status


class Sensor(Component):
    __temperature: float

    def __init__(self, id, connected, temperature):
        super().__init__(id, connected)

        self.__temperature = temperature
