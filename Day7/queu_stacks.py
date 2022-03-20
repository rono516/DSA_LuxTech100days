from collections import deque


class Queue():
    def __init__(self):
	#initialize two stacks using deque
        self.stack1 = deque()
        self.stack2 = deque()

    def enque(self,data):
        #move elements of the first stack to the second stack
        while len(self.stack1):
            self.stack2.append(self.stack1.pop())


        #push items into the first stack
        self.stack1.append(data)

        #return elements from stack2 to stack1

        while len(self.stack2):
            self.stack1.append(self.stack2.pop())


     #Remove elements from the queue

    def deque(self):

        #if first stack is empty

        if not self.stack1:
            print("Nothing in Stack1")
            exit(0)

        #return top item from first stack
        return self.stack1.pop()


if __name__ == "__main__":
    list1 = [1, 45, 67, 78]     
    q1 = Queue()

    for i in list1:
        q1.enque(i)

    print(q1.deque())
    print(q1.deque())


        