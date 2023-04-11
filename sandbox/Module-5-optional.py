class Person:
    apples = 0
    ideas = 0

johanna = Person()
johanna.apples = 1
johanna.ideas = 1

martin = Person()
martin.apples = 2
martin.ideas = 1

def exchange_apples(you, me):
    temp_apples = you.apples
    you.apples = me.apples
    me.apples = temp_apples
    return you.apples, me.apples
    
def exchange_ideas(you, me):
    total_ideas = you.ideas + me.ideas
    you.ideas = total_ideas
    me.ideas = total_ideas
    return you.ideas, me.ideas

exchange_apples(johanna, martin)
print("Johanna has {} apples and Martin has {} apples".format(johanna.apples, martin.apples))
exchange_ideas(johanna, martin)
print("Johanna has {} ideas and Martin has {} ideas".format(johanna.ideas, martin.ideas))


class City:
    name = ""
    country = ""
    elevation = 0
    population = 0

city1 = City()
city1.name = "Cusco"
city1.country = "Peru"
city1.elevation = 3399
city1.population = 358052

city2 = City()
city2.name = "Sofia"
city2.country = "Bulgaria"
city2.elevation = 2290
city2.population = 1241675

city3 = City()
city3.name = "Seoul"
city3.country = "South Korea"
city3.elevation = 38
city3.population = 9733509

def max_elevation_city(min_population):
    return_city = City()

    if city1.population >= min_population and (return_city.elevation == 0 or city1.elevation > return_city.elevation):
        return_city = city1

    if city2.population >= min_population and (return_city.elevation == 0 or city2.elevation > return_city.elevation):
        return_city = city2

    if city3.population >= min_population and (return_city.elevation == 0 or city3.elevation > return_city.elevation):
        return_city = city3

    if return_city.name:
        return "{}, {}".format(return_city.name, return_city.country)
    else:
        return ""

print(max_elevation_city(100000))  # Should print "Cusco, Peru"
print(max_elevation_city(1000000))  # Should print "Sofia, Bulgaria"
print(max_elevation_city(10000000))  # Should print ""

mystring = "My Name is Robel "
print(mystring)
print(mystring[4:25])


def count_numbers(first, last):
  # Loop through the numbers from first to last 
  x = first
  while x <= last:
    print(x)
    x+= 1

count_numbers(0,6)

# Creating a string
my_string = "This is my string # for Pyton 3.9"

# Reverse the entire string
reversed_string = my_string[::-1]
print("Reversed string:", reversed_string)

# Get the last character of the string
last_character = my_string[-1]
print("Last character:", last_character)

# Get every other character in the string
every_other_character = my_string[::2]
print("Every other character:", every_other_character)

# Check the length of the string
length = len(my_string)
print("Length of the string:", length)

# Get the 4th character in the string
fourth_character = my_string[3]
print("4th character:", fourth_character)

# Get the 4th character through the 9th character in the string
fourth_to_ninth = my_string[3:9]
print("4th to 9th character:", fourth_to_ninth)

# Get the 7th through last character in the string
seventh_to_last = my_string[6:]
print("7th to last character:", seventh_to_last)
