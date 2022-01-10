# 1. TASK: print "Hello World"
print("Hello World")

# 2. print "Hello Noelle!" with the name in a variable
my_name = "Carlos"
print("Hello World", my_name)	# with a comma
print("Hello World " + my_name)	# with a +


# 3. print "Hello 42!" with the number in a variable
fav_num = 37
print("Hello", fav_num)    # with a comma
# print("Hello" + name)    # with a +	-- this one should give us an error!
print("Hello " + str(fav_num))   # conversion of a number to a string

# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "bread"
fave_food2 = "avocado"
print("I love to eat {} and {}.".format(fave_food1, fave_food2)) # with .format()
print(f"I love to eat {fave_food1} and {fave_food2}.") # with an f string



