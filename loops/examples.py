'''# start list of definitions
range(int n) - iterates over all numbers from 0 to n (not including n)
range(int a, int b, int c) - iterates over all numbers from a to b (not including b), each time increasing by c
	if c is negative then range counts backwards
# end list of definitions'''

'''# start while loop example

# prints a variable i and increases it while it's less than 10

i = 0
while i < 10:
	print("i is "+str(i)+" which is less than 10!")
	i += 1 # this increases i

# end while loop example'''

'''# start for loop example
# iterating over a list of random words

thingsILike = ["potatoes", "hair", "Dobby", "Dr. Mantis Toboggan MD"]

for a in thingsILike:
	print("I like "+a)
# end for loop example'''

'''# start for loop example

# iterating over the numbers from 0 to 9

for n in range(10):
	print("you will see this printed 10 times!")
# end for loop example '''

'''# start for loop example

# iterating over the numbers 1 to 100 with increments of 2

for cat in range(1, 100, 2):
	print(str(cat) + " is an even number less than 100")

# end for loop example'''

''' # start for loop example

# iterating over the numbers from 1 to 100 backwards

for tac in range(100, 0, -1):
	print(str(tac) + " is part of a backwards sequence of numbers from 100 to 1")

# end for loop example'''
