my_cat = "  Sherlock  "

print(my_cat)		   # => "  Sherlock  "
print(my_cat.rstrip()) # => "  Sherlock"
print(my_cat.lstrip()) # => "Sherlock  "
print(my_cat.strip())  # => "Sherlock"

print(my_cat) # rstrip, lstrip, and strip are non-mutating
my_cat = my_cat.strip()
print(my_cat) # reassignment allows us to save string sans whitespace