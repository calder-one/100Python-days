# 🚨 Don't change the code below 👇
row1 = ["1","2","3"]
row2 = ["4","5","6"]
row3 = ["7","8","9"]
map= [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

col = int(position[0])
row = int(position[1])

mark_row = map[row - 1] 
mark_row[col - 1] = "X" # Final mark for column within row/list

print(f"{row1}\n{row2}\n{row3}")

# ['X', '2', '3']
# ['4', '5', '6']
# ['7', '8', '9']