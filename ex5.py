#  need to embed variables inside a string by using { } sequence
#  then put variables inside { }
#  must start string  with the letter 'f' for "format"
#  f"Hello {somevar} --->  this string needs to be formatted, put these variables in there




my_name = 'Ringo George'
my_age = 35
my_height = 74
my_weight =  210
my_eyes = 'hazel'
my_teeth = 'white'
my_hair = 'brown'

print("--------------------------------------")

print(f"Let's talk about {my_name}.")
print(f"My height {my_height} is in inches.")
print(f"My weight is {my_weight} pounds.")
print(f"Actually that is not too heavy.")
print(f"You have {my_eyes} eyes and {my_hair} hair.")
print(f"My teeth are usually {my_teeth}, depending on the amount of caffeine I drink.")

# this line is interesting
total = my_age + my_height + my_weight
print(f"If you add {my_age} + {my_height} + {my_weight} you will get {total}.")

#  if you do not put the 'f' in the print function will print out
#  Let's talk about {my_name}  <---->  You have {my_eyes} eyes and {my_hair} hair.