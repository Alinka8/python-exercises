destination="Paris"
duration = 5
budget=1500
places_visit=["Eiffel Tower", "Lauvre Museum", "Notre-Dame Cathedral"]
food_try=["Croissant", "Ratatouille", "Crepe"]

itinerary=[destination,duration,budget,places_visit,food_try]
itinerary[3].append("Champs-Elysees")
itinerary[4].append("Baugette")
print(f"Destination: {itinerary[0]}")
print(f"Duration: {itinerary[1]}")
print(f"Budget: {itinerary[2]}")
print(f"Places to visit: {', '.join(itinerary[3])}")
print(f"Food to try: {',' .join(itinerary[4])}")