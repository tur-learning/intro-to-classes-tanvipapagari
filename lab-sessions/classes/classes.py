class Person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def info(self):
        print(self.name, self.age, self.height)

    def change_age(self, new_age):
        self.age = new_age

class Country:
    def __init__(self, name, continent, people, flowers):
        self.name = name
        self.continent = continent
        self.people = people
        self.flowers = flowers
        
    def print_info(self):
        print(f"Country: {self.name}, Continent: {self.continent}, Population: {self.people}, Flowers: {self.flowers}")
        
    def change_people(self, new_people): 
        self.people = new_people

    def calculate_flowers(self):
        print("Flowers per Person:")
        if self.flowers != 0:
            print(f"{self.people / self.flowers} 🌼") 
        else:
            print("Cannot divide by zero :).")