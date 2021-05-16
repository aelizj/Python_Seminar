# class Building:
#     """A class modeling a building at a basic level."""

#     def __init__(self, name, address):
#         """Initialize name and type attributes."""
#         self.name = name
#         self.address = address

#     def get_building_description(self):
#         """Return formatted description of a building."""
#         desc = f"Name: {self.name}\nAddress: {self.address}\n"
#         return desc

# class ApartmentBuilding(Building):
#     """Class modeling an apartment building."""
#     # def __init__(self):
#     #     """Initialize apartment building."""

#     # def print_hello(self):
#     #     return "hello"

# # ---------------
# building = Building("Empire State Building", "an address")
# print(building.get_building_description())

# apt = ApartmentBuilding("Apartment Building", "123 Address Street")
# # print(apt.print_hello())
# print(apt.get_building_description())



# do you have to list attrs in child class too?? 



# class Building:
#     """A class modeling a generic building."""
    
#     def __init__(self, name, address):
#         """Initialize name and address attributes."""
#         self.name = name
#         self.address = address
        
#     def get_description(self):
#         """Return a formatted description."""
#         description = f"Name: {self.name}\nAddress: {self.address}"
#         return description

# my_building = Building("building", "123 Address")


# clone_army_barracks = Building("Building of Annes", "123 Anne Street") 
# print(clone_army_barracks.get_description())


# class PersonalComputer:
#     """A model of a personal computer."""
#     pass

# class WorkComputer:
#     """A model of a work computer."""
#     pass

# class Laptop(PersonalComputer, WorkComputer):
# #     """A model of a laptop."""
# #     pass
# class Location:
#     """Models a specific geographic location.""" 
#     def __init__(self, address):
#         """Initialize address attribute."""
#         self.address = address

#     def get_coordinates(self):
#         """Given an address, return corresponding GPS coordinates."""
#         pass

# class Origin(Location):
#     """Models an origin location."""

#     def __init__(self, address):
#         """Initialize address attribute."""
#         super().__init__(address)

#     def ask_home_address(self):
#         """Ask user whether entered origin is user's home address."""
#         pass

# class Destination(Location):
#     """Models a destination location."""
    
#     def __init__(self, address):
#         """Initialize address attribute."""
#         super().__init__(address)


# class Route:
#     """Model of a navigational route from an origin to a destination."""
    
#     def __init__(self, origin, destination):
#         """Initialize origin and destination coordinates."""
#         self.origin = Origin(origin)
#         self.destination = Destination(origin)

#     def print_endpoints(self):
#         orig = f"Origin: {self.origin}\nDestination: {self.destination}"
#         return orig


# route = Route("123 Oak Street", "456 Pine Street")
# print(route.print_endpoints())






# # dishware.py
# class Plate:
#     """Model of a plate of the sustenance-carrying variety."""
#     def __init__(self, color, radius):
#         """Initialize radius and color attributes."""
#         self.color = color
#         self.radius = radius

# class DinnerPlate(Plate):
#     """Model of a dinner plate."""
    
#     def __init__(self, radius, weight, color = "yellow"):
#         """Initialize radius and color attributes."""
#         super().__init__(color, radius)
#         self.weight = weight

#     def describe(self):
#        str = f"{self.color}\n{self.radius}\n{self.weight}"
#        return str

# p = DinnerPlate(7, 4)
# print(p.describe())


# class Cat:
#     """A very basic model of a cat."""
    
#     def __init__(self, name, favorite_toy, age):
#         """Initialize name and favorite toy attributes."""
#         self.name = name
#         self.favorite_toy = favorite_toy
#         self.age = age
      
#     def cat_birthday(self):
#         """Increments age attribute by one."""
#         self.age += 1
        

# sherlock = Cat("Sherlock", "wiggly fish", 5)

# print(sherlock.favorite_toy) # => wiggly fish
# sherlock.favorite_toy = "rattle mouse"
# print(sherlock.favorite_toy) # rattle mouse

# print(sherlock.age) # => 5
# sherlock.cat_birthday()
# print(sherlock.age) # => 6





