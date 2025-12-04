# n = int(input())

# id = int(input())

# name = str(input())

# Dob = str(input())

# nb_course = int(input())

# id_course = str(input())

# name_course = str(input())

students = []  # list
courses = []   # list
marks = {} 

def input_number_student():
    print("Enter the nb of student: ")
    nb_student = int(input())
    for i in range(nb_student):
        print("Student ", i+1)
        input_info_student()
        print("-------------")

def input_info_student():
    students.append({"name": input("Name: ") , "id": input("ID: "),"Dob":input("Dob: ")})

def input_nb_course():
    nb_course = int(input("Input the nb of course: "))
    for i in range(nb_course):
        input_info_course()
        print("-------------")

def input_info_course():
    courses.append({"ID": input("ID course: "), "Name": input("Name_course: ")})

def input_mark(): 
    print("---INPUT MARK---")
    cid = input("Enter id of course to input marks: ")
    for course in courses:
        if cid == course["ID"]:
            for student in students:
                sid = student["id"]
                marks[(sid,cid)] = float(input(f"Enter mark of {student["name"]} :"))

def list_course():
    print("-----COURSE---------")
    for c in courses:
        print(f"ID: {c["ID"]} || Name: {c["Name"]}")
def list_students():
    print("------STUDENTS-------")
    for s in students:
        print(f"ID: {s["id"]} || Name: {s["name"]} || DoB: {s["Dob"]}")

def show_mark():
    cid = input("Enter course ID to show marks: ")
    for s in students:
        sid = s["id"]
        key = (sid,cid)
        if key in marks:
            print(f"{s["name"]} : {marks[key]}")   
        else:
            print(f"{s['name']}: no mark")


# input_number_student()    
# input_nb_course()
# input_mark()

# list_course()
# list_students()
# show_mark()

def main():
    while True:
        print("List action: \n")
        print("1.Input number students\n2.Input number of course\n3.Input mark \n4.Show full course\n5.Show list student\n6.Show mark")
        
        choice = input("Enter the number of your choice: ")
        if choice == 1:
            input_number_student
        if choice == 2:
            input_nb_course
        if choice == 3:
            input_mark
        if choice == 4:
            list_course
        if choice == 5:
            list_students
        if choice == 6:
            show_mark
        if choice == 0:
            break

main()