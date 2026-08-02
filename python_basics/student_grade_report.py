# Ask the user for student information
student_name=input("ENTER YOUR NAME : ")
student_id=input("ENTER YOUR ID : ")

exam1=float (input(" Enter exam 1 score: "))
exam2=float (input(" Enter exam 2 score: "))
exam3=float (input(" Enter exam 3 score: "))


# Calculate the total and average
totalScores= exam1 + exam2 + exam3
avg= totalScores/3


# Determine the letter grade
if avg >=90: grade="A"
elif avg >=80: grade="B"
elif avg >=70: grade="C"
elif avg >=60: grade="D"
else : grade="F"


# Display the report
print("\n STUDENT GRADE REPORT :\n")
print(f"Student Name:{student_name}")
print(f"\n Student ID: {student_id}")
print(f" \n Exam Scores:\n Exam1 :{exam1} \n Exam2 :{exam2} \n Exam3 :{exam3}")
print(f"\n Results : \n  Total Score:{totalScores} \n   Average:{avg:.2f} \n  Grade: {grade}")
