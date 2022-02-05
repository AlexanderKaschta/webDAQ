from webDAQ.internal.sensor import Sensor

import board
import adafruit_bme680


class BME680(Sensor):

    def __init__(self):
        super(BME680, self).__init__(name="BME680", channels=["T", "H", "P", "h", "R"],
                                     channel_names=["Temperature", "Humidity", "Pressure", "Altitude",
                                                    "Gas resistance"],
                                     channel_units=[u"\u2103", "%", "hPa", "m", "Ohm"],
                                     description="A Bosch sensor")

        self.board = None
        self.sensor = None

    def start(self) -> None:
        # Configure the sensor here
        self.board = board.I2C()
        self.sensor = adafruit_bme680.Adafruit_BME680_I2C(self.board, debug=False)

    def get_data(self):
        # Get the data
        return [self.sensor.temperature, self.sensor.relative_humidity, self.sensor.pressure, self.sensor.altitude,
                self.sensor.gas]

    def close(self) -> None:
        # There's nothing to do here
        return
