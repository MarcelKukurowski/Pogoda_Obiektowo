class Animal:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    
    @property # Getter
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value
    
    @age.deleter
    def age(self):
        del self.__age

x = Animal('Burek', 2)

print(x.age)

x.age = 4 # modyfikuje atrybut age

print(x.age)

del x.age # Usuwa atrybut age

print(x.__dict__)