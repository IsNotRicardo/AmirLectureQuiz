grades = []
value = int(input("Insert a number: "))

while value != -1:
    if 0 <= value <= 100:
        grades.append(value)
    else:
        print("Invalid grade.")
    value = int(input("Insert a number: "))

print("The smallest number is:", min(grades), '\n' +
      "The largest number is:", max(grades))