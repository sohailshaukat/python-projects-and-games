class House():

	def __init__(self,rate,width,height):
		self.r=rate
		self.h=height
		self.w=width
		self.area=height*width
	def area(self):
		return str(self.area)+' square meter is the area'

	def __str__(self):
		print(f'RATE : {self.r} $ per m \n WIDTH : {self.w} m \n HEIGHT : {self.h} m \n AREA: {self.area} sqm')

	def cost(self):
		return self.area * self.r

print('WELCOME TO OUR COST CALCULATOR')
print('ENTER RATE , WIDTH , HEIGHT')
rate=float(input('RATE'))
width=float(input('WIDTH'))
height=float(input('HEIGHT'))
h1=House(rate=rate,width=width,height=height)
h1.__str__()
print(f'Total cost of tile = {h1.cost()} $' )
