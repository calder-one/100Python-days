import random
# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
nums = len(names)
random_choice = random.randint(0, nums - 1)
payer = names[random_choice]
print(f"{payer} Will pay for the bill tonight!.")