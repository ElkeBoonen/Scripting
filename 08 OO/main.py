from birds import Bird, Parrot
from datetime import date

# object/instantiotion from Parrot class
blu = Parrot("Blu", date(2000, 2, 3), "blue")
jewel = Parrot("Jewel", date(2005, 2, 3), "blue")
bird = Bird()

bird_list = [blu, jewel, bird]

for bird in bird_list:
    bird.whoIsThis()

