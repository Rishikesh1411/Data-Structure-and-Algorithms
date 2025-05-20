"""
     1.define a class queue to implement queue data structure using list .define __init__() method to create an empty list object as instance object member of queue
     2.DEFINE A METHOOD IS EMPTY () TO CHECK IF THE QUEUE IS EMPTY IN QUEUE C LASS
     3.IN QUEUE CLASS DEFINE ENQUEUE() METHOD TO ADD THE DATA AT THE REAR END OF THE QUEUE
     4.IN QUEUE CLASS DEFINE DEQUEUE() METHOD TO REMOVE FRONT ELEMENT FROM QUEUE
     5.IN QUEUE CLASS DEFINE GET_FRONT() METHOD TO RETURN FRONT ELEMENT OF THE QUEUE
     6.IN QUEUE CLASS,DEFINE GET_REAR() METHOD TO RETURN REAR ELEMMENT OF THE QUEUE
     7.IN QUEUE CLASS DEFINE SIZE() METHOD TO RETURN SIZE OF TH QUEUE THAT IS NUMBER OF ITEMS PRESENT IN THE QUEUE.
 
     using list rear element list[-1] and front(first element) list[0]

"""

class Queue(list):

     def __init__(self):  ##1------------
          self.items=[]
          self.front=None
          self.rear= None
     
     def  is_empty(self):  ##2------------
          return len(self.items)==0

     def enqueue(self,data): ##3-----
          self.items.append(data)

     def dequeue(self):  ##4-----
          if not self.is_empty():
               self.items.pop(0)
          else:
               raise IndexError("Queue Underflow")


     def get_front(self): ##peek
          if not self.is_empty():
               return self.items[0]
          else:
               raise IndexError("Queue Underflow")
          

     def get_rear(self):
          if not self.is_empty():
               return self.items[-1]
          else:
               raise IndexError("Queue Underflow")
          

     def size(self):
          return len(self.items)

     def print(self):
          print(self.items)

## testing------

q1=Queue()
try:
     print(q1.get_front())
except  IndexError as e:
     print(e.args[0])


q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
q1.enqueue(40)
q1.enqueue(50)
print(q1.size())
print("front",q1.get_front(),"rear=",q1.get_rear())
q1.print()
try:
     q1.dequeue()
     print("queue has now",q1.size(),"elements")
except   IndexError as e:
     print(e.args[0])






     
     

    
