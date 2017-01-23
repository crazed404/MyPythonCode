#Owen Fitzgerald
#My first program for the Python class

print "Enter the amount of flour (cups): ",
flour = raw_input()

print "Enter the amount of water (cups): ",
water = raw_input()

print "Enter the amount of salt (teaspoons): ",
salt = raw_input()

print "Enter the amount of yeast (teaspoons): ",
yeast = raw_input()

print "Enter the loaf adjustment factor (e.g 3 will triple the size): ",
factor = raw_input()

print "Flour: %.2f " % (float(flour) * float(factor)) + "cups"
print "Water: %.2f " % (float(water) * float(factor)) + "cups"
print "Salt: %.2f " % (float(salt) * float(factor)) + "teaspoons"
print "Yeast: %.2f " % (float(yeast) * float(factor)) + "teaspoons"
print "Don't burn it!"