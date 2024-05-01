
#This program aims to teach you about arrays and the linear search function

#In this program, you have a list of items and need to find if a specific item is in that list


#example array
#an array is a list of items seperated by a ','
#you can add to, remove from, search through, find length of the list
list_of_homeroom_students = []

#The following code is called a FUNCTION. It is like a recipe and can be called unlimited times
#A function requires three things:
#1) def or define declares the start of a function
#2) name of your function. Below it is getNumStudents
#3) Parameters. these are items that are needed for the function to run
#they go in the (). The one below is empty because it does not require any parameters to run



#This function returns the length of the list
def getNumStudents():
    number_of_students_going_on_senior_trip = len(list_of_homeroom_students)
    return number_of_students_going_on_senior_trip

#This code adds a student to the list
def addStudentToList():
    print("What is the student's name?")
    name = input("->")
    new_student = name
    print(new_student, "has been added")
    list_of_homeroom_students.append(new_student)

#This function searches the list to see if a studdent is on the list and returns a 'yes' or 'no'
def searchForStudentInHomeroom(name):
    for student in list_of_homeroom_students:
        if student == name:
            print("Student is on the list")
            return
    print("Student is not on the list")
        
#This function prints the list to the terminal for viewing
def printList():
    print(list_of_homeroom_students)

#All functions are listed above the main code of the program.
    
#MAIN CODE:
#loop infinitely until you break 
while True:

    #Welcome Message and Menu of options
    print("Student Roster Maker V1.1")
    print("What would you like to do?")
    print("1: Add student to list")
    print("2: Check if a student is on the list")
    print("3: View number of students on list")
    print("4: View students on the list")
    print("5: Exit Program")
    #store their choice and go to the appropriate option below
    choice = input("->")

    if choice == "1":
        #Add Student to List
        addStudentToList()

    elif choice == "2":
        print("Who would you like to check?")
        name_choice = input("->")
        searchForStudentInHomeroom(name_choice)

    elif choice == "3":
        print(getNumStudents(), "student(s) in homeroom.")

    elif choice == "4":
        printList()

    elif choice == "5":
        break

#END OF CODE
print("Exiting")
