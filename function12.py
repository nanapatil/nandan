#what is function.
#what is server.
#what is server side scripting language/scripting language.
#whar is argument/parameter in function python
#types of argument in function
#types of function
#differance between return and print
#what is iterable
#what is sequence
#what is collection
'''
actual argument:-function calling argument are called actual argument 
formal argument:-function defining argument are called formal argument
'''

def add(a,b):   #formal argument
    print(a+b)

#function calling
add(1,2)  #actual argument


#type of actual argument/ways of passing argument to a function.

'''
1)positinal argument
2)keyword argument
3)default argument
4)variable legth argument
5)keyword variable length argument
'''

#1)positinal argument-here we are passing value to a function in correct position

def add(a,b):   
    print(a+b)

#function calling
add(1,2)  #here the value pass to a function in correct position

#2)keword argument-here value pass to a function in the form of keyword
def add(a,b):   
    print(a+b)

#function calling
add(a=1,b=2) 

#3)default argument-here we can pass value to a function but one value can be default if we are not passing
#any value to a function then default value will be considered.
def add(a,b=33):   
    print(a+b)

#function calling
add(1,34) 

#4)variable length argument-here we can pass multiple value to a function/here we can pass any iterable to a function.
def add(a):   
    print(a)

#function calling
add([1,34,22,43,4,5,6,77,3]) 



def add(*a):   
    for i,j in enumerate(a):
        for k in range(len(j)):
            print(k)
l=[1,34,22,43,4,5,6,77,3]
add(l) 

#5)keyword variable length:-here we can can pass value to function in the form of dictionary

def add(a):   
    print(z)
z={1:'rahul',2:'amol'}
#function calling
add(z) 

#core remaing syllabus
'''


lambda function
comprehension
recursion
decorators
generator
diff between generator vs iterator
diff between return and yield

'''
#print and return
#print:-print will print and return business logic
#return-it only only return business logic we need to print it explicitly
def hello():
    print('hello')
    a=2
    return a
print(hello())    