# What is the difference between %r and %s?
# We use %r for debugging, since it displays the “raw” data of the variable, but we use %s and
# others for displaying to users.

# What’s the point of %s and %d when you can just use %r?
# The %r is best for debugging, and the other formats are for actually displaying variables to users.

x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)
print (x)
print (y)
print ("I said: %r." % x)
print ("I also said: '%s'." % y)
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"
print (joke_evaluation % hilarious)
w = "This is the left side of..."
e = "a string with a right side."
print (w + e)

print ("Mary had a little lamb.")
print ("Its fleece was white as %s." % 'snow')
print ("And everywhere that Mary went.")
print ("." * 10) # what'd that do?

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end4 = "s"
end5 = "e"
end6 = "b"
end7 = "u"
end8 = "r"
end9 = "g"
end10 = "e"
end11 = "r"

print ((end1 + end2 + end3 + end4 + end5 + end6) + (end7 + end8 + end9 + end10 + end11))
