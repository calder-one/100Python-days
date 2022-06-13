#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to tip calculator.\n")
bill = float(input("What was the total bill? "))
tip_amount = int(input("What percentage would you like to give? 10, 12 or 15 "))
people = int(input("How many people are splitting the bill? "))

total_with_tip = bill + tip_amount * bill / 100 
per_person = round(total_with_tip / people, 3)
total_per = "{:.2f}".format(per_person)
print(f"Each person owes: ${total_per}")