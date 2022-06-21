
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")


#Write your code below this line 👇
both_lower = name1.lower()+name2.lower()

t = both_lower.count("t")
r = both_lower.count("r")
u = both_lower.count("u")
e = both_lower.count("e")

true_total = t + r + u + e 

l = both_lower.count("l")
o = both_lower.count("o")
v = both_lower.count("v")
e = both_lower.count("e")

love_total = l + o + v +e
total = str(true_total) + str(love_total)
int_total = int(total)

if int_total < 10 or int_total > 90:
    print(f"Your love score is {int_total}, you go together like coke and mentos")
elif int_total <=50 and int_total >=40:
    print(f"Your score is {int_total}, you are alright together.")
else:
    print(f"Your score is {int_total}.")