#keyword
#Getting List of all Python keywords
import keyword

# printing all keywords at once using "kwlist()"
print("The list of keywords is : ")
print(keyword.kwlist)


#Value Keywords: True, False, None Keyword, del
print("                   ")
print("value keyword : True,Flase,None,del")
print(False == 0 )
print(True == 1)

#True +True +True = 3
print(True+True+True)
print(True+False+False)

#none isn't equal to 0 or an empty list[]
print(None == 0)
print(None == [])


#operator keyword: and ,or ,not, in, is
print("              ")
print("and or not")
a = True
b = False
print(a and b)
print(a or b)
print(not a)


print("              ")
print("in keyword")
print(3 in [1,2,3])

if 'an' in 'nandhu':
    print("an is part of nandhu")
else:
    print("an is not part of nandhu")


print("                ")
print("is keyword")
print(2 is 2)
a = [1,2,3]
b = a
c = [1,2,3]
print(a is b)
print(a is c)

print("                   ")
print("conditional keyword: if,else, elif")
x = -9
if x>0:
    print("positive")
elif x<0:
    print("Negative")
else:
    print("Zero")

# interation keyword: for,while,break,continue,pass
print("   ")
print("for,continue")
for num in range(3):
    if num == 2:
        continue
    print(num)


print(" ")
print("while,break")
count = 0
while count <4:
    count += 1
    if count ==3:
        break
    print(count)
print(count)

print("     ")
print("pass")
n = 10
for i in range(n):
    # pass is a placeholder
    # where the code is added later
    pass



#exception handling keywords
'''print(" ")
print("try except arrise raise")

a, b = 4, 0
try:
    k = a // b  # Attempt integer division (4 // 0)
    print(k)
    
# This block catches the ZeroDivisionError
except ZeroDivisionError: 
    print("Can't divide by zero")

finally:
    # This block is always executed regardless of the exception
    print('This is always executed')


print("The value of a / b is : ")

# Will raise an AssertionError because b == 0
assert b != 0, "Divide by 0 error"  

# Division is attempted but will not reach due to assert
print(a / b)  

# Raise a TypeError if the strings are different
temp = "geeks for geeks"
if temp != "geeks":
    raise TypeError("Both the strings are different.")'''




    
    
      



