import math
from car import Car
class RaceCar(Car):
    def __init__(self, color, max_speed,acceleration,tyre_friction):
        Car.__init__(self, color, max_speed,acceleration,tyre_friction)
        self._nitro=0
        self.horn="Peep Peep\nBeep Beep"
    @property
    def nitro(self):
        return self._nitro
    def apply_brakes(self):
        if(self._current_speed>self._max_speed/2):
            self._nitro+=10
        super().apply_brakes()
    def accelerate(self):
        if(self._nitro!=0):
            self._current_speed+=math.ceil(0.3*self._acceleration)
            self._nitro-=10
        super().accelerate()