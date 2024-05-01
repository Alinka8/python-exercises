mood =input("What is your mood? ")
weather = input("How is the weather? ")

if mood == "happy":
    if weather == "sunny":
       print("You should watch comedy")
    else:
       print("You should watch romantic")
elif mood == "sad":
    print("You should watch drama")
else:
    print("You should watch Adventure")

