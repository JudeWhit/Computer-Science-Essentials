print("Welcome to the Letter Grade Calculator")
print("This calculator calculates your grade")
pointsEarned=input("Enter points earned: ")
pointsPossible=input("Enter points possible: ")
grade=(int(pointsEarned)/int(pointsPossible)*(100))
if grade >= (90):
    print("Grade: A")
    print(float(grade),"%")
elif grade >= (80):
    print("Grade: B")
    print(float(grade), "%")
elif grade >= (70):
    print("Grade: C")
    print(float(grade), "%")
elif grade >= (60):
    print("Grade: D")
    print(float(grade), "%")
elif grade >= (0):
    print("Grade: F")
    print(float(grade), "%")
else:
    print("Invalid percentage, please try again")
