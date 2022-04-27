


from Rectangle import Rectangle


class Carre(Rectangle):


    def __init__(self, *, cote) -> None:
        print(f"def __init__(self, *, {cote})")
        super().__init__(longueur=cote, largeur=cote)
        self._cote = cote
    

    @property
    def cote(self):
        return self._cote

    @cote.setter
    def cote(self,cote):
        self._cote = cote
        self.largeur = cote
        self.longueur = cote

    def __del__(self):
        print(f"{__class__.__name__} __del__")

    def __str__(self):
        return f"{__class__.__name__} {self._cote=}"

