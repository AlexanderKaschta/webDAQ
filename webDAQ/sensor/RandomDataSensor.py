import random
import time

from webDAQ.internal.sensor import Sensor


class RandomDataSensor(Sensor):

    def __init__(self):
        super().__init__(name="RandomDataSensor",
                         channels=["N"],
                         channel_names=["Random data"],
                         channel_units=[""],
                         description="A simple device generating random data")

        # Set a random seed for the generator
        random.seed(time.time())

    def start(self) -> None:
        return

    def get_data(self):
        return random.random()

    def close(self) -> None:
        return
