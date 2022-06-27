#vehicle class with custrutor
class Vehicle:
	def __init__(self,type):   #constructor for type
		self.type=type 

#new subclass Automobile from vehicle
class Automobile(Vehicle):
	def __init__(self,type,year,make,model,doors,roof):
		super().__init__(type) #super function is called to invoke vehicle class constructor
		self.year=year
		self.make=make
		self.model=model
		self.doors=doors
		self.roof=roof

type_i=input("Type of vehicle :")
year_i=input("Enter the year :")
make_i=input("Enter who manufacture :")
model_i=input("Enter the model :")
doors_i=input("Enter the number of doors(2 or 4) :")
roof_i=input("solid or sun roof :")
A=Automobile(type_i,year_i,make_i,model_i,doors_i,roof_i) #calling the constructor with alls values readed

#print the deatils
print("\nVehicle Type :"+A.type)
print("\nYear :"+A.year)
print("\nMake :"+A.make)
print("\nModel :"+A.model)
print("\nNo of doors :"+A.doors)
print("\nType of roof :"+A.roof)