# Deklaracja klasy
class Samochód:
    # Zmienne klasowe
    marka = None
    color = 0
    max_speed = None

    # Inicjalizator (Konstruktor) klasy, wywoływany podczaas tworzenia instancji
    # self (odpowiednik this) - zmienna pozwalająca na dostanie się do zmiennych klasowych, metod, itp.
    def __init__(self):
        pass

    # Definicja metody (funkcji w klasie) / akcja
    def speed(self, courrentSpeed):
        if courrentSpeed == 150:
            # odwołanie albo wywołanie samej siebie to rekonstrukcja
            return self.speed
        self.max_speed = courrentSpeed
        return courrentSpeed
    
# Przypisanie zmiennej do klasy skutkuje referencja - czyli przejęciem "właściwości" klasy
audi = Samochód()
audi.max_speed = 150
audi.color = 'czarny'
audi.marka = "BMW"
audi.speed(400)

print(audi.color)

# W tym przypadku "BMW" nadpisuje "audi" i podmienia jego kolor na czerwony
bmw = audi
bmw.color = "czerwony"

print(audi.color)
print(bmw.color)