from car import Car
class Truck(Car):
    def __init__(self,color,max_speed,acceleration,tyre_friction,max_cargo_weight):
        super().__init__(color,max_speed,acceleration,tyre_friction)
        if(max_cargo_weight<0):
            raise ValueError("Invalid value for cargo_weight")
        self.max_cargo_weight=max_cargo_weight
        self._cargo=0
        self.horn="Honk Honk"
    @property
    def cargo(self):
        return self._cargo
    def load(self,cargo_weight):
        if cargo_weight<0 :
            raise ValueError("Invalid value for cargo_weight")
        elif self._current_speed!=0 :
            print("Cannot load cargo during motion")
        elif self._cargo+cargo_weight<=self.max_cargo_weight :
            self._cargo+=cargo_weight
        else:
            print("Cannot load cargo more than max limit: {}".format(self.max_cargo_weight))
    def unload(self,cargo_weight):
        if cargo_weight<0:
            raise ValueError("Invalid value for cargo_weight")
        elif self._current_speed!=0 :
            print("Cannot unload cargo during motion")
        elif(self._cargo-cargo_weight>=0):
            self._cargo-=cargo_weight