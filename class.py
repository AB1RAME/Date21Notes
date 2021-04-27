# class AmazingDog:
#     animal_kind='canine'
#     def bark(self):
#         print(self.animal_kind)
#         return 'woof!'
# Bob=AmazingDog()
# Bob.animal_kind='dolphin'
# print(Bob.animal_kind)

# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# p=Person('John',36)
# print(p.name)
# print(p.age)

# class Car:
#     def setMax(self,maxspeed):
#         self.__maxspeed=maxspeed
#     def getMax(self):
#         return self.__maxspeed
#     def setBrake(self,braketime):
#         self.__braketime=braketime
#     def getBrake(self,braketime):
#         return self.__braketime
#     def setAccelerations(self,acceleration):
#         self.__acceleration=acceleration
#     def getAcceleration(self,acceleration):
#         return self.__acceleration
#     def __init__(self,brand,colour):
#         self.brand=brand
#         self.colour=colour
#     def currentspeed(self,acceleration,braketime):
#         return acceleration*braketime


class Car:
    def __init__(self,brand,colour,acceleration,time,maxspeed):
        self.brand=brand
        self.colour=colour
        self.acceleration=acceleration
        self.time=time
        self.__maxspeed=maxspeed
    def set_Max(self,maxspeed):
        self.__maxspeed=maxspeed
    def get_Max(self,maxspeed):
        return self.__maxspeed
    def currentSpeed(self,acceleration,time):
        self.speed=0
        self.speed=self.speed+self.acceleration*self.time
        if self.speed>self.__maxspeed:
            self.speed==self.__maxspeed
        elif self.speed<0:
            self.speed=0
        return self.speed
    def __repr__(self):
        return(f"The {self.colour} {self.brand} is travelling at high speed  with a maximum speed of {self.__maxspeed}")

c=Car('bmw','black',10,0.5,200)
print(c)

