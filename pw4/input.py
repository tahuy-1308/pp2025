import curses
from domains import Student
from domains import Course

students = []
courses = []

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