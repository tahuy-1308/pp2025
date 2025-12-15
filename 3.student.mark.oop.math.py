import math
import numpy as np
import curses


class Student():
    def __init__(self,name,sid,dob):
        self.__name = name
        self.__id = sid
        self.__dob = dob
        self.gpa = 0

    def get_name(self):
        return self.__name
    def get_id(self):
        return  self.__id
    def get_dob(self):
        return self.__dob
    def get_gpa(self):
        return self.gpa
    
    def input(screen):
        curses.echo()
        screen.addstr("Name: ")
        name = screen.getstr().decode()  #decode() dể chuyển từ bytes sang str vì screen.gettr() trả về bytes
        screen.addstr("ID: ")
        sid = screen.getstr().decode()
        screen.addstr("Dob: ")
        dob = screen.getstr().decode()
        return Student(name, sid, dob)

    def list(self,screen):
        screen.addstr(f"Name: {self.__name} | Id: {self.__id} | Dob: {self.__dob} | GPA: {self.gpa:.2f} \n")    

class Course():
    def __init__(self,cid,name,credit):
        self.__id = cid
        self.__name = name
        self.__credit = int(credit) #credit cần là số để tính gpa

    def get_name(self):
        return self.__name
    def get_id(self):
        return  self.__id
    def get_credit(self):
        return self.__credit
    
    def input(screen):
        curses.echo()
        screen.addstr("ID course: ")
        cid = screen.getstr().decode()
        
        screen.addstr("Name course: ")
        name = screen.getstr().decode()

        screen.addstr("Credit course: ")
        credit = int(screen.getstr().decode())

        return Course(cid, name,credit)
    
    def list(self,screen):
       screen.addstr(f"ID: {self.__id} | Name Course: {self.__name} | Credit: {self.__credit} \n")

class MarkManager():
    def __init__(self):
        self.__marks = {}
    
    def input(self,students,courses,screen):
        screen.clear() #clear để làm mới UI trước khi in nội dung mới
        curses.echo()
        screen.addstr("---INPUT MARK---\n")
        screen.addstr("Enter id of course to input marks: ")
        cid = screen.getstr().decode()

        found = False
        for course in courses:
            if cid == course.get_id():
                found = True
                break
        if not found:
            screen.addstr("Course ID not found!")
            screen.getch()
            return
        
        for student in students:
            sid = student.get_id()
            screen.addstr(f"Enter mark of {student.get_name()} :")
            markRaw = float(screen.getstr().decode())
            mark = math.floor(markRaw*10)/10
            self.__marks[(sid, cid)] = mark
        screen.addstr("\nMarks saved")
        screen.getch()  #getch() để pause màn hình

    def show(self,students,screen):
        screen.clear()
        curses.echo()
        screen.addstr("----Show Mark--------\n")
        screen.addstr("Enter course ID to show marks: ")
        cid = screen.getstr().decode()
        for s in students:
            sid = s.get_id()
            key = (sid, cid)
            if key in self.__marks:
                screen.addstr(f"{s.get_name()} : {self.__marks[key]} \n")
            else:
                screen.addstr(f"{s.get_name()}: no mark")

        screen.getch()
    
    def cal_gpa(self,students,courses):
        for st in students:
            marks = []
            credits = []
            for c in courses:
                key = (st.get_id(), c.get_id())
                if key in self.__marks:
                    marks.append(self.__marks[key])
                    credits.append(c.get_credit())
            if len(marks) == 0:
                st.gpa = 0
            else:
                marks_arr = np.array(marks)
                credits_arr = np.array(credits)

                st.gpa = float(np.sum(marks_arr*credits_arr) / np.sum(credits_arr))
                # st.gpa = np.average(marks_arr, weights=credits_arr) other method with np.average
            


students = []
courses = []
mark_manager = MarkManager()

def input_number_student(screen):
    screen.clear()
    curses.echo()
    screen.addstr("Enter the nb of student: ")
    nb_student = int(screen.getstr().decode())
    for i in range(nb_student):
        screen.addstr("Student ", i+1)
        st = Student.input(screen)
        students.append(st)
        screen.addstr("\n-------------\n")

    screen.getch()
def input_nb_course(screen):
    screen.clear()
    curses.echo()
    screen.addstr("Input the nb of course: ")
    nb_course = int(screen.getstr().decode())
    for i in range(nb_course):
        screen.addstr("Course", i+1)
        c = Course.input(screen)
        courses.append(c)
        screen.addstr("-------------\n")
    screen.getch()
    
def list_students(screen):
    screen.clear()
    screen.addstr("------STUDENTS-------\n")
    for s in students:
        s.list(screen)
    screen.getch()

def list_course(screen):
    screen.clear()
    screen.addstr("-----COURSE---------\n")
    for c in courses:
        c.list(screen)
    screen.getch()


def curses_main(screen):
    curses.curs_set(1)
    curses.echo()

    while True:
        screen.clear()
        screen.addstr(1, 2, "===== STUDENT MANAGEMENT SYSTEM =====")
        screen.addstr(3, 4, "1. Input students")
        screen.addstr(4, 4, "2. Input courses")
        screen.addstr(5, 4, "3. Input marks")
        screen.addstr(6, 4, "4. Show students")
        screen.addstr(7, 4, "5. Show courses")
        screen.addstr(8, 4, "6. Show marks")
        screen.addstr(9, 4, "7. Calculate + Sort GPA")
        screen.addstr(10, 4, "0. Exit")
        screen.addstr(12, 2, "Your choice: ")

        screen.refresh()
        choice = screen.getstr(12, 16, 10).decode()

        if choice == "1":
            input_number_student(screen)
        elif choice == "2":
            input_nb_course(screen)
        elif choice == "3":
            mark_manager.input(students, courses,screen)
        elif choice == "4":
            list_students(screen)
        elif choice == "5":
            list_course(screen)
        elif choice == "6":
            mark_manager.show(students,screen)
        elif choice == "7":
            screen.clear()
            mark_manager.cal_gpa(students,courses)
            students.sort(key=lambda x: x.gpa, reverse=True)

            screen.addstr("\nSorted by GPA: \n")
            for s in students:
                s.list(screen)
                screen.addstr("\n")
            # screen.refresh()    #cập nhật nội dung đã vẽ lên màn hình thật
            screen.getch()
            

        elif choice == "0":
            break
        else:
            screen.addstr("Invalid choice!")

def main():
    curses.wrapper(curses_main)
main()

