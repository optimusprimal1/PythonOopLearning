


from abc import ABC, abstractmethod


class A(ABC):
    @abstractmethod
    def display(self):
        None


class B(A):

    def display(self):
        print('Displaying abstract method of class A')


class Animal(ABC):
    @abstractmethod
    def eat(self):
        pass

class Cow(Animal):
    def eat(self):
        print('Cow eat grass and herbs.')



class Tiger(Animal):
    def eat(self):
        print('Tiger is a carnivor animal and eat meat')



class X(ABC):
    @abstractmethod
    def m1(self):
        pass

    @abstractmethod
    def m2(self):
        pass

class Y(X):
    def m1(self):
        print('This is m1')


class Z(Y):
    def m2(self):
        print('This is m2')


class Cal(ABC):
    def __init__(self, value) :
        self.value = value
    
    @abstractmethod
    def add(self):
        pass

    @abstractmethod
    def substract(self):
        pass


class C(Cal):
    def add(self):
        print('self.value = ',self.value+100    )

    def substract(self):
        print('Subtract self.value = ',self.value - 10    )


cobj = C(1000)
cobj.add()
cobj.substract()



# yobj = Y()
# yobj.m1()
# zobj = Z()
# zobj.m1()
# zobj.m2()

# tiger = Tiger()
# tiger.eat()
# cow = Cow()
# cow.eat()

# b = B()
# b.display()




