# Single level inheritance
class A:
    x,y=10,20
    def m1(self):
        print('This m1 is from Class A. ', self.x+self.y)


class B(A):
    a,b = 100,200
    def m2(self):
        print('This m2 is from Class B. ', self.b+ self.a)

    def m3(self):
        print('This m2 is from Class B. ', self.y+ self.a)


# aObj = A()
# aObj.m1()

# bObj = B()
# bObj.m1()
# bObj.m2()
# bObj.m3()


# Multilevel Inheritance
class multiA:
    x, y = 10, 20

    def m1(self):
        print('This m1 is from Class A. ', self.x + self.y)


class multiB(multiA):
    a, b = 100, 200

    def m2(self):
        print('This m2 is from Class B. ', self.b + self.a)

    def m3(self):
        print('This m3 is from Class B. ', self.y + self.a)

class multiC(multiB):
    i,j = 1,2
    def m4(self):
        print('This m4 is from Class C. ', self.i + self.j)


# c = multiC()
# c.m1()
# c.m2()
# c.m3()
# c.m4()

# Heirarichal Inheritance
class multiA:
    x, y = 10, 20

    def m1(self):
        print('This m1 is from Class A. ', self.x + self.y)


class multiB(multiA):
    a, b = 100, 200

    def m2(self):
        print('This m2 is from Class B. ', self.b + self.a)

    def m3(self):
        print('This m3 is from Class B. ', self.y + self.a)

class multiC(multiA):
    i,j = 1,2
    def m4(self):
        print('This m4 is from Class C. ', self.i + self.j)

# b = multiB()
# c = multiC()
# b.m1()
# b.m2()
# b.m3()
# c.m1()
# c.m4()


# Multilevel Inheritance


class multiA:
    x, y = 10, 20

    def m1(self):
        print('This m1 is from Class A. ', self.x + self.y)


class multiB():
    a, b = 100, 200

    def m2(self):
        print('This m2 is from Class B. ', self.b + self.a)

    def m3(self):
        print('This m3 is from Class B. ', self.y + self.a)

class multiC(multiA, multiB):
    i,j = 1,2
    def m4(self):
        print('This m4 is from Class C. ', self.i + self.j)



c = multiC()
c.m1()
c.m2()
c.m3()
c.m4()










