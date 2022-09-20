class Student():
    def __init__(self,eid,ename,rollno):
        self.eid = eid
        self.ename = ename
        self.rollno = rollno

    def displayStudentName(self):
        print("stid:{} Name:{} RollNo{}".format(self.eid,self.ename,self.rollno))