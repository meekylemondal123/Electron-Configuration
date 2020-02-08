import periodictable as pr

def nearest_noble(atomic_number):
    noble_gases = [2, 10, 18, 36, 54, 86, 118]

    for x in noble_gases:
        if atomic_number - x < 0:
            return noble_gases[noble_gases.index(x) - 1]
        
        elif atomic_number - x == 0:
            return atomic_number
        
    
def configuration(atomic_number):
    orbitals = {"1s": 2, "2s": 2, "2p": 6, "3s": 2, "3p": 6, "4s": 2, "3d": 10, "4p": 6, "5s": 2, "4d": 10, "5p": 6, "6s": 2, "4f": 14, "5d": 10, "6f": 6, "7s": 2, "5f": 14,
                "6d": 10, "7p": 6}
    
    
    total_electrons = 0
    energy_level = ""
    final_electron = False
    
    # The following is the longhand electron configuration
    for keys in orbitals.keys():
        for potential in range(0, orbitals[keys]):
            atomic_number -= 1

            # Figure this bit out here
            if atomic_number == 0:
                energy_level += " " + keys + "" + str(potential + 1)
                final_electron = True
                break

        if final_electron:
            return energy_level
        else:
            energy_level += " " + keys + "" + str(orbitals[keys])
  
def shorten_configuration(configuration1, configuration2, noble_name):
    conf1list = configuration1.split(" ")
    conf2list = configuration2.split(" ")

    final_config = " [" + noble_name + "]"
    
    for x in conf1list:
        if x not in conf2list:
            final_config += " " + x

    return final_config
            
def display(atomic_number, noble_name, noble_number):
    configuration_atom = configuration(atomic_number)
    configuration_noble = configuration(noble_number)

    
    
    user_choice = input("Please enter whether or not you would like the shorthand (s) or longhand (l) configuration of your element: \n")

    if user_choice == "s":
        return shorten_configuration(configuration_atom, configuration_noble, noble_name)
    elif user_choice == "l":
        return configuration_atom
    
def main():
    exists = False
    atomic_number = 0
    nearest_noble_gas = 0
    noble_number = 0
    noble_name = ""
    
    # Try and find the nearest noble gas here, and then pass it into the method
    
    element_name = input("Please enter the element you would like to find the electron configuration of: \n")


    element_name = element_name.lower()

    for el in pr.elements:
        if el.name == element_name:
            exists = True
            element_name = el.name
            atomic_number = el.number


    noble_gas = nearest_noble(atomic_number)

    for el in pr.elements:
        if el.number == noble_gas:
            noble_name = el.symbol
            noble_number = el.number

    if exists:
        final_level = display(atomic_number, noble_name, noble_number)
        
        print ("The electron configuration for " + element_name + " is:" + str(final_level))
    else:
        print ("The element could not be found!")

main()
