# from collections import deque
# list1 = deque(['a', 'b', 'c', 'd'])
# list1.append('f')
# list1.appendleft("Z")
# # list1.popleft()
# print(list1)


#IMPLEMENTING A QUEUE
# In a queue you add items or people as they arrive
#https://realpython.com/linked-lists-python/

# from collections import deque
# # import queue
# queue = deque()
# queue
# queue.append('Mary')
# queue.append('John')
# queue.append('Peter')

# print(queue)

# #REMOVE THE QUEUE FROM THE FIRST ONE
# queue.popleft()
# print(queue)

#mary exits from the queue
#Mimicking a real life queue



# Implementing a linked list

#create class to represent linked list

# class LinkedList:
#     def __init__(self):
#         self.head = None

#node of each linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)  

llist = LinkedList()
#print(llist)
first_node = Node('a')
second_node = Node('b')
third_node = Node('c')
llist.head = first_node
first_node.next = second_node
second_node.next = third_node
print(llist)