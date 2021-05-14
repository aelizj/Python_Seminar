message = "If I had a salamander I'd name them Antonio."
print(message)

message = "I do not have a salamander."
print(message)

# SPlitting a string
word = "hello"
chars_1 = list(word)
chars_2 = [char for char in word]

print(chars_1)
print(chars_2)

# Joining a string
chars = list('hello')
word = "".join(chars)
print(word)

#Iterating over a list with index
arr = [1, 2, 3, 4]
for idx, val in enumerate(arr):
	print(f"{idx} => {val}")


# Mapping though a collection
arr = [1, 2, 3, 4]

def double(num):
	return num * 2

doubles = list(map(double, arr))
# map needs a function to call on each element in order to transform it

doubles = list(map(lambda num: num * 2, arr))

print(doubles)

# Filtering - calling this function similar to calling map function