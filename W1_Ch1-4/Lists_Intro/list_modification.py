# List modification through indexed reassignment
dinnerparty_guests = ["Barack Obama", "Marie Curie", "Edgar Allen Poe"]
dinnerparty_guests[2] = "Siddhartha Mukherjee"

print(dinnerparty_guests) # => ['Barack Obama', 'Marie Curie', 'Siddhartha Mukherjee']

# Adding elements to a list
dinnerparty_guests.append("Edgar Allen Poe")
print(dinnerparty_guests) # => ['Barack Obama', 'Marie Curie', 'Siddhartha Mukherjee', 'Edgar Allen Poe']

# Inserting items into a list
dinnerparty_guests.insert(1, "Alfred Hitchcock")
print(dinnerparty_guests) # => ['Barack Obama', 'Alfred Hitchcock', 'Marie Curie', 'Siddhartha Mukherjee', 'Edgar Allen Poe']

# Deleting items at specific index
del dinnerparty_guests[4]
print(dinnerparty_guests) # => ['Barack Obama', 'Alfred Hitchcock', 'Marie Curie', 'Siddhartha Mukherjee']
# **removed value cannot be accessed after del is used

# Deleting items with pop() - removed value can be used after it's popped
popped_guest = dinnerparty_guests.pop()
print(dinnerparty_guests) # => ['Barack Obama', 'Alfred Hitchcock', 'Marie Curie']
print(popped_guest) 	  # => Siddhartha Mukherjee

dinnerparty_guests.pop(1)
print(dinnerparty_guests) # => ['Barack Obama', 'Marie Curie']

# Removing an item by value
dinnerparty_guests.remove("Marie Curie")
print(dinnerparty_guests) # => ['Barack Obama']



# CHAPTER 3 LIST MODIFICATION EXERCISES ---------------------------------------------------------------------------------------
dinnerparty_guests = ["Barack Obama", "Marie Curie", "Edgar Allen Poe"]

print()
print(f"Please come to my dinner party, {dinnerparty_guests[0]}.")
print(f"Please come to my dinner party, {dinnerparty_guests[1]}.")
print(f"Please come to my dinner party, {dinnerparty_guests[2]}.")
print()

print(f"{dinnerparty_guests[-1]} can't make it.")
print()

dinnerparty_guests.insert(-1, "Siddhartha Mukherjee")

print(f"Please come to my dinner party, {dinnerparty_guests[0]}.")
print(f"Please come to my dinner party, {dinnerparty_guests[1]}.")
print(f"Please come to my dinner party, {dinnerparty_guests[2]}.")
print()

print("Hey everyone, I found a bigger dinner table for the dinner party.")
print()

dinnerparty_guests.insert(0, "Albert Einstein")
dinnerparty_guests.insert(2, "Alfred Hitchcock")
dinnerparty_guests.insert(-1, "Joe Biden")

print(f"Please come to my dinner party, {dinnerparty_guests[0]}.")
print(f"Please come to my dinner party, {dinnerparty_guests[1]}.")
print(f"Please come to my dinner party, {dinnerparty_guests[2]}.")
print(f"Please come to my dinner party, {dinnerparty_guests[3]}.")
print(f"Please come to my dinner party, {dinnerparty_guests[4]}.")
print(f"Please come to my dinner party, {dinnerparty_guests[5]}.")
print()

print("Plot twist, I should have expedited the delivery on that table.. I can only invite two people.")
print()

popped_guest = dinnerparty_guests.pop()
print(f"I'm sorry {popped_guest}, there's not enough room at the table for you at my dinner party.")

popped_guest = dinnerparty_guests.pop()
print(f"I'm sorry {popped_guest}, there's not enough room at the table for you at my dinner party.")

popped_guest = dinnerparty_guests.pop()
print(f"I'm sorry {popped_guest}, there's not enough room at the table for you at my dinner party.")

popped_guest = dinnerparty_guests.pop()
print(f"I'm sorry {popped_guest}, there's not enough room at the table for you at my dinner party.")

popped_guest = dinnerparty_guests.pop()
print(f"I'm sorry {popped_guest}, there's not enough room at the table for you at my dinner party.")
print()

print(f"You're still invited to my dinner party, {dinnerparty_guests[0]}!")
print(f"You're still invited to my dinner party, {dinnerparty_guests[1]}!")
print()

del dinnerparty_guests[1]
del dinnerparty_guests[0]

print(dinnerparty_guests)
