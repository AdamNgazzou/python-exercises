
def init_students(student,number_students):
    for i in range(number_students):
        x = input(f" Enter the name of student {i + 1}: ")
        student.append(x)

def init_courses(course,number_courses):
    for i in range(number_courses):
        x = input(f" Enter the name of course {i + 1}: ")
        course.append(x)

def init_grades(grade,course,student,number_courses,number_students):
    for i in range(number_students):
        grade_entry = {"student": student[i], "mark": []}
        print(f"\n 🌟Enter marks for {student[i]}: ")
        for j in range(number_courses):
            midterm = float(input(f" Enter {student[i]}'s midterm mark for {course[j]}: "))
            final = float(input(f" Enter {student[i]}'s final exam mark for {course[j]}: "))
            
            new_course = {
                "course": course[j],
                "midterm": midterm,
                "final": final,
                "final_grade": (midterm * 0.3) + (final * 0.7)
            }
            grade_entry["mark"].append(new_course)
        grade.append(grade_entry)
            
def final_score(student, grade, number_students,number_courses, mo3adlet):
    print("\n 📚Final Grades:")
    for i in range(number_students):
        mo3adel = 0
        # Find the course marks for the student
        for mark_entry in grade[i]["mark"]:
            mo3adel += mark_entry["final_grade"]
        mo3adel /= number_courses
        mo3adlet.append({"student": student[i], "Grade": mo3adel})
        print(f" {student[i]}: {mo3adel}")

def bubble_sort(mo3adlet,number_students):
    n = number_students
    # Traverse through all elements in mo3adlet
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
            if mo3adlet[j]["Grade"] < mo3adlet[j + 1]["Grade"]:
                mo3adlet[j], mo3adlet[j + 1] = mo3adlet[j + 1], mo3adlet[j]


def statistic(mo3adlet,number_students):
    bubble_sort(mo3adlet,number_students)
    student = "student"
    Grade = "Grade"
    average = 0
    print("\n 📊 LeaderBoard")
    for i in range(number_students) : 
        print(f" 🏆 Top {i+1} Student: {mo3adlet[i][student]} with a mo3adel of {mo3adlet[i][Grade]}")
        
        average += mo3adlet[i][Grade]
    print(f" 📉 Worst Student: {mo3adlet[number_students - 1][student]} with a mo3adel of {mo3adlet[number_students - 1][Grade]}")
    
    print(f" 🎯 Class Average: {average/number_students}")

def search_student(grade,number_students,searched_student):
    course = "course"
    print(" 📜 med's Grades:")
    for i in range (number_students) : 
        if searched_student==grade[i]["student"]:
            for mark in grade[i]["mark"]:
                print(f"{mark[course]} : {mark['final_grade']}")
            break
        
def main():
    #student initialisation and adding
    number_students = int(input("Enter the number of students: "))
    student = []
    init_students(student,number_students)
    
    #course initialisation and adding
    course = []
    number_courses = int(input("\nEnter the number of courses: "))
    init_courses(course,number_courses)
    
    #grading initialisation and adding
    grade = []
    init_grades(grade,course,student,number_courses,number_students)
    
    #final Grades 
    mo3adlet = []
    final_score(student, grade, number_students,number_courses, mo3adlet)
    
    #statistics
    statistic(mo3adlet,number_students)
    
    #search student
    searched_student = input("\nEnter a student's name to see their grades: ")
    search_student(grade,number_students,searched_student)
    
main()
        
    