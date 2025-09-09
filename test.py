class Product:
	def __init__(self, name, price):
		self.name = name
		self.__price = price	
	def set_price(self, price):
		self.__price = price
	def get_price(self):
		return self.__price


p1 = Product("아이폰", 100000)
p1.set_price(50000)

