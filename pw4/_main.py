import curses

import input
import output
from domains import MarkManager

mark_manager = MarkManager()

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
            input.input_number_student(screen)
        elif choice == "2":
            input.input_nb_course(screen)
        elif choice == "3":
            mark_manager.input(input.students, input.courses,screen)
        elif choice == "4":
            output.list_students(input.students,screen)
        elif choice == "5":
            output.list_course(input.courses,screen)
        elif choice == "6":
            mark_manager.show(input.students,screen)
        elif choice == "7":
            screen.clear()
            mark_manager.cal_gpa(input.students,input.courses)
            input.students.sort(key=lambda x: x.gpa, reverse=True)

            screen.addstr("\nSorted by GPA: \n")
            for s in input.students:
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

