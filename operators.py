#operators

#arithmetic operators
print("Arithmetic operators")
a = 5
b = 20
print("addition of numbers:", a+b)
print("subtraction of numbers :",a-b)
print("subtraction of numbers:",b-a)
print("multipication of numbers:", a*b)
print("divison of numbers:", a/b)
print("division of numbers:", b/a)
print("floor division:", a//b)
print("floor division:", b/a)
print("modulus:", a%b)
print("modulus:",b%a)
print("exponential:", a**b)
print("exponential:",b**a)


#float division
print("          ")
print(5/5)
print(10/2)
print(-10/2)
print(20.0/2)

#floor division
print("                      ")
print(10//3)
print (-5//2)
print (5.0//2)
print (-5.0//2)


#comparison operator or relational operator
print("\n")
print("relational operator")
a = 56
b = 33

print(a > b)
print(a < b)
print(a == b)
print(a != b)
print(a >= b)
print(a <= b)

print("\n")
a = 9
b = 5
c = 9

print(a != b)
print(a != c)


#logical operator
print("               ")
print("logical operator")
a = True
b = False
print(a and b)
print(a or b)
print(not a)

print("               ")
print("2")
a,b,c = True,False,True
if a and c:
    print("Both a ,c staisfy AND operator")
if b or c:
    print("Both b ,c satisfy OR operator")
if not c:
    print("print b is false (NOT CONDITION)")

print("               ")
print("3")
a = 10
b = 10
c = -10
if a>0 and b>0:
          print("The numbers are greater than 0")
if a>0 and b>0 and c>0:
           print("The numbers are greater than 0")
else:
    print("not all numbers are greater than 0")


#The code checks if all variables a, b, and c evaluate to True, printing a message accordingly.
print("                                ")
print("4")
a = 10
b =12
c = 0
if a and b and c:
    print("if all the boolean values are true")
else:
    print("any one of the boolean is true")


print("                                ")
print("5")
a = 10
b =10
c = 10
if a and b and c:
    print("if all the boolean values are true")
else:
    print("any one of the boolean is true")


print("                                ")
print("6")
a = 10
b = -10
c = 0
if a > 0 or b > 0:
    print("Either of the number is greater than 0")
else:
    print("No number is greater than 0")
if b > 0 or c > 0:
    print("Either of the number is greater than 0")
else:
    print("No number is greater than 0")

print("                                ")
print("7")
a = 10
b = 12
c = 0
if a or b or c:
    print("Atleast one number has boolean value as True")
else:
    print("All the numbers have boolean value as False")


print("                                     ")
print("8")
a = 10
if not a:
    print("Boolean value of a is True")
if not (a % 3 == 0 or a % 5 == 0):
    print("10 is not divisible by either 3 or 5")
else:
    print("10 is divisible by either 3 or 5")


print("         ")
print("9")
def order(x):
    print("Method called for value:", x)
    return True if x > 0 else False


a = order
b = order
c = order
if a(-1) or b(5) and c(10):
    print("Atleast one of the number is positive")


#The function order(x) is being called here: as a(-1)


#bitwise operator
print("      ")
print("bitwise operator")
a = 10
b = 4
# Print bitwise AND operation
print("a & b =", a & b)

#Membership Operators
print("                      ")
print(" IN Operator")
list1 = [1,2,3,4]
str1 = "Hello world"
dict= {1:"i", 2:"am", 3:"nandhu"}
print(2 in list1) # checking whether present
print('o' in str1)
print(3 in dict)


#NOT IN Operator
print("                     ")
print("NOT IN Operator")
list1 = [1,2,3,4]
str1 = "Hello world"
dict= {1:"i", 2:"am", 3:"nandhu"}
print(2  not in list1) # checking whether not present
print('o' not in str1)
print(3 not in dict)


# operators.contains() Method
# Syntax: operator.contains(sequence, value)
print("                   ")
print(" operators.contains() Method")
# import module
import operator

# using operator.contain()
# checking an integer in a list
print(operator.contains([1, 2, 3, 4, 5], 2))

# checking a character in a string
print(operator.contains("Hello World", 'O'))

# checking an integer in aset
print(operator.contains({1, 2, 3, 4, 5}, 6))

# checking for a key in a dictionary
print(operator.contains({1: "i", 2:"am", 3:"nandhu"}, 3))

# checking for an integer in a tuple
print(operator.contains((1, 2, 3, 4, 5), 9))


#Python Identity Operators
#Python IS Operator
print("                       ")
print("Python IS Operator")

# of 'is' identity operator
num1 = 5
num2 = 5

a = [1, 2, 3]
b = [1, 2, 3]
c = a

s1 = "hello world"
s2 = "hello world"

# using 'is' identity operator on different datatypes
print(num1 is num2)
print(a is b)
print(a is c)
print(s1 is s2)
print(s1 is s2)

#Python IS NOT Operator
print("                        ")
print("Python IS NOT Operator")

# of 'is' identity operator
num1 = 5
num2 = 5

a = [1, 2, 3]
b = [1, 2, 3]
c = a

s1 = "hello world"
s2 = "hello world"

# using 'is not' identity operator on different datatypes
print(num1 is not num2)
print(a is not b)
print(a is not c)
print(s1 is not s2)
print(s1 is not s1)


#Difference between '==' and 'is' Operator
#The equality operator is used to compare the value of two variables, whereas the identities operator is used to compare the memory location of two variables
print("   ")
print("difference btw == and 'is' ")
a = [1, 2, 3]
b = [1, 2, 3]

# using 'is' and '==' operators
print(a is b)
print(a == b)







    






          






