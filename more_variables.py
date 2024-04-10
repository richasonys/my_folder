# What does %s, %r, and %d do again?
# You’ll learn more about this as you continue, but they are “formatters.” They tell Python to take
# the variable on the right and put it in to replace the %s with its value. 
my_name = "Riya"
my_age = 35
my_height = 89
my_weight = 55
my_eyes = 'black'
my_teeth = 'white'
my_hair = 'black'

print ("Let's talk about %s." % my_name) # %s for string
print ( "He's %d inches tall." % my_height) # %d for numbers
print ("He's %d pounds heavy." % my_weight)
print ("Actually that's not too heavy.")
print ("She's got %s eyes and %s hair." % (my_eyes, my_hair))
print ("Her teeth are usually %s depending on the coffee." % my_teeth)

# this line is tricky, try to get it exactly right
print ("If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight))
