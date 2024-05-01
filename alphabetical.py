pens=["blue", "red", "black","blue","green", "red", "blue" ]
pens.sort()
blue_pens = pens.count("blue")
notebooks=["large", "medium", "small", "medium", "large"]
notebooks=len(notebooks)
print(f"Sorted pens : {pens}")
print(f"Number of blue pens: {blue_pens}")
print(f"Total number of notebooks: {notebooks}")


fruits = ["apple", "banana", "cherry", "date", "fig", "grape"]
vegetables = ["carrot", "broccoli", "spinach","potato", "onion"]

if "banana" in fruits and "carrot" in vegetables:
    print("We have them in stock")
else:
    print("They are out of stock")

first_three_fruits=fruits[:3]
print(f"The first three fruits are: {fruits}")

if "mango" in fruits:
    print("Yes, we have in stock")
else:
    print("We don't have it")