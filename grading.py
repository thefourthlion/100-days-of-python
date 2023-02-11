student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}

for student in student_scores:
    score = student_scores[student]
    if(score > 90):
        student_grades[student] = "Outstanding"
        print(f"{student} did Outstanding.")
    elif(score > 80):
        student_grades[student] = "Exceeds Expectations"
        print(f"{student} Exceeds Expectations.")
    elif(score > 70):
        student_grades[student] = "Acceptable"
        print(f"{student} score is Acceptable.")
    elif(score < 70):
        student_grades[student] = "Fail"
        print(f"{student} score is a Fail")
    
print(student_grades)