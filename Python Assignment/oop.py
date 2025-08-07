#class defintion and encapsulation example
class superHero():

    def __init__(self,name,power,city):
        self.name = name #public attribute
        self._power = power #protected attribute
        self.__city = city #private attribute
    
    def get_city(self):
        return self.__city
    
    def set_city(self, new_city):
        self.__city = new_city
    
    def description(self):
        return f"{self.name} has the power of {self._power} and protects the city of {self.__city}."

 #example of Inheritance   
class superVillan(superHero):

    def __init__(self,name,power,city,evil_plan):
        super().__init__(name, power, city)
        self.evil_plan = evil_plan

    def description(self):
        return f"{self.name} has the power of {self._power}, plans to {self.evil_plan}, and operates in the city of {self.get_city()}."

#exmple of polymorphism

def introduce_character(character):
    print(character.description())

Hero = superHero("Superman", "Flight", "Metropolis")
Villain = superVillan("Lex Luthor", "Genius Intellect", "Metropolis", "take over the world")

introduce_character(Hero)
introduce_character(Villain)

#  Demonstrating Encapsulation
print(Hero.name)              # Public
print(Hero._power)            # Protected (not recommended but possible)
print(Hero.get_city())        # Access private attribute via getter
Hero.set_city("Gotham")       # Modify private attribute via setter
print(Hero.get_city())

#ACTIVITY 2

class Animal:
    def __init__(self,name, species,movement):
        self.name = name
        self.species = species
        self.movement = movement

    def move(self):
        return f"{self.name} the {self.species} moves by {self.movement}."
    
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Dog", "running")
        self.breed = breed

    def move(self):
        return f"{self.name} the {self.breed} dog runs quickly."
    
class Fish(Animal):
    def __init__(self, name):
        super().__init__(name, "Fish", "swimming")
    
    def move(self):
        return f"{self.name} the fish swims gracefully."
    
Dog1 = Dog("Buddy", "Golden Retriever")
Fish1 = Fish("Nemo")

print(Dog1.move())  # Buddy the Golden Retriever dog runs quickly.
print(Fish1.move())  # Nemo the fish swims gracefully.