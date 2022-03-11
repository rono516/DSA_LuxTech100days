class Node:
    def __init__(self, data=None, next=None):
        self.data= data
        self.next= next
class LinkedList:
    def __init__(self):
        self.head = None
        
    def findKth(self, index):
        itr = self.head
        
        count= 0
        while itr:
            if count == index:
                print (itr.data)
            itr = itr.next
            
            count +=1
            
    def insertAtEnd(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)    
    def insertValues(self, dataList):
        self.head = None
        for data in dataList:
            self.insertAtEnd(data)        
        
ll = LinkedList()
ll.insertValues([89, 17, 78, 89, 63, 67])
ll.findKth(2)