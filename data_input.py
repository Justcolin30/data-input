# function to take data inputs
def data_input():
    student_data = []

    for st in range(3):
        ind_student_data = []
        course_score = []
        st_name = input("Name of Student: ")
        ind_student_data.append(st_name)
        print(" ")
        print("--------------------------------------------------------------")
        print(f"Data for {st_name}")
        print("----------------------------------------------------------------")

        for stc in range(0, 4):
            ind_course_data = []
            st_course = input("Course: ")
            ind_course_data.append(st_course)

            st_course_score = input(f"Marks for {st_course}: ")
            ind_course_data.append(st_course_score)
            print(" ")

            course_score.append(ind_course_data)
        ind_student_data.append(course_score)
        student_data.append(ind_student_data) 

    print("---------------------------------------------------------------------------")
    #print(student_data)
    return student_data

    def determining_grade ( grade) :      
      if grade >= 85 :
        return "A"
      elif grade >= 74 :
       return "B"
      elif grade >= 50 :
        return "C"
      elif grade <= 50 :
        return "D"
      else :    
        return "F"        

    # Get and validate marks for the course
    while True:
        try:
            st_course_score = int(input(f"Marks for {st_course}: "))
            if st_course_score < 0 or st_course_score > 100:
              print("Invalid marks. Please enter a value between 0 and 100")
            else:
                break
        except ValueError:
                print("Invalid input. Please enter a numerical value.")

        grade = decision(st_course_score)


def display_data(student_data):

    print("\n-----------------------------------------")
    print("Student Data Summary")
    print("---------------------------------------------")

    for student in student_data:
        name = student[0]
        courses = student[1]

        print(f"\nStudent Name: {name}")

        # Table header with spacing for better readability
        print(" | Course        | Score | Grade |")
        print(" |---------------|-------|-------|")

        for course in courses:
            course_name = course[0]
            course_score = course[1]
            course_grade = course[2]
            print(F"  | {course_name:<14} | {course_score:^4} | {course_grade:^4} |")    


student_data = data_input()
display_data(student_data=student_data)