import sys
# sys.path.append('D:/pythonPyProject/PythonPackage');

sys.path.append('D:/pythonPyProject/Package1');
sys.path.append('D:/pythonPyProject/Package1/Pack2');
sys.path.append('D:/pythonPyProject/ClassPack1');
sys.path.append('D:/pythonPyProject/ClassPack2');
# Approach 1

# import module1
# import module2
# module1.display()
# module2.show()

from emp import Employee
from StudentClass import Student

e = Employee(101,'Sir Pavan', 40000)
e.displayEmployeeName()
s = Student(101,'Kakoo Mian', 40000)
s.displayStudentName()
# # from module2 import *
# show()
# display()
# Approach 2

# from module1 import *
# from module2 import *
# display()
# show()



