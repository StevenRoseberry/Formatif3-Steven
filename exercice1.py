from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Animal(ABC) :
    __nom:str=""
    __age:int =0
    __poids:float = 0

    # def __init__(self,nom,age,poids) :
    #     self.__nom = nom
    #     self.__age = age
    #     self.__poids = poids

    @property
    def nom(self):
        return self.__nom

    @nom.setter
    def nom(self, value):
        self.nom = value

    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, age):
        self.__age = age

    @property
    def poids(self):
        return self.__poids
    @poids.setter
    def poids(self, poids):
        self.__poids = poids

    @abstractmethod
    def parler(self) :
        pass
    @abstractmethod
    def se_deplacer(self) :
        pass

@dataclass
class AnimalMuet(Animal) :

    # def __init__(self, nom, age, poids):
    #     super().__init__(nom, age, poids)

    def parler(self) :
        print(f"{self.nom} est muet")


@dataclass
class Lion(AnimalMuet):
    __dangereux:bool=True

    # def __init__(self,nom,age,poids) :
    #     super().__init__(nom,age,poids)
    #     #le lion est toujurs dangereux
    #     #self.__dangereux=True

    def se_deplacer(self) :
        print(f"{self.nom} court")


@dataclass
class Pingouin(AnimalMuet):
    def __init__(self,nom,age,poids):
        super().__init__(nom, age, poids)

    def se_deplacer(self):
        print(f"{self.nom} titube")

@dataclass
class Perroquet(Animal):
    dangereux: bool = False

    # def __init__(self,nom,age,poids,dangereux=False):
    #     super().__init__(nom, age, poids)
    #     self.dangereux = dangereux

    def parler(self):
        print(f"{self.nom} repete")

    def se_deplacer(self):
        print(f"{self.nom} vole")

    def __str__(self):
        desc =f"Perroquet nommé {self.nom} age de {self.age} ans pesant {self.poids} lb."
        if self.dangereux :
            desc+=" Attention dangereux!"
        return desc


# Programme principal
if __name__ == "__main__":

    #Le lion est toujours dangereux
    lion = Lion("Simba", 5, 180.5)

    #Le pingouin n'a pas d'attrinut dangereux
    pingouin = Pingouin("Pingu", 3, 12.3)

    #Ce perroquet particulier est dangereux
    perroquet = Perroquet("Coco", 17, 3.3,dangereux=True)

    zoo = [lion, pingouin,perroquet]

    for animal in zoo:
        print(animal)
        animal.parler()
        animal.se_deplacer()
        print("---------------------")

    print(repr(perroquet))


