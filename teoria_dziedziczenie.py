class A:
    LICZBA = 20
    def a(self):
        print(self.LICZBA)

class C:
    LITERA = 'c'
    def c(self):
        print(self.LITERA)

class B(A,C):
    pass

b = B()

print(b.a()) 
print(b.c())
