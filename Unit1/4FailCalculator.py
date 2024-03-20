print("Welcome to the fail calculator")
print("This calculator calculates if you passed or failed")
pointsEarned=input("Enter points earned: ")
pointsPossible=input("Enter points possible: ")
grade=(int(pointsEarned)/int(pointsPossible)*(100))
if grade >= (60):
    print("You passed!")
    print((grade), "%")
elif grade >= (0):
    print("You failed")
    print(float(grade), "%")
else:
    print("Invalid Grade, please try again")
