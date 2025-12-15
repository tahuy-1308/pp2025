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
        name = screen.getstr().decode()
        screen.addstr("ID: ")
        sid = screen.getstr().decode()
        screen.addstr("Dob: ")
        dob = screen.getstr().decode()
        return Student(name, sid, dob)

    def list(self,screen):
        screen.addstr(f"Name: {self.__name} | Id: {self.__id} | Dob: {self.__dob} | GPA: {self.gpa:.2f} \n")    
