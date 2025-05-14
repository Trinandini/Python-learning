# to show a statement in python
print("Hello world")

#Indentation in python
print("          ")
if 10>5:
    print("Indentation")
    print("Tab Indenation")

print("I have not Indentation")

#Input in python
print("          ")
name = input("Enter the name:")
print("HI",name)


# variables: Single variable,Multiple Variables
print("          ")
s = "Nandhu"
print(s)


s = "Nandhu"
age = 20
city = "India"
print(s, age, city)

#Take Multiple Input in Python
# taking two inputs at a time
print("          ")
x, y = input("Enter the no.of shoes and heels:").split()
print("No.of shoes:",x)
print("No.of heels:",y)

# taking three inputs at a time
print("          ")
x, y, z = input("Enter three values: ").split()
print("Total number of students: ", x)
print("Number of boys is : ", y)
print("Number of girls is : ", z)


#Output Formatting

#In Python, the format() method is used for string formatting, allowing the insertion of values into placeholders within a string.
#Placeholders are defined using curly braces {}. The format() method
print("          ")
name = "Nandhu"
age = 20
formatted_string = "My name is {} and I am {} years old.".format(name, age)
print(formatted_string)

amount = 150.75
print("Amount: ${:.2f}".format(amount))



#using sep and end parameter
print("          ")
# end Parameter with '@'
print("Python", end='@')
print("GeeksforGeeks")


# Seprating with Comma
print('G', 'F', 'G', sep='')

# for formatting a date
print('09', '12', '2016', sep='-')

# another example
print('pratik', 'geeksforgeeks', sep='@')



#using f string, concise way format by f or F with sm {} fillings
print("          ")
name = 'Nandhu'
age = 20
print(f"Hello, My name is {name} and I'm {age} years old.")

#using % operator

#we use ‘%’ operator. % values are replaced with zero or more value of elements.
#The formatting using % is similar to that of ‘printf’ in the C programming language.

#%d –integer
#%f – float
#%s – string
#%x –hexadecimal
#%o – octal

# Taking input from the user
num = int(input("Enter a value: "))

add = num + 5

# Output
print("The sum is %d" %add)

# we barely use this
































