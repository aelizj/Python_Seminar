immutable_numbers = (1, 2, 3, 4, 5)
print(immutable_numbers)

immutable_numbers = (6, 7, 8, 9, 10)
print(immutable_numbers)


# EXERCISES --------------------------------
immutable_foods = ("bread", "meat", "cheese", "ketchup", "lettuce")

for food in immutable_foods:
	print(food)

# immutable_foods[1] = "ham"

immutable_foods = ("bread", "ham", "swiss cheese", "ketchup", "lettuce")

for food in immutable_foods:
	print(food)
