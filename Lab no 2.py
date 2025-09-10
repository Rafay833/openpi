#A hospital records Heart rate of a patient. Daily for the month of January .
#Take input in array .
#Display lowest and highest heart rate.
#Display average heart rate.
#Display the Days on which heart rate was abnormal (less than 60 or greater than 100).
Heart_Rate = []
print("Enter the Heart Rate for each day of January:")
for i in range(4):
    hr = int(input("Enter Heart Rate: "))
    Heart_Rate.append(hr)
lowest = 0
for i in range(4):
    if Heart_Rate[i] < Heart_Rate[lowest]:
        lowest = i
print("Lowest Heart Rate:", Heart_Rate[lowest], "on day", lowest + 1)
highest = 0
for i in range(4):
    if Heart_Rate[i] > Heart_Rate[highest]:
        highest = i
print("Highest Heart Rate:", Heart_Rate[highest], "on day", highest + 1)
Sum = 0
for x in Heart_Rate:
    Sum += x
avg = Sum / 4
print("Average Heart Rate:", avg)
print("Days with abnormal Heart Rate (less than 50 or greater than 120):")
for i in range(4):
    if Heart_Rate[i] < 50 or Heart_Rate[i] > 120:
        print("Day", i + 1, "with Heart Rate:", Heart_Rate[i])
        break
else:
    print("No abnormal Heart Rate recorded.")
#A city records daily temperature of a week.
#Take input in array.
# Display lowest and highest temperature.
#Display average temperature.
# Display the Days on which temperature was above average.       
Days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
Temp = []
print("Enter the temperature for each day:")
for i in range(7):
    t = int(input("Enter temp: "))
    Temp.append(t)
min_index = 0
for i in range(7):
    if Temp[i] < Temp[min_index]:
        min_index = i
print("Coldest day:", Days[min_index], Temp[min_index])
max_index = 0
for i in range(7):
    if Temp[i] > Temp[max_index]:
        max_index = i
print("Hottest day:", Days[max_index], Temp[max_index])
total = 0
for x in Temp:
    total += x
avg = total / 7
print("Average temperature:", avg)
print("Days with temperature above average:")
for i in range(7):
    if Temp[i] > avg:
        print(Days[i])
        break
else:
    print("No day had temperature above average.")
#A cinema recordno of tickets sold in a week price of ticket is 1000.
# input value from user  in  an array.
#Display the day with highest tickets sales.
#calculate the total amount collected in a week.
#display the Day having exactly 50 no of tickets sold.
Days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
TicketsSold = []
print("Enter the number of tickets sold for each day:")
for i in range(7):
    tickets= int(input("Enter tickets sold: "))
    TicketsSold.append(tickets)
highest = 0
for i in range(7):
    if TicketsSold[i] > TicketsSold[highest]:
        highest = i
print("Day with highest ticket sales:", Days[highest], TicketsSold[highest])
totaltickets = 0
for x in TicketsSold:
    totaltickets += x
print("Total tickets sold in the week:", totaltickets)
totalamount = totaltickets * 1000
print("Total amount collected in the week: Rs.", totalamount)
print("Days with exactly 50 tickets sold:")
for i in range(7):
    if TicketsSold[i] == 50:
        print(Days[i])
        break
else:
    print("No day had exactly 50 tickets sold.")
#Develop a course register system.For students max 10 students can register 
#store the name and CNIC of student registered in the course.
#User should press 1 for register new student
#User should press 2 to delete student by CNIC
#User should press 3 to display all students
#keep repeating until the User should press 4 to exit
Students = []
while True:
    print("1. Register new student")
    print("2. Delete student by CNIC")
    print("3. Display all students")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        if len(Students) < 10:
            name = input("Enter student name: ")
            cnic = input("Enter student CNIC: ")
            Students.append({"name": name, "cnic": cnic})
            print("Student registered successfully.")
        else:
            print("Registration full. Cannot register more students.")
    elif choice == 2:
        cnictodelete = input("Enter CNIC of student to delete: ")
        for i in Students:
            if i["cnic"] == cnictodelete:
                Students.pop(i)
                print("Student deleted successfully.")
                break
        else:
            print("Student with given CNIC not found.")
    elif choice == 3:
        if Students:
            print("Registered students:")
            for i in Students:
                print("Name:", i["name"], ", CNIC:", i["cnic"])
        else:
            print("No students registered.")
    elif choice == 4:
        print("Exiting the system.")
        break
    else:
        print("Invalid choice. Please try again.")
#Develop a course register system.For students max 10 students can register 
#store the name and CNIC of student registered in the course.
#User should press 1 for register new student
#User should press 2 to delete student by CNIC
#User should press 3 to display all students
#keep repeating until the User should press 4 to exit
class Student:
    def __init__(self, name, cnic):
        self.name = name
        self.cnic = cnic

Students = []
while True:
    print("1. Register new student")
    print("2. Delete student by CNIC")
    print("3. Display all students")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        if len(Students) < 10:
            name = input("Enter student name: ")
            cnic = input("Enter student CNIC: ")
            Students.append(Student(name, cnic))
            print("Student registered successfully.")
        else:
            print("Registration full. Cannot register more students.")
    elif choice == 2:
        cnictodelete = input("Enter CNIC of student to delete: ")
        for idx, student in enumerate(Students):
            if student.cnic == cnictodelete:
                Students.pop(idx)
                print("Student deleted successfully.")
                break
        else:
            print("Student with given CNIC not found.")
    elif choice == 3:
        if Students:
            print("Registered students:")
            for student in Students:
                print("Name:", student.name, ", CNIC:", student.cnic)
        else:
            print("No students registered.")
    elif choice == 4:
        print("Exiting the system.")
        break
    else:
        print("Invalid choice. Please try again.")

#Develop a course register system.For students max 10 students can register 
#store the name and CNIC of student registered in the course.
#User should press 1 for register new student
#User should press 2 to delete student by CNIC
#User should press 3 to display all students
#keep repeating until the User should press 4 to exit
class Student:
    def __init__(self, name, cnic):
        self.name = name
        self.cnic = cnic
Students = []
while True:
    print("1. Register new student")
    print("2. Delete student by CNIC")
    print("3. Display all students")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        if len(Students) < 10:
            name = input("Enter student name: ")
            cnic = input("Enter student CNIC: ")
            Students.append(Student(name, cnic))
            print("Student registered successfully.")
        else:
            print("Registration full. Cannot register more students.")
    elif choice == 2:
        cnictodelete = input("Enter CNIC of student to delete: ")
        for idx, student in enumerate(Students):
            if student.cnic == cnictodelete:
                Students.pop(idx)
                print("Student deleted successfully.")
                break
        else:
            print("Student with given CNIC not found.")
    elif choice == 3:
        if Students:
            print("Registered students:")
            for student in Students:
                print("Name:", student.name, ", CNIC:", student.cnic)
        else:
            print("No students registered.")
    elif choice == 4:
        print("Exiting the system.")
        break
    else:
        print("Invalid choice. Please try again.")