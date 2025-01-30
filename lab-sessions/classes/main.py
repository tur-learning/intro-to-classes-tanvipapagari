from classes import Country

italy= Country ("Italy", "Europe", 55, 55)

france= Country ("France", "Europe", 65, 55)

italy.print_info()
france.print_info()

france.change_people(70)
france.print_info()

print("Flowers per People:")
italy.calculate_flowers()
italy.print_info()
