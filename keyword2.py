#del keyword
s = "iamnandhu"
print(s)
del s
#print(s)

#Structure Keywords : def, class, return, lambda
print("    ")
print("def")
def fun():
    print("Inside Function")


fun()

print("  ")
print("class")
class Dog:
    attr1 = "mammal"
    attr2 = "dog"

print("     ")
print("return , yield")
'''When 'return' is used, it returns a single value and ends the function, while 
yield returns multiple values one at a time and keeps the function's state.'''
def fun():
  
    s = 2  
    
    # Return the value of S
    return s

# Call the function and print the result
print(fun())  

# Yield Keyword
def fun():
  
    # Yield the value 1, pausing the function here
    yield 1
    # Yield the value 2, pausing the function again
    yield 2
    # Yield the value 3, pausing the function once more
    yield 3  

# Iterate through the values yielded by the function
for value in fun():
    print(value)


print("              ")
print("lambda keyword ")
# Lambda keyword
'''Lambda keyword is used to make inline
returning functions with no statements allowed internally.'''
g = lambda x: x*x*x

print(g(7))


print("                 ")
print("with keyword")
'''with keyword is used to wrap the execution of block of code within methods
defined by context manager.This keyword is not used much in day to day
programming, mostly used in file'''
# using with statement
with open('file_path', 'w') as file:
    file.write('hello world !')


#as Keyword In Python
'''as keyword is used to create the alias for the module imported. i.e giving a new
name to the imported module. E.g import math as mymath.'''
import math as banda
print(banda.factorial(5))


#Scope and Namespace: Global, Nonlocal in Python
'''global: This keyword is used to define a variable inside the function to be of a
global scope.

non-local : This keyword works similar to the global, but rather than global, this
keyword declares a variable to point to variable of outside enclosing function,
in case of nested functions.'''
print("            ")
print("scope:")
a = 15
b = 10

def add():
  
    # Add global variables a and b
    c = a + b  
    print(c)

add()  # Output: 25

def fun():
  
  # Local variable in fun()
    var = 10  

    def gun():
      
    # Modify var1 in the enclosing scope (fun)
        nonlocal var  
        var += 10  
        print(var)  

    gun() 

fun() # Output: 20




#Async Programming: async, await
'''async: Used to declare a function as asynchronous, allowing
it to run concurrently with other tasks.'''
import asyncio

async def func():
    print("Hello, async world!")

'''await: Used to pause the execution of an async function
until the awaited task is complete.'''
import asyncio

# Define an asynchronous main function
async def main():
    await func()

# Define another async function that prints a message
async def func():
    print("Hello, async world!")  
    
# Run the main function using asyncio.run
asyncio.run(main())



