class Animal:
    def __init__(self,name):
        print("__init__ is calling")        
        self.name = name
        
    def speak(self):
        print("Name of the animal is ",self.name)
        print("This animal have ",self.leg, "leg")

    def eat(self):
        print("The animal is eating");

    @property
    def leg(self):
        print("in the leg getter function")
        return self._leg

    @leg.setter
    def leg(self,value):
        print("in the leg setter function")
        self._leg = value * 2

    

    #leg = property(legGetter,legSetter)    


class Cat(Animal):
    def __init__(self,name):
        print("Child cass __init__ is calling")
        super().__init__(name)
    def speak(self):
        super().speak()
        print("It is speaking from the child class")
        

cat = Cat("Shwe War")
cat.leg = 4
cat.speak()
cat.eat()
