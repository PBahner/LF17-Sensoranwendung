from lf17_sensor.component import Actor, Sensor


class RoomHeater:
    __actor: Actor
    __sensor: Sensor

    def __init__(self, actor: Actor, sensor: Sensor):
        self.__actor = actor
        self.__sensor = sensor

    def get_actor(self) -> Actor:
        return self.__actor

    def get_sensor(self) -> Sensor:
        return self.__sensor
