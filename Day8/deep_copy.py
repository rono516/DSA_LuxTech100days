'''
Deep Copy
In deep copy, a collection object is first created then populated with copies
of original object. A copy of object is copied in another object
uses deepcopy() function

'''
import copy
list1 = [13, 67, [44, 78], 93]

list2 = copy.deepcopy(list1)

#Elements of list1 before any alteration
print("Original elements of list1")

print("\r")
for i in range(0, len(list1)):
    print(list1[i], end=" ")

print("\r")
#Alter the copy of list1

list2[2][0] = 899
list2[2][1] = 678

#Elements of list1 and 2 after deep copy

print("After deep copy list1 and list2")
print("\r")

for i in range(0, len(list1)):
    print(list1[i], end=" ")

print("\r")
print("List2")

for i in range(0, len(list2)):
    print(list2[i], end=" ")



print("Change is not reflected in original List because it was deepcopied")