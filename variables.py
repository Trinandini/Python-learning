#python variables
s = 5
T = " nandhu"
print(s)
print(T)

#some invalid
#1name = 7, can't start with number
#class name = "10A", space does not exists in variable name
#class = 10, class reserved key


#dynamic typing
print("                                ")
print("dynamic typing")
#dynamically typed, meaning the same variable can hold different types of values during execution.
x = 15
x ="nandhu"
print(x) # will give output of last permanent varibale container 


#Multiple Assignments

#Assigning the Same Value
print("                                ")
print("sm value multiple assignments")
a = b = c = 100
print(a,b,c)
# here also without _  it takes abc as one variable, error print(abc) 
# it win't print without comma between variables print(a b c)
# to equally mutilpes assigned commas are deifferenited to print

#Assigning Different Values
print("                                ")
print("different values mutliple assignments")
a,b,c = 34,"nandhu", 89.5
print(a,b,c)


#Type Casting a Variable
print("                                ")
print("Type cast")
n = "10" # string
c = int(n) # type cast to inetger
k = 10
f = float(k)
j =10
l = str(j)


print(c)
print(f)
print(l)


#Getting the Type of Variable
# type() built in function
print("                                ")
print("type function")
a = 1
b = 2.5
c = 3+4j
d = {'key' : 'value'}
i = True
e = set("Nandhu")
f = "Trinandini"
g = [ 1, 2.5, 3+4j, 'Nandhu', {'key':'value'}]
h = (1,"hello")

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(i))
print(type(e))
print(type(f))
print(type(g))
print(type(h))


#Scope of a Variable
print("                   ")
print("local variable")
#variables defined inside a function are local to that function.
def f():
    a = "I am local"
    print(a)
f()
#f() this is callling without this body of code does not ptint, function syntax

print("                                     ")
print("global variable")
#Variables defined outside any function are global and can be accessed inside functions using the globalkeyword.
b = "I am global"
def f():
    global b
    b = " Modified globally"
    print(b)
f()

#del Keyword
'''a = 10
print(a)
del a ''' # throws an error a is not defined

#swapping of numbers
print("                                               ")
print("swapping")
a,b = 10,5
a, b = b,a
print(a,b)
print("swapping by third variable")
a = 10
b =5
c = a
a = b
b = c
print(a,b)

#Counting Characters in a String
print("                    ")
s = " i am trinandini "
s = len(s)
print("length of the string:",s)

 #the correct way to check if a variable is of a specific type in Python?  isinstance(var, int)

x = 5
y = 2
print(x // y)

#concatenate two strings in Python? str1+str2

#What is the purpose of the max() function in Python? To find the maximum value in a list

#What is the purpose of the enumerate() function in Python?To get the index and value of each item in an iterable\

#How do you create a dictionary using a comprehension in Python? {key: value for key, value in iterable}

#What is the purpose of the __dict__ attribute in Python? To access the dictionary of a class or module

#How do you convert a list of strings to a single string in Python?  " ".join(list)

'''What is the output of the following code?

x = [1, 2, 3, 4]
y = filter(lambda a: a % 2 == 0, x)
print(list(y))

 [2, 4]

 returns a %2==0 , even only 2,4 '''


def sum_of_n(n):
    return n * (n + 1) // 2

n = int(input("Enter a number: "))
print("Sum of first", n, "numbers is:", sum_of_n(n))












