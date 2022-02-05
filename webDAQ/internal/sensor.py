from typing import Optional, List
from webDAQ.internal.setting import Setting


class Sensor:
    """
    A model class representing a skeleton for the implementation of sensors
    """

    def __init__(self, name: str, channels: List[str], channel_names: List[str], channel_units: List[str],
                 description: Optional[str] = None, settings: Optional[List[Setting]] = None):
        self.name = name
        if type(description) is None:
            self.description = ""
        else:
            self.description = description
        if len(channels) is not len(channel_names) or len(channels) is not len(channel_units):
            raise Exception("Passed channel configuration are of unequal length!")
        else:
            self.channel_count = len(channels)
            self.channels = channels
            self.channel_names = channel_names
            self.channel_units = channel_units

        if type(settings) is None:
            self.settings = []
        else:
            self.settings = settings

    def start(self) -> None:
        pass

    def get_data(self):
        pass

    def close(self) -> None:
        pass
