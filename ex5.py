name = 'Zed A. Shaw'
age = 35 #not a lie
height = 74 #inches
height_cm = height * 2.54 #centimeters
weight = 180 #lbs
weight_kg = weight * 0.453592 #kilograms
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'


print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print(f"Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

#this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}")

#Adding three double-quotes allows me to write a string in more than one line
print(f"""If i convert from imperial into standard, I get that {name} 
is {height_cm} centimeters tall and {weight_kg} kilograms heavy.""")
