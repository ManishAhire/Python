list_1 = ["ABC", "DEF", "GHI"]
print(list_1)


mix_list = ["ABC", 1, True, 1.23]
print(mix_list)

mix_list = []
print(mix_list)

vowels = "aeiou"
vowels_list = list(vowels)
print(vowels_list)


mix_list = ["ABC", 1, True, 1.23]
print(mix_list[0])
print(mix_list[2])
print(mix_list[-1])
print(mix_list[-3])

mix_list[0] = "XYZ"
print(mix_list)

mix_list.append("C")
print(mix_list)

cart = ["T-shirt", "Lamp", "Pen"]
fav_items = ["Headphones", "Phone"]

# Add all the items from fav_items to cart
cart.extend(fav_items)

print(cart)


cart.insert(2, "Book")
print(cart)

cart.remove("Book")
print(cart)

cart.pop()
print(cart)

cart.clear()
print(cart)

cart = ['T-shirt', 'Lamp', 'Pen', 'Book']
del cart[2]
print(cart)

# Delete the list itself
# del cart
# print(cart) # NameError: name 'cart' is not defined


items = ["Shirt", "Pant"]
cart = items.copy()
print(cart)

lenght = len(cart)
print(lenght)

isPreset = "Shirt" in cart
print(isPreset)

isPreset = "Book" in cart
print(isPreset)

for item in cart:
    print(item)
