# Nested statements or functions of if-then or loops...
print(type(float(5)))

favourite_colour = "blue"
favourite_food = "bacon"

if favourite_colour == "blue":
    print("That's my favourite too.")
elif favourite_colour == "green":
    print("That's my second favourite colour.")
else:
    print("Not a bad colour.")

favourite_colour = "blue"
favourite_food = "bacon"

if favourite_colour == "blue":
    if favourite_food == "bacon":
        print("Food and colour, what are the odds?")
    else:
        print("That's my favourite too.")
elif favourite_colour == "green":
    if favourite_food == "bacon":
        print("Favourite food, but not colour that's a shame")
    else:
        print("That's my second favourite colour.")
else:
    if favourite_food == "bacon":
        print("Well at least we can eat together")
    else:
        print("We have nothing in common and that's so sad.")

favourite_colour = "blue"
favourite_food = "bacon"

if favourite_colour == "blue" and favourite_food == "bacon":
    print("Food and colour, what are the odds?")
if favourite_colour == "blue" and not favourite_food == "bacon":
    print("That's my favourite too.")
elif favourite_colour == "green":
    if favourite_food == "bacon":
        print("Favourite food, but not colour that's a shame")
    else:
        print("That's my second favourite colour.")
else:
    if favourite_food == "bacon":
        print("Well at least we can eat together")
    else:
        print("We have nothing in common and that's so sad.")