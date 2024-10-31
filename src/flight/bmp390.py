from dataclasses import dataclass

import busio

from base.component import Component


@dataclass
class BMP390State:
    pressure: float = 0
    altitude: float = 0
    temperature: float = 0


class BMP390Component(Component):

    def __init__(self, i2c: busio.I2C, address: int = 0x77):
        self._state = BMP390State()

    @property
    def state(self):
        return self._state

    def dispatch(self):
        ...
