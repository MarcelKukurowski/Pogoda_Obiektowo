'''
#Normarna lista
lista = [x*x for x in range(10)]

print(lista)

# Generator
generator = (x*x for x in range(10))

for i in range(10): 
    print(next(generator))
'''

'''
def a(liczba):
    wynik = liczba
    yield wynik # yield przechowuje zmienną 
    wynik = wynik + liczba
    yield wynik
    wynik = liczba * liczba
    yield wynik

b = a(30)
for i in range(3):
    print(next(b))

print("=========")

for item in a(3):
    nowy_wynik = item/2
    print(nowy_wynik)


'''

class IleRazyDoKwadratu:
    def __init__(self, liczba, ilosc_iteracji):
        self.liczba = liczba
        self.il_iteracji = ilosc_iteracji
        self.end_iter = 0

    def __iter__(self):
        self.liczba

    def __next__(self):
        if self.end_iter < self.il_iteracji:
            self.il_iteracji -= 1
            self.liczba = self.liczba ** 2
            return self.liczba
        raise StopIteration

x = IleRazyDoKwadratu(2,5)

for i in range(5):
    print(next(x))
    


