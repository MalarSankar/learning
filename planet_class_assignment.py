class planet:
    earth_year=365.25
    def __init__(self,planet_name,diameter,no_of_moons,len_of_year):
        self.planet_name=planet_name.lower()
        self.diameter=diameter
        self.no_of_moons=no_of_moons
        self.len_of_years=len_of_year.lower()
    def find_and_print_radius_of_planet(self):
        print ("The Radius of ",self.planet_name,"is",(self.diameter/2))
    def find_and_print_num_of_days(self):
        days=(self.len_of_years).split()
        if(days[1]=="days"):
            print("The total number of days in",self.planet_name,"is",days[0])
        else:
           print("The total number of days in",self.planet_name,"is",int(days[0])*self.earth_year)

def largest_planet(*planets):
    for planet in planets:
        if(planet.diameter==max_size):
            print("The largest planet is",planet.planet_name)
mercury=planet("Mercury",4879,0,"88 days")
venus=planet("Venus",12100,0,"225 days")
earth=planet("Earth",12755,1,"365 days")
mars=planet("Mars",6786,2,"687 days")
jupiter=planet("Jupiter",142800,79,"12 earth years")
saturn=planet("Saturn",120537,82,"29.5 earth years")
uranus=planet("Uranus",51819,27,"84 earth years")
neptune=planet("NEPTUNE",49529,14,"165 EARTH YEARS")
max_size=max(mercury.diameter,venus.diameter,earth.diameter,mars.diameter,jupiter.diameter,saturn.diameter,uranus.diameter,neptune.diameter)

neptune.find_and_print_radius_of_planet()
jupiter.find_and_print_num_of_days()
largest_planet(mercury,venus,earth,mars,jupiter,saturn,uranus,neptune)
