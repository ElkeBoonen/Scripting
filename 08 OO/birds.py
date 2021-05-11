import os
from playsound import playsound
from datetime import date

class Bird:
    species = "bird"

    def whoIsThis(self):
        print(self.species)


class Parrot(Bird):
    species = "parrot"

    def __calculateAge(self, birthdate):
        return date.today().year - birthdate.year 

    # constructor (fill with properties)
    def __init__(self, name, birthdate, color):
        self.name = name
        self.__age = self.__calculateAge(birthdate)
        self.color = color

    def getAge(self):
        return self.__age
    
    def setAge(self, birthdate):
        self.__age = self.__calculateAge(birthdate)

    def sing(self):
        playsound('parrot.wav')

    def talk(self, text):
        print(self.name, "says '" + text + "'")

    def whoIsThis(self):
        super().whoIsThis()
        print("- My name is " + self.name)
    
