from ast import arg


def sum(*args):
    sum = 0
    for i in args:
        sum+=i
    print('Sum of args is = ',sum)

sum(1,2,3)

# printing list instead of passing variable one by one 

# Example 1


def my_list(a,v,b,n,m):
    print('value are = ',a,v,b,n,m)

args= [1,2,3,4,5]
my_list(*args)

#  Checking **kwargs

def my_kwargs(a,b,c):
    print('a,b,c = ', a,b,c)

a={'a':'1','b':"Syed M Usama", 'c': 'Graduate'}

my_kwargs(**a)

# Example 2

def my_func(**kwargs):
    for i,j in kwargs.items():
        print('I,j = ',i,j)


my_func(name='Tom',sport='Football',roll='10')










