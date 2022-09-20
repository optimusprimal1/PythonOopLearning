class Employee():
    def __init__(self,eid,ename,sal):
        self.eid = eid
        self.ename = ename
        self.sal = sal

    def displayEmployeeName(self):
        print("empid:{} empname:{} empSal{}".format(self.eid,self.ename,self.sal))