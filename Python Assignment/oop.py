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
