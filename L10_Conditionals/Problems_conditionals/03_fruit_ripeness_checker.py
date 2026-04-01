# problem= determine if a fruit is ripe, overripe, or unripe based on its color.(eg. banana:grean-unripe, yellow-ripe, brown-overripe)
fruit = input("Enter the fruit name: ")
color = input("Enter the color of the fruit: ")
if color == "green":
    color = color.upper()
    print(f"The {fruit} is unripe.")
elif color == "yellow":
    color = color.upper()
    print(f"The {fruit} is ripe.")
elif color == "brown":
    color = color.upper()
    print(f"The {fruit} is overripe.")
else:
    print("Invalid color input.")