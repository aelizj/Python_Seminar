# Slicing a list
colors = ["red", "yellow", "blue", "green"]
print(colors[1:2]) # => ['yellow']
print(colors[:1])  # => ['red']
print(colors[:3])  # => ['red', 'yellow', 'blue']
print(colors[3:])  # => ['green']

for color in colors[:3]:
	print(f'{color}') # => red yellow blue


# Copying a list
colors_copy = colors[:]
colors_copy.append("purple")

print(colors)		# => ['red', 'yellow', 'blue', 'green']
print(colors_copy)  # => ['red', 'yellow', 'blue', 'green', 'purple']


# exercises
print(f"The first three colors are {colors[:3]}")
print(f"The first three colors are {colors[1:4]}")
print(f"The first three colors are {colors[1:]}")



