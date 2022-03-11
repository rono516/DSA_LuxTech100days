#linked list will have two classes the node and the linked list
# from itertools import count


class Node:
    def __init__(self,data=None, next=None):
        self.data = data
        self.next = next
        #the node has data and pointer to the next value

class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtBeginning(self, data):
        #to insert the value at the beginning, you need to unsit the current head value
        #and use a Node class to create a node with data and pointer to the next value

        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("Linked List is Empty")
            return

        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data)+ '-->'
            itr = itr.next   
        print(llstr)
        
    def insertAtEnd(self, data):
        #to insert at the end of the linked list
        #we first have to check if there is no data or if data has no next value
        if self.head is None:
            self.head = Node(data, None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
        
        itr.next = Node(data, None)

    
    def insertValues(self, data_list):
        #inserts into the linked list from a set of values in a list
        self.head = None
        for data in data_list:
            self.insertAtEnd(data)
            
    def getLength(self):
        count = 0
        itr = self.head
        while itr:
            count +=1
            itr = itr.next
            # print(itr.next)
        return count    
    
    def removeAt(self, index):
        if index<0 or index>=self.getLength():
            raise Exception("Invalid index")
        if index == 0:
            self.head = self.head.next
            #||| set head of linked list to be the next value after head
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                itr.next = itr.next.next   
                #set value of index given to be the next element in the linked list         
            itr = itr.next  
            count += 1     
            
             
    def insertAt(self, index, data):
        if index<0 or index>=self.getLength():
            raise Exception ("Invalid index")
        #insert at the index provided
        
        if index == 0:
            #if index is zero, insert at the begining
            self.insertAtBeginning(data)
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                #create node to add data
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count +=1 
            
    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            return
        
        if self.head.data == data_after:
            self.head.next = Node(data_to_insert, self.head.next)
            return
        
        itr = self.head
        while itr:
            if itr.data == data_after:
                itr.next = Node(data_to_insert, itr.next)
                break
            itr = itr.next  
            
    def remove_by_value(self, data):
        if self.head is None:
            return
        
        if self.head.data == data:
            self.head = self.head.next
            return
        
        
        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next          
                    

if __name__ == '__main__':
    ll = LinkedList()
    # ll.insertAtBeginning(178)
    # ll.insertAtBeginning(510)
    # ll.insertAtBeginning(556)
    # ll.insertAtEnd(700)
    # ll.insertAtEnd(400)
    # ll.insertAtBeginning(9)
    # ll.insertAtEnd(420)
    ll.insertValues([45, 75, 89, 5456, 890, 654])
    ll.print()
    ll.removeAt(3)
    ll.print()
    ll.insertAt(0, "figs")
    ll.print()
    ll.insert_after_value("figs", 40)
    ll.print()
    ll.remove_by_value(654)
    print("One value removed")
    ll.print()
    print(f'Length of our linked list: {ll.getLength()}')