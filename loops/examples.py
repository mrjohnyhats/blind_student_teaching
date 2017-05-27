'''# start list of definitions
range(int n) - iterates over all numbers from 0 to n (not including n)
range(int a, int b, int c) - iterates over all numbers from a to b (not including b), each time increasing by c
	if c is negative then range counts backwards
# end list of definitions'''

'''# start while loop example
i = 0
while i < 10:
	print("i is "+str(i)+" which is less than 10!")
	i += 1 # this indents i

# end while loop example'''

'''# start for loop example
thingsILike = ["potatoes", "hair", "Dobby", "Dr. Mantis Toboggan MD"]

for a in thingsILike:
	print("I like "+a)

for n in range(10):
	print("you will see this printed 10 times!")

for cat in range(1, 100, 2):
	print(str(cat) + " is an even number less than 100")

for tac in range(100, 0, -1):
	print(str(tac) + " is part of a backwards sequence of numbers from 100 to 1")

# end for loop example'''
