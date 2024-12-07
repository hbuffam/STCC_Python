#SGF is for Surface Gravity Factor, these are constants

MERCURY_SGF = 0.38
VENUS_SGF = 0.91
MOON_SGF = 0.165
MARS_SGF = 0.38
JUPITER_SGF = 2.34
SATURN_SGF = 0.93
URANUS_SGF = 0.92
NEPTUNE_SGF = 1.12
PLUTO_SGF = 0.066

# we are asking for the persons Name and their Weight on Earth so we can calculate their weight on dif planets

s_Name =  int( input("What is your name?: "))
n_Weight = float( input("Enter your weight: "))
fPlanetaryWeight = n_Weight