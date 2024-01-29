grade = int(input("Enter your grade: "))

if (grade >= 96 and grade <=100):
    print("You got an A+, Congratulations!")
elif (grade >= 91 and grade <=95):
    print("You got an A-, Congratulations!")
elif (grade >= 86 and grade <= 90):
    print("You got a B+, Wonderful!")
elif (grade >= 81 and grade <= 85):
    print("You got a B-, You did a great job!")
elif (grade >= 75 and grade <= 80):
    print("You got a C, Study Hard!")
elif (grade > 100):
    print("Invalid Input. Try again!")
else:
    print("You Failed!")