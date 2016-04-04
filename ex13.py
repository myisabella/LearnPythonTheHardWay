from sys import argv

script, first, second, third = argv
weather = raw_input("What's the weather today? ")

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

print "Today's weather is like: %s" % weather