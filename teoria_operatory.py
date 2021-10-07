class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(selft):
        return 'f{self.name} {self.age}'

    # MATEMATYCZNE
    def __add__(self, other):
        self.age = self.age + int(other)
        return self.age

    def __sub__(self, other):
        self.age = self.age - int(other)

    def __mul__(self, other):
        self.age = self.age * int(other)

    #def __truediv__
    #def __floordiv__
    #def __mod__
    #def __pow__
    #def __int__
    #def __float__

    def __int__(self):
        return self.age

    def __len__(self):
        return self.age

    # PORÓWNANIA

    # < __lt__
    # <= __le__
    # == __eq__
    # != __ne__
    # >= __gt__
    # > __gt__

x = Animal('Burek', 2)

print(x+4)
print(x.age)

type(x)
type(int(x))