names = ["Anne", "Max", "Sherlock"]

print(names)	# => ['Anne', 'Max', 'Sherlock']

#Accessing list elements
print(names[0]) # => Anne
print(names[1]) # => Max
print(names[2]) # => Sherlock

print(f"Hi there, {names[0]}!")
print(f"Hi there, {names[1]}!")
print(f"Hi there, {names[2]}!")

transportation = ["helicopter", "unicycle"]

# Using list elements in strings
print(f"I sure enjoy commuting by {transportation[1]}.") # => I sure enjoy communting by unicycle.
print(f"Life's more fun in a {transportation[0]}!") # => Life's more fun in a helicopter!