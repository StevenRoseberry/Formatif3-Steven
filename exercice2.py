# class StationMesure:
#
#     def __init__(self, nom_station, capteurs):
#         self.station = station
class Capteur():
    compteur = 0
    unite: int

    def __init__(self, unite):
        self.id_capteur = Capteur.compteur
        Capteur.compteur += 1
        self.unite = unite
        def mesurer(self):
            pass

class Thermometre(Capteur):
    def __init__(self):
        super().__init__("C")


class Barometre(Capteur):
    def __init__(self):
        super().__init__("kP")

class Luxmetre(Capteur):
    def __init__(self):
        super().__init__("Lux")
    # def mesurer(self):

if __name__ == '__main__':
    # station =

    print(Thermometre(), Barometre(), Luxmetre())