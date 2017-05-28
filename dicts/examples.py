'''# start example
# creating a simple dict
myDict = {"a": 10}

# end example'''

'''# start example
# creating a dict of people's names and ages
namesAndAges = {
	"Joe": 10,
	"Bobby": 50,
	"Yogi": 33,
	"Jason": 25,
	"JSON": 25
}
# end example'''

'''# start example
# creating the dict above in a different way
namesAndAges = {}
namesAndAges["Joe"] = 10
namesAndAges["Bobby"] = 50
namesAndAges["Yogi"] = 33
namesAndAges["Jason"] = 25
namesAndAges["JSON"] = 25
# end example'''

'''# start example
# removing a value from a dict
myDict = {"a": 10, "b": 20}
del myDict["a"]
# end example'''

'''# start example
# iterating over a dict of people and ages to increment each age by 1
namesAndAges = {
	"Daniel": 20,
	"Greg": 32,
	"Billy": 72
}

for i in namesAndAges:
	namesAndAges[i] += 1
# end example'''
