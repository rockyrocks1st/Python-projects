
#creating a dictionary with students roll numbers and their marks
stu_marks = {
    "1": 80, 
    "2": 78,
    "3": 90,
    "4": 75,
    "5": 65,
    "6": 85,
    "7": 83,
    "8": 95,
    "9": 79,
    "10": 92,
    "11": 81,
    "12": 70,
    "13": 88,
    "14": 74,
    "15": 73,
    "16": 72,
    "17": 76,
    "18": 69,
    "19": 82,
    "20": 89,
    "21": 94
    }

#creating a list of students name
stu_name = ["Aditya", "Aman", "Amit", "Ankur", "Anurag", "Avneesh", "Ayush", "Bhumi", "Brijesh", "Chirag", "Devansh", "Dhruv", "Gaurav", "Harish", "Harsh", "Ishan", "Kanika", "Komal", "Nikita", "Rohan"]

#taking input from user
roll_no = input("Enter the roll number of the student: ")

#checking if the roll number is present in the dictionary
if roll_no in stu_marks:
    #if the roll number is present, getting the index of the roll number
    index = list(stu_marks.keys()).index(roll_no)
    #printing the marks of the student
    print("Marks of", stu_name[index], "is", stu_marks[roll_no], "out of 100")
#if the roll number is not present, printing a message
else:
    print("Roll number not found")
