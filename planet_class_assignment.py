class planet:
    earth_year=365.25
    def __init__(self,planet_name,diameter,no_of_moons,len_of_year):
        self.planet_name=planet_name
        self.diameter=diameter
        self.no_of_moons=no_of_moons
        self.len_of_years=len_of_year
    def radius_of_planet(self):
        self.radius=(self.diameter/2)
        print("The Radius of ",self.planet_name,"is",self.radius)
    def num_of_days(self):
        if(self.planet_name=="Merury" or self.planet_name=="Venus" or self.planet_name=="Earth" or self.planet_name=="Mars"):
            print("The number of days in",self.planet_name,"is",self.len_of_years)
        else:
           self.len_of_years=self.len_of_years*self.earth_year
           print("The no of days in",self.planet_name,"is",self.len_of_years)

def largest_planet(*planets):
    for planet in planets:
        if(planet.diameter==max_size):
            print("The largest planet is",planet.planet_name)
mercury=planet("Mercury",4879,0,88)
venus=planet("Venus",12100,0,225)
earth=planet("Earth",12755,1,365)
mars=planet("Mars",6786,2,687)
jupiter=planet("Jupiter",142800,79,12)
saturn=planet("Saturn",120537,82,29.5)
uranus=planet("Uranus",51819,27,84)
neptune=planet("Neptune",49529,14,165)
max_size=max(mercury.diameter,venus.diameter,earth.diameter,mars.diameter,jupiter.diameter,saturn.diameter,uranus.diameter,neptune.diameter)

neptune.radius_of_planet()
jupiter.num_of_days()
largest_planet(mercury,venus,earth,mars,jupiter,saturn,uranus,neptune)
