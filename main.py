first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

star_wars_first_name = first_name[0:3] + last_name[0:3].lower()

maiden_name_of_mother = input(
 "Enter your mother's maiden name: ").lower().capitalize()

city_of_birth = input(
 "Enter the city your mother was born: ").lower().capitalize()

star_wars_last_name = maiden_name_of_mother[0:4:1] + city_of_birth[0:4].lower()

star_wars_name = star_wars_first_name + " " + star_wars_last_name

print(f"Your Star Wars name is + {star_wars_name}")
