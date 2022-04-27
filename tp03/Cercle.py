


import math

from ICalcGeo import ICalcGeo


class Cercle(ICalcGeo):

    def __init__(self,rayon) -> None:
        print(f"def __init__(self,{rayon})")
        self._rayon = rayon
    
    @property
    def rayon(self):
        return self._rayon

    @rayon.setter
    def rayon(self,rayon):
        self._rayon = rayon
    
    @property
    def surface(self):
        return math.pi*self._rayon**2

    def __del__(self):
        print(f"{__class__.__name__} __del__")

    def __str__(self):
        return f"{__class__.__name__} {self._rayon=}"
