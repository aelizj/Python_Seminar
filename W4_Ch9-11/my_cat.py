# from cat import Cat 

# sherlock = Cat("Sherlock", "wiggly fish", 5)
# print(sherlock.show_favorite_toy()) # => wiggly fish

# sherlock._Cat__favorite_toy = "rattle mouse"
# print(sherlock.show_favorite_toy()) # => rattle mouse

class Speak:
  """Model of speaking."""
 
  def __init__(self, word):
    """Initialize word attribute."""
    self.word = word

  def speak(self):
    """Print out word attribute."""
    print(self.word)


class Shout(Speak):
  """Model of shouting."""
  
  def __init__(self, word):
    """Initialize word attribute via superclass."""
    super().__init__(word)
  
  def speak(self):
    """Print uppercase word attribute."""
    print(self.word.upper())

yell = Shout("Hi there!")
yell.speak()