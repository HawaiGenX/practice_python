pizza = {
    "crust": "thick",
    "toppings": ["mushroom", "extra cheese"]
}
print(f"You oredered a {pizza['crust']}-crust pizza with the"
        "following toppings") # breakup the long line
for topping in pizza["toppings"]:
    print(f"\t{topping}")