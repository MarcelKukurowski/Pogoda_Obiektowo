class A: # klasa bazowa
    LICZBA = 20
    def a(self):
        print(self.LICZBA)

class B(A): # klasa potomna
    def a(self):
        print("Metoda klasy B")

b = B()

print(b.a()) 

