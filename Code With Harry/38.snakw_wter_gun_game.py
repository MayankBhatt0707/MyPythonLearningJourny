import random
rand_no = random.randint(1,3)
if rand_no == 1:
    choise1 = "Snake"
elif rand_no == 2:
    choise1 = "Water"
else:
    choise1 = "Gun"




def snake_water_gun(choise1, choise2):
    if choise1 == "Snake" and choise2 == "Water":
        return "Snake drinks water and Computer wins"
    elif choise1 == "Water" and choise2 == "Snake":
        return "Snake drinks water and You win"
    elif choise1 == "Gun" and choise2 == "Snake":
        return "Gun Kills snake and Comp wins"
    elif choise1 == "Snake" and choise2 == "Gun":
        return "Gun Kills snake and You win"
    elif choise1 == "Water" and choise2 == "Gun":
        return "Gun drowns and Comp wins"
    elif choise1 == "Gun" and choise2 == "Water":
        return "Gun drowns and You win"
    else:
        return "It's a tie"

choise2 = input("Your Turn: What do you choose? ")
print(f"Computer Chose: {choise1}")
print(snake_water_gun(choise1, choise2))    