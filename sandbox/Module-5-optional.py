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

