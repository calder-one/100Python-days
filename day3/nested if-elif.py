print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
  print("You are able to ride!")
  age = int(input("What is your age? "))
  if age < 12:
    print("Please pay $5")
  elif age <= 18:
    print("Please pay $7")
  elif age >= 55:
    print("You get special senior discounted rate of $3")
  else:
    print("Please pay full admission price of $12")
else:
  print("Sorry, you need to grow some more.")