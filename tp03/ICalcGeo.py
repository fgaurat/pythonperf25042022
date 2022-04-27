from abc import ABCMeta, abstractmethod

class ICalcGeo(metaclass=ABCMeta):


    @abstractmethod
    def surface(self):
        pass


    # def surface(self):
        # raise NotImplementedError('surface !')