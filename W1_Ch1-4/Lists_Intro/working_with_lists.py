pizzas = ["pepperoni", "cheese", "italian"]

# for loop syntax
for pizza in pizzas:
	print(f"I love {pizza} pizza!")

print(f"I love {pizzas[0]} pizza!\nI love {pizzas[1]} pizzas!\nI love {pizzas[2]} pizzas!\nI LOVE pizza!!!")

# the last value that `pizza` was assigned to is still available outside the loop - weird that this isn't out of scope
print(pizza) # => italian
print()

animals = ["leopard", "cow", "dalmation"]

for animal in animals:
	print(f"{animal.title()}s have spots!")

print("All of these animals have spots!")
print()

# numerical lists -----------------------------------------------------------------------------------------------------
for number in range(1, 10):
	print(number)


evens = []
for number in range(0, 21, 2):
	evens.append(number)

print(evens) # => [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

evens = list(range(0, 21, 2))
print(evens)


# Simple statstics ----------------------------------------------------------------------------------------------------
numbers = list(range(1, 21))
print(numbers) 		# => [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

print(min(numbers)) # => 1
print(max(numbers)) # => 20
print(sum(numbers)) # => 210


# EXERCISES -----------------------------------------------------------------------------------------------------------
for number in range(1, 21):
	print(number)

# numbers = list(range(1, 1_000_001))

#for number in numbers:
	#print(number)

# print(sum(numbers))

odds = list(range(1, 20, 2))

for odd in odds:
	print(odd)

threes = list(range(3, 31, 3))

for three in threes:
	print(three)

cubes = []
for value in range(1, 11):
	cubes.append(value**3)

print(cubes)

cubes = [value**3 for value in range(1, 11)]
print(cubes)