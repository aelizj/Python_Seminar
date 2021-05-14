class Meal:
  """A class modeling a generic meal."""
  def __init__(self, name, type, calorie_count):
    """Initialize name, type, and calorie count."""
    self.name = name
    self.type = type
    self.calorie_count = calorie_count

  def print_description(self):
    """Print formatted description of a meal object."""
    description = f"Name {self.name}\nMeal Type:{self.type}\nCalorie Count: {self.calorie_count}"
    return description

  
class Dinner(Meal):
  """A class modeling a dinner object."""

class Breakfast(Meal):
  """A class modeling a breakfast object."""