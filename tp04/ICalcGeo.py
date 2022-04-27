from abc import ABCMeta, abstractmethod

class ICalcGeo(metaclass=ABCMeta):


    @abstractmethod
    def surface(self):
        pass