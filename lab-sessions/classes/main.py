from classes import Country  

italy = Country("Italy", "Europe", 55, 55)
france = Country("France", "Europe", 65, 55)

italy.print_info()
france.print_info()

italy.change_people(60)  
print(f"Italy's new population: {italy.people}")

italy.calculate_flowers()
italy.print_info()

