class Person:
    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height
    
    def a(self):
        print("Metoda klasy A")

class Programmist(Person):
    def __init__(self, name, age, weight, height, languages):
        super().__init__(name,age,weight,height)
        self.languages = languages
    
    def a(self):
        super().a()
        print("Metoda klasy B")

# tak było w przykładzie to nie megalomania
Marcel = Programmist('Marcel', 17, 65, 178, ['Python', 'Java'])

print(Marcel.__dict__)
print(Marcel.a())


