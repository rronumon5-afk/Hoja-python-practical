
from sqlalchemy import Result


def get_marks():
    marks ={}
    marks["English"]=int(input("Enter marks for English:"))
    marks["Maths"]=int(input("Enter marks for Maths:"))
    marks["Science"]=int(input("Enter marks for Science:"))
    marks["Social"]=int(input("Enter marks for Social:"))
    marks["Computer"]=int(input("Enter marks for Computer:"))
    return marks

def calculate_total(marks):
    print(marks.values())
    return sum(marks.values())

def calculate_average(total):
    return total/5

def find_grade(average):
    if 90 <= average<= 100:
        return "A+"
    elif 80 <= average < 90:
        return "A"
    elif 70 <= average < 80:
        return "B"
    elif 60 <= average < 70:
        return "C"
    elif 50 <= average < 60:
        return "D"
    else:
        return "Fail"
    
    
    
marks = get_marks()
Total = calculate_total(marks)
Average = calculate_average(Total)
Grade = find_grade(Average)

print("\n---Results---")
print(f"Total Marks: {Total}")
print(f"Average Marks: {Average:.2f}")
print(f"Grade: {Grade}")
print(f"Result: {Result}")






    
    
