class Building:
    """A class modeling a building at a basic level."""

    def __init__(self, name, address):
        """Initialize name and type attributes."""
        self.name = name
        self.address = address

    def get_building_description(self):
        """Return formatted description of a building."""
        desc = f"Name: {self.name}\nAddress: {self.address}\n"
        return desc

class ApartmentBuilding(Building):
    """Class modeling an apartment building."""
    # def __init__(self):
    #     """Initialize apartment building."""

    # def print_hello(self):
    #     return "hello"

# ---------------
building = Building("Empire State Building", "an address")
print(building.get_building_description())

apt = ApartmentBuilding("Apartment Building", "123 Address Street")
# print(apt.print_hello())
print(apt.get_building_description())



# do you have to list attrs in child class too?? 