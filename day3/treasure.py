first = input('You are alone in a forest and find some food. You see some berries in the distance and some mushrooms near by.\
  Do you go for the berries or for the mushrooms. Type "berries" or "mushrooms" \n').lower()
if first == "berries":
    second = input("You have come to a small cabin with a canoe near the river. Type 'canoe' or 'stay' to continue\n").lower()
    if second == "canoe":
        third = input("Great. You escaped the wild fire. You made it down river and got to a town. You found a church with tree doors. Pick 'red', 'blue', or 'black' door \n").lower()
        if third == "black":
            print("You have made it. Your treasure awaits behind this door.")
        elif third == "red" or third == "blue":
            print("Wrong door. Gave Over")
        else:
            print("You can't read instructions.")
    elif second == 'stay':
        print("You got caught in a wild fire. Game Over")
    else:
        print("Not a choice.")
elif first == "mushrooms":
    print("Those were terrible mushrooms. You died")
else:
    print("Try again")