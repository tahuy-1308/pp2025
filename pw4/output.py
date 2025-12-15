import curses
def list_students(students,screen):
    screen.clear()
    screen.addstr("------STUDENTS-------\n")
    for s in students:
        s.list(screen)
    screen.getch()

def list_course(courses,screen):
    screen.clear()
    screen.addstr("-----COURSE---------\n")
    for c in courses:
        c.list(screen)
    screen.getch()