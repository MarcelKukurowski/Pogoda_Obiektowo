lista = [0, 6, 21, 4]

# Normalne iterowanie
'''
for i in lista:
    print(i)
    
'''


#__iter__()
#__next__()

# iter() , next() - funkcje pythona

# Iterowanie na funkcjach

'''

b = iter(lista)

print(next(b))
print(next(b))
print(next(b))
print(next(b))

'''

# Iterowanie na funkcjach magicznych

'''
c = lista.__iter__()
print(c.__next__())
print(c.__next__())
print(c.__next__())
print(c.__next__())

'''

# Budowa pętli for

'''

liter_obj = iter(lista)

while True:
    try:
        element = next(liter_obj)
        print(element)
    except StopIteration:
        break

'''

# Nieskończony iterator

'''

x = iter(int, 1)

print(next(x))

'''

# an = a1 + (n-1)*r  Wzór na ciąg arytmetyczny

class Sequence:
    def __iter__(self):
        self.num = 14
        return self
    
    def __next__(self):
        num = self.num
        self.num += 3
        return num

x = iter(Sequence())

# Wypisze: 14, 17, 20, 23
print(next(x))
print(next(x))
print(next(x))
print(next(x))



