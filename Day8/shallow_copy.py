'''
Sometimes a user wants to create a copy that can be modified without
modifying the orignial, in order to do that we create copies of the
objects using 'copy' module

There are two ways to create copies

->Deep copy 
->Shallow copy

copy() returns a shallow copy of list
while deepcopy() returns a deep copy of list

Shallow Copy
A new collection object is constructed and references to the original
objects populated in the new object. Therefore it means changes to any
object reflect in the other object
Uses copy() function
'''

import copy
list1 = [10, 42, [23,55],16]
#using copy() to shallow copy
list2 = copy.copy(list1)

#output elements of list1 before any change
print("Original List1")
for i in range(0, len(list1)):
    print(list1[i], end=" ")

list2[2][0] = 89
list2[2][1]=10000

print("\r")

#output elements of list1 after changing list2
print("List1 after altering with list2")

for i in range(0, len(list1)):
    print(list1[i], end=",")




