positions=["Healing", "Invisibility", "Strength"]
favorite_potion = positions[1]
print(favorite_potion)


electric_list = ["moon","sun"]
electric_list.append("starry night")
print(electric_list)


flowers=["rose", "lily","rose","daisy", "lily"]
rose_count = flowers.count("rose")
print(rose_count)

hobbies = ["reading", "cycling","painting"]
# change the first value to writing 
# hobbies[0]="writing"
# it will insert the item
hobbies.insert(1,"dancing")
# you can remove the item
hobbies.remove("cycling")
# remove last item use pop
hobbies.pop(1)
print(hobbies)