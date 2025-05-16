# data tyoes
# set data type
# initializing empty set
s1 = set()

s1 = set("i am nandhu")
print("Set with the use of String: ", s1)

s2 = set(["i", "am", "nandhu"])
print("Set with the use of List: ", s2)

#Access Set Items
print("        ")
set1 = set(["i", "am", "Nandhu"])
print(set1)

# loop through set
for i in set1:
    print(i, end=" ")

print("\n")
    
# check if item exist in set    
print("Nandhu" in set1)





#Dictionary Data Type
print("        ")
print("dict dt")
# initialize empty dictionary
d = {}


d = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print(d)

# creating dictionary using dict() constructor
d1 = dict({1: 'Geeks', 2: 'For', 3: 'Geeks'})
print(d1)

#Accessing Key-value in Dictionary
d = {1: 'Geeks', 'name': 'For', 3: 'Geeks'}

# Accessing an element using key
print(d['name'])

# Accessing a element using get
print(d.get(3))



#list
print("      ")
fruits = ["apple", "banana", "orange"]
print(fruits)
fruits.append("grape")
print(fruits)
fruits.remove("orange")
print(fruits)


#tuple
coordinates = (3, 5)
print(coordinates)
print("X-coordinate:", coordinates[0])
print("Y-coordinate:", coordinates[1])


