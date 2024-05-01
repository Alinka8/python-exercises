weather = "sunny"
activity = "beach" if weather=="sunny" else "indoor games"
print(activity)

hours_of_day = 7
energy_level = 3
beverage = "coffee" if (6 <= hours_of_day<12) and energy_level<4 else "tea"
print(beverage)

energy_level = 4.5
time_available = 30.5
short_on_time = time_available <45.0
workout = "increase_cardio" if energy_level>4.0 and not short_on_time else "light yoga"
print(workout)

topic_difficulty = "hard"
available_hours = 3.5
understanding_level = 6

study_method = "deep dive" if topic_difficulty == "hard" and available_hours> 2.5 else "quick review" 
bonus_hours =1.5 if understanding_level<5 else 0.5
available_hours+=bonus_hours
print(study_method)
print("Total tudy hours: ", available_hours )



