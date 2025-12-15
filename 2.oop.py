class Student():
    def __init__(self,name,sid,dob):
        self.__name = name
        self.__id = sid
        self.__dob = dob

    def get_name(self):
        return self.__name
    def get_id(self):
        return  self.__id
    def get_dob(self):
        return self.__dob
    
    def input():
        name = input("Name: ")
        sid = input("ID: ")
        dob = input("Dob: ")
        return Student(name, sid, dob)

    def list(self):
        print (f"Name: {self.__name} | Id: {self.__id} | Dob: {self.__dob}")    

class Course():
    def __init__(self,cid,name):
        self.__id = cid
        self.__name = name

    def get_name(self):
        return self.__name
    def get_id(self):
        return  self.__id
    
    def input():
        cid = input("ID course: ")
        name = input("Name course: ")
        return Course(cid, name)
    
    def list(self):
        print(f"ID: {self.__id} | Name Course: {self.__name}")

class MarkManager():
    def __init__(self):
        self.__marks = {}
    
    def input(self,students,courses):
        print("---INPUT MARK---")
        cid = input("Enter id of course to input marks: ")
        
        found = False
        for course in courses:
            if cid == course.get_id():
                found = True
                break
        if not found:
            print("Course ID not found!")
            return
        
        for student in students:
            sid = student.get_id()
            mark = float(input(f"Enter mark of {student.get_name()} :"))
            self.__marks[(sid, cid)] = mark

    def show(self,students):
        print("----Show Mark--------")
        cid = input("Enter course ID to show marks: ")
        for s in students:
            sid = s.get_id()
            key = (sid, cid)
            if key in self.__marks:
                print(f"{s.get_name()} : {self.__marks[key]}")
            else:
                print(f"{s.get_name()}: no mark")


students = []
courses = []
mark_manager = MarkManager()

def input_number_student():
    print("Enter the nb of student: ")
    nb_student = int(input())
    for i in range(nb_student):
        print("Student ", i+1)
        st = Student.input()
        students.append(st)
        print("-------------")

def input_nb_course():
    nb_course = int(input("Input the nb of course: "))
    for i in range(nb_course):
        print("Course", i+1)
        c = Course.input()
        courses.append(c)
        print("-------------")

def list_students():
    print("------STUDENTS-------")
    for s in students:
        s.list()

def list_course():
    print("-----COURSE---------")
    for c in courses:
        c.list()


def main():
    while True:
        print("\nList action:")
        print("1.Input number students")
        print("2.Input number of course")
        print("3.Input mark")
        print("4.Show full course")
        print("5.Show list student")
        print("6.Show mark")
        print("0.Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            input_number_student()
        elif choice == 2:
            input_nb_course()
        elif choice == 3:
            mark_manager.input(students, courses)
        elif choice == 4:
            list_course()
        elif choice == 5:
            list_students()
        elif choice == 6:
            mark_manager.show(students)
        elif choice == 0:
            break
        else:
            print("Invalid choice!")


main()