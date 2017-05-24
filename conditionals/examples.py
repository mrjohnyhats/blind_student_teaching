''' #start list of conditional operators
l == r - check if l equal r
l != r - check if l does not equal 4
l > r - check if l is greater than r
l < r - check if l is less than r
l >= r - check if l is greater than or equal to r
l <= r - check if l is less than or equal to r
l in a - check if l is an element or susbtring in a, a can be an dict, array, or string
c1 and c2 - check if the conditionals c1 and c2 are both true
c1 or c2 - check if either the conditional c1 or c2 is true
not c1 - check if the conditional c1 is false

#end list of conditional operators'''

''' #start simple conditionals examples

# set a variable to 5 and run code if it is equal to 5

a = 5
if a == 5:
    print("it works!")

# check if a variable is greater than 10

b = 100
if b > 10:
    print("it works!")

# check if b is greater than 10 and a is 5

if b > 10 and a == 5:
    print("it works!")

# check if b is greater than 10 or a is 15

if b > 10 or a == 15:
    print("it works!")

#end simple conditionals examples '''

''' #start advanced conditional examples

# print "a" if b is less than 10, if it isn't then print "b"

b = 10
if b < 10:
    print("a")
else:
    print("b")

# print "a" if b is not equal to 10, if it isn't but b is less than -5 then print "b", else print "c"

if b != 10:
    print("a")
elif b < -5:
    print("b")
else:
    print("c")

# if the string "potato" is not a substring of "I like potatoes" then print "he didn't mention potatoes", else print "he mentioned potatoes"

if "potato" not in "I like potatoes":
    print("he didn't mention potatoes")
else:
    print("he mentioned potatoes")

# end advanced conditional examples'''
