import math;

def fuel_for(payload_mass):
    total_fuel_mass = 0
    mass_iter = payload_mass
    
    while(mass_iter >= 9):
        fuel_iter = math.floor(mass_iter / 3) - 2
        total_fuel_mass += fuel_iter
        mass_iter = fuel_iter
    
    return total_fuel_mass

with open("Day01/input.txt", "r") as input:
    fuel_needed = 0
    
    for line in input:
        fuel_needed += fuel_for(int(line))
    
    print("Total fuel mass needed: %i" % fuel_needed)