places = ["Tokyo", "Nepal", "Amsterdam", "New Zealand", "Hong Kong"]
print(places) # => ['Tokyo', 'Nepal', 'Amsterdam', 'New Zealand', 'Hong Kong']

# Sorting a list => THIS IS PERMANENT
places.sort()
print(places) # => ['Amsterdam', 'Hong Kong', 'Nepal', 'New Zealand', 'Tokyo']

places.sort(reverse=True)
print(places) # => ['Tokyo', 'New Zealand', 'Nepal', 'Hong Kong', 'Amsterdam']

# Sorting a list temporarily
places = ["Tokyo", "Nepal", "Amsterdam", "New Zealand", "Hong Kong"]
print(places) 			# => ['Tokyo', 'Nepal', 'Amsterdam', 'New Zealand', 'Hong Kong']
print(sorted(places))	# => ['Amsterdam', 'Hong Kong', 'Nepal', 'New Zealand', 'Tokyo']

print(places)						# => ['Tokyo', 'Nepal', 'Amsterdam', 'New Zealand', 'Hong Kong']
print(sorted(places, reverse=True)) # => ['Tokyo', 'New Zealand', 'Nepal', 'Hong Kong', 'Amsterdam']
print(places)						# => ['Tokyo', 'Nepal', 'Amsterdam', 'New Zealand', 'Hong Kong']



# Reversing order => PERMANENT
print(places) 	 # => ['Tokyo', 'Nepal', 'Amsterdam', 'New Zealand', 'Hong Kong']
places.reverse()
print(places) 	 # => ['Hong Kong', 'New Zealand', 'Amsterdam', 'Nepal', 'Tokyo']


# Determining list length
print(places) 	   # => ['Hong Kong', 'New Zealand', 'Amsterdam', 'Nepal', 'Tokyo']
print(len(places)) # => 5



# EXERCISES ---------------------------------------------------------------------------
places = ["Tokyo", "Nepal", "Amsterdam", "New Zealand", "Hong Kong"]

print(places)
print(sorted(places))
print(places)
print()

print("HIYO")

print(sorted(places, reverse=True))
print(places)
print()

places.reverse()
print(places)
print()

places.reverse()
print(places)
print()

places.sort()
print(places)
print()

places.sort(reverse=True)
print(places)
print()

dinnerparty_guests = ["Barack Obama", "Marie Curie", "Edgar Allen Poe"]
print(len(dinnerparty_guests)) # => 3
