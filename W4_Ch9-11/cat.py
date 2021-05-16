class Cat:
    """A very basic model of a cat."""
    
    def __init__(self, name, favorite_toy):
        """Initialize name and favorite toy attributes."""
        self.name = name
        self.__favorite_toy = favorite_toy

    def show_favorite_toy(self):
      """Return favorite toy attribute value."""
      return self.__favorite_toy
