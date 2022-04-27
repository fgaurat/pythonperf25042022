
from ICalcGeo import ICalcGeo
from Singleton import Singleton


class Rectangle(metaclass=Singleton):
    
    cpt=0
    _instance = None
    
    def __init__(self,*,longueur=1,largeur=1) -> None:
        assert longueur >0 and largeur >0
        print(f"def __init__(self,{longueur},{largeur}) -> None")
        self._longueur = longueur
        self._largeur = largeur
        Rectangle.cpt+=1
    
    @classmethod
    def get_instance(cls):
        if Rectangle._instance is None:
            Rectangle._instance = cls()
        
        return Rectangle._instance

    @classmethod
    def build_from_str(cls,value):
        k = ['longueur','largeur']
        v = [int(s) for s in value.split(",")]

        d = dict(zip(k,v))

        return cls(**d)

    
    @property
    def longueur(self):
        print("def get_longueur(self)")
        return self._longueur
    
    @longueur.setter
    def longueur(self,a):
        assert a >0
        self._longueur = a
    
    @property
    def largeur(self):
        
        return self._largeur

    @largeur.setter
    def largeur(self,a):
        assert a >0
        
        self._largeur = a
    
    
    @property
    def surface(self):
        return self._longueur*self._largeur

    @staticmethod
    def get_cpt(v):
        print("def get_cpt(self)")
        print(v)
        return Rectangle.cpt

    def __str__(self):
        return f"{__class__.__name__} {self._longueur=} {self._largeur=}"

    def __int__(self):
        return self.surface
    
    def __eq__(self, o: object) -> bool:
        return self._largeur == o._largeur and self._longueur == o._longueur

    def __del__(self):
        print(f"{__class__.__name__} __del__")

    
    # longueur = property(get_longueur,set_longueur)
    # largeur = property(get_largeur,set_largeur)
    # surface = property(get_surface)