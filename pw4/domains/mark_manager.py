import math
import numpy as np
import curses

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
            
