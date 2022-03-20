from sympy import preview


class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class linkedList(object):
    def __init__(self, head = None):
        self.head = head


    def insertNode(self,data):
        node = Node(data)
        node.next = self.head
        self.head = node
        
    # def insertAtEnd(self, data):
    #     current1 = self.head
    #     if self.head == None:
    #         self.head = data
    # # if self.head == None:
    #     #     self.head = data


    def displayList(self):
        
        current = self.head
        while current:
            print(current.value, end="->>")
            current = current.next


    def deleteDuplicate(self):
        current = self.head
        prev = None
        duplicateDict = dict()
        while current:
            if current.value not in duplicateDict:
                duplicateDict[current.value] = None
                prev = current
            else:
                prev.next = current.next

            current = current.next



l1 = linkedList()
l1.insertNode(9)
l1.insertNode(90)
l1.insertNode(90)
l1.insertNode(40)
l1.insertNode(46)
l1.insertNode(83)
l1.deleteDuplicate()
l1.displayList()