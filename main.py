# Generate a Star Wars name
def generate_star_wars_name(first_name, last_name, maiden_name, city):
  """
  Generates a Star Wars name using the provided parameters
  """
  star_wars_first_name = first_name[0:3] + last_name[0:3].lower()
  star_wars_last_name = maiden_name[0:4:1] + city[0:4].lower()
  star_wars_name = star_wars_first_name + " " + star_wars_last_name
  return star_wars_name

# Main program
message = "Make a Star Wars name"
print(message)

first_name = input("Enter your first name: ")
if type(first_name) != str:
  print('Please enter a valid first name.')

last_name = input("Enter your last name: ")
if type(last_name) != str:
  print('Please enter a valid last name.')

maiden_name_of_mother = input(
 "Enter your mother's maiden name: ").lower().capitalize()
if type(maiden_name_of_mother) != str:
  print('Please enter a valid maiden name.')

city_of_birth = input(
 "Enter the city your mother was born: ").lower().capitalize()
if type(city_of_birth) != str:
  print('Please enter a valid city.')

star_wars_name = generate_star_wars_name(first_name, last_name, maiden_name_of_mother, city_of_birth)

print(f"Your Star Wars name is + {star_wars_name}")