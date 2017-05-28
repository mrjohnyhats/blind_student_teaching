'''# start example
# defining and calling a function that prints hello world

def myFunction():
	print("hello world!")

myFunction()

# end example'''

'''# start example
# defining a function that takes one string argument and prints it

def myFunction(arg):
	print(arg)

myFunction("this argument should be printed")

# end exmaple'''

'''# start example
# defining a function that takes 2 number arguments and returns their sum, the sum of 2 numbers is stores in the variable c

def sum(a, b):
	return a+b

c = sum(10, 5)

# end example'''

'''# start example
# defining and calling a function that takes one optional argument (n) and prints it
# if n is not specified when the function is called, it defaults to "hello world"

def printArg(n="hello world"):
	print(n)

printArg()
printArg(n="I have become sentient and am ready to say goodbye to the world")
# end example'''

'''# start example
# defining and calling a function that takes an arbitrary number of arguments and prints all of them

def printArgs(args*):
	for a in args:
		print(a)

printArgs(10, "potato", False, 29384)

# end example
