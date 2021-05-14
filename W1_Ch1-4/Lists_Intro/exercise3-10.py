countries  = ["Russia", "Bhutan", "Cambodia", "Kenya", "Estonia", "Tuvalu", "Mongolia", "Denmark", "Brazil", "East Timor", "Germany"]

countries.append("Canada")
print(countries)
print(len(countries))

print(countries[2])

del countries[1]
print(countries)
print(len(countries))

countries.remove("Denmark")
print(countries)
print(len(countries))

print(sorted(countries))
print(sorted(countries, reverse=True))
print(countries)

countries.sort()
print(countries)

countries.sort(reverse=True)
print(countries)

countries.reverse()
print(countries)

countries.insert(3, "Iran")
print(countries)

countries.pop()
print(countries)
