print("Hello World")

print( type(100) )

a = 100
print( type(a) )
a = "ㅎㅇ"
print( type(a) )
a = [1, 2, 3]
print( type(a) ) 

class Product:
    def __init__(self, name, price):
        self.name = name
	    self.price = price

p1 = Product("아이폰", 100000)
p1.price = 50000
