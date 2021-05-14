# cat = "Sherlock"
# cat == "Sherlock"

# print(5 > 4 and 6 > 5)
# print(5 > 4 or 6 > 12)

# requested_toppings = ["pepperoni", "olives", "tomatoes"]

# for topping in requested_toppings:
# 	if topping == "olives":
# 		print("Sorry, we're out of olives!")
# 	else:
# 		print(f"Adding {topping} to your pizza!")

# things = []

# if things:
#   print("Things is a thing")
# else:
#   print("An empty array evaluates to false")




# EXERCISES
# 5-1 ------------------------------------------------
# cat = "Sherlock"
# colors = ["red", "blue"]

# print(cat == "Sherlock")
# print(cat != "SHERLOCK")
# print(cat.lower() == "sherlock")
# print(5 <= 4)
# print(6 >= 12)
# print(4 > 5)
# print(5 < 9)
# print(5 != 5)
# print(4 == 4)
# print("blue" not in colors)
# print("green" in colors)
# print("sherlock" == "Sherlock" or 4 > 3)
# print(4 == 4 and 6 > 3)


# # 5-3 ------------------------------------------------
# alien_color = "red"

# if alien_color == "green":
#   print("You just earned 5 points!")

# if alien_color != "green":
#   print("You just earned 10 points!")


# # 5-4 ------------------------------------------------
# if alien_color == "green":
#   print("You just earned five points!")
# else:
#   print("You just earned ten points!")

# if alien_color != "green":
#   print("You've just earned ten points!")
# else:
#   print("You've just earned five points!")  


# 5-5 ------------------------------------------------
# if alien_color == "green":
#   print("You just earned five points!")
# elif alien_color == "yellow":
#   print("You just earned ten points!")
# else:
#   print("You just earned fifteen points!")

# if alien_color == "red":
#   print("You've just earned fifteen points!")
# elif alien_color == "green":
#   print("You've just earned five points!")
# else:
#   print("You've just earned ten points!")

# if alien_color == "yellow":
#   print("You've just earned ten points!")
# elif alien_color == "green":
#   print("You've just earned five points!")
# else:
#   print("You've just earned ten points!")


# 5-8 ------------------------------------------------
usernames = ["admin", "anne", "max", "sherlock", "greycat"]
new_users = ["greycat", "browntabby", "yourneighborhoodficus", "zumbazealot33", "sherlock"]

if usernames:
  for username in usernames:
    if username == "admin":
      print("Hello admin! Would you like to see a status report?")
    else:
      print(f"Hello {username.title()}, good to see you!")
else:
  print("We need to find some users!")

for new_user in new_users:
  if new_user in usernames:
    print(f"Sorry, the username {new_user} is taken!")
  else:
    print(f"Welcome aboard, {new_user}!")


# 5-9
