"""
         1.define a class Node with instance object memeber veriables ,prev,item,next

         2.define a class deque to implement deque data structure using dll concept.
          define __init__()method to initialize front and rear refrence veriable and;
          item count variable to keep track of number of element in the deque.

          3.define a method is empty() to check if the dequq is empty in  deque class.

          4.in deque class define insert front() method to add data at the front of the deque

          5.in deque class define insert rear()  method to add data at the rear of the deque


          6.in  deque class define delete_front() method to removve front element from the deque

          7. in  deque class define delete_rear()  method to remve rear element from the deque

          8.in deque class ,define get_front() method to return rear element from the deque

          9.n deque class ,define get_rear() method to return rear element from the deque

          10.in deque class,define size() method to return size of the deque that is number of items present in the deque.


"""

class Node:  ####1--------
    def __init__(self, item):
        self.prev = None
        self.item = item
        self.next = None

class deque: ##2-----
    def __init__(self):
        self.front = None
        self.rear = None
        self.item_count = 0

    
    def is_empty(self):  ###3---
        return self.item_count == 0 or self.front==None

    def insert_front(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.rear = new_node
        else:
            new_node.next = self.front  # Set the next attribute of the new node
            self.front.prev = new_node  # Set the prev attribute of the current front node
        self.front = new_node
        self.item_count += 1

    def insert_rear(self, data):
        new_node = Node(data)  # Create a new Node object with only the data
        if self.is_empty():
            self.front = new_node
        else:
            self.rear.next = new_node  # Set the next attribute of the current rear node
            new_node.prev = self.rear  # Set the prev attribute of the new node
        self.rear = new_node
        self.item_count += 1

    def  del_front(self): ###6---
        if self.is_empty(self):
            raise IndexError("Deque is Empty")
        else:
            if self.front==self.rear:
                self.front=None
                self.rear=None
            else:
                self.front=self.front.next  
                self.front.prev=None
            self.item_count-=1

    def delete_rear(self): ####7----
        if self.is_empty():
            raise IndexError("Deque is Empty")
        else:
            if self.front==self.rear:
                self.front=None
                self.rear=None
            else:
                self.rear=self.rear.prev
                self.rear.next=None

    def get_front(self):  ###8----
        if self.is_empty():
            raise IndexError("Deque is Empty")
        else:
            return self.front.item


    def get_rear(self): ##9----
        if self.is_empty():
            raise IndexError("Deque is Empty")
        else:
            return self.rear.item

    def size(self):
        return self.item_count

    def print_deque(self):
        temp = self.front
        while temp is not None:
            print(temp.item, "<->", end="")
            temp = temp.next
        print()


d1=deque()
d1.insert_front(10)
d1.insert_front(20)
d1.insert_front(30)
d1.insert_rear(40)
d1.insert_rear(50)
d1.print_deque()
print(d1.get_rear())
print(d1.get_front())
d1.delete_rear()
d1.print_deque()


    


        



    


