import curses
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
