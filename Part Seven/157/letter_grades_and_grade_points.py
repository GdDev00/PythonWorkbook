#Exercise 157: Both Letter Grades and Grade Points

A_PLUS = 4.0
A = 4.0
A_MINUS = 3.7
B_PLUS = 3.3
B = 3.0
B_MINUS = 2.7
C_PLUS = 2.3
C = 2.0
C_MINUS = 1.7
D_PLUS = 1.3
D = 1.0
F = 0

def from_letter_to_points(grade):
    points = None

    grade = grade.upper()
    if grade == "A+":
        points = A_PLUS
    elif grade == "A":
        points = A
    elif grade == "A-":
        points = A_MINUS
    elif grade == "B+":
        points = B_PLUS
    elif grade == "B":
        points = B
    elif grade == "B-":
        points = B_MINUS
    elif grade == "C+":
        points = C_PLUS
    elif grade == "C":
        points = C
    elif grade == "C-":
        points = C_MINUS
    elif grade == "D+":
        points = D_PLUS
    elif grade == "D":
        points = D
    elif grade == "F":
        points = F
    
    if points == None:
        raise ValueError
    else:
        return points

def form_points_to_letter(points):
    grade = None
    try:
        points = float(points)
        if points >= 0 and points < 0.5:
            grade = "F"
        elif points >= 0.5 and points < 1.15:
            grade = "D"
        elif points >= 1.5 and points < 1.5:
            grade = "D+"
        elif points >= 1.5 and points < 1.85:
            grade = "C-"
        elif points >= 1.85 and points < 2.15:
            grade = "C"
        elif points >= 2.15 and points < 2.5:
            grade = "C+"
        elif points >= 2.5 and points < 2.85:
            grade = "B-"
        elif points >= 2.85 and points < 3.15:
            grade = "B"
        elif points >= 3.15 and points < 3.5:
            grade = "B+"
        elif points >= 3.5 and points < 3.85:
            grade = "A-"
        elif points >= 3.85 and points < 4.0:
            grade = "A"
        elif points >= 4.0:
            grade = "A+"

        if grade == None:
            raise ValueError
        else:
            return grade
    except Exception:
        raise ValueError

def main():
    print("This program converts from letter grades to grade points and vice-versa")
    print("Insert a letter grades or grade points and it automatically show its conversion")
    
    line = input("Enter the value: ")

    while line != "":
        result = None

        try:
            result = from_letter_to_points(line)
            print("The conversion result is %s" %result)
        except Exception:
            result = form_points_to_letter(line)
            print("The conversion result is %s" %result)
        except Exception:
            print("Please enter a valid input!")

        print()
        line = input("Enter the value: ")

main()

