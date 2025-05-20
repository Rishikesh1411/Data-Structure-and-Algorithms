"""
        assignment-13

        1.define a class queue to implement queue data structure using singly link list concept.define __init__() method to initialize front and rear reference 
        veriable and item count variable to keep track  of the number of items in the queue.

        2.define a method is_empty() to check if the queue is empty in queue class.

        3.in queue class ,define enqueue() method to add data into the queue.

        4.in queue class ,define dequeue() method to remove data from the queue.

        5.in queue class ,define get_front() method to return the front item of the queue without.

        6.in queue class, define get_rear() method to return rear element of the queue.

        7.in queue class, define get_size() method to return the number of items in the queue.



"""

class Node:
    def  __init__(self,item=None):
        self.item=item
        self.next=None


class Queue:

    def  __init__(self): ######1-------
        self.front = None
        self.rear = None
        self.item_count = 0

    def is_empty(self):   #####2------
        return  self.item_count==0 or  self.front == None or self.rear==None


    def  enqueue(self, data):  #####3------
        newnode=Node(data)
        if self.is_empty():
            self.front = newnode
            

        else:
            self.rear.next=newnode

        self.rear=newnode
        self.item_count += 1

    def dequeue(self):######4------
        if self.is_empty():
            raise IndexError("Empty Queue")

        elif self.front==self.rear:
            self.front=None
            self.rear=None
        
        else:
            self.front=self.front.next
            self.front.next=self.front

        self.item_count -= 1

    def get_front(self): ####5---------
        if self.is_empty():
            raise IndexError("Empty Queue")
        else:
            return self.front.item

    def  get_rear(self):   #####6-----
        if self.is_empty():
            raise IndexError("Empty Queue")
        else:
            return self.rear.item

    def size(self): # ##7-------
        return  self.item_count

    def print_sll_queue(self):  ####8----
        if self.is_empty():
            print("Queue is empty")
        else:
            temp=self.front
            while temp:
                print(temp.item,end=" ")
                temp=temp.next


q1=Queue()

q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
q1.enqueue(40)
q1.enqueue(50)

print("front /peek value is",q1.get_front(),"rear value is",q1.get_rear())
q1.print_sll_queue()
q1.dequeue()
print(q1.get_front(),q1.get_rear())
print(q1.size())
print(q1.is_empty())




    


