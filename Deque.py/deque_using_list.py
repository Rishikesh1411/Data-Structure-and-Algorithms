"""   
       ASSIGNMENT-14-


       1.DEFINE A CLASS DEQUE TO IMPLEMENT DEQUE DATA STRUCTURE USING LIST.DEFINE __INIT__
       () METHOD TO CREATE AN EMPTY LIST OBJECT AS INSTANCE OBJECT MAMBER OF DEQUE.

       2.DEFINE A METHOD IS EMPTY() TO CHECK IFF THE DEQUE IS EMPTY IN DEQUE CLASS

       3.IN DEQUE CLASS DEFINE INSERT_FRONT() METHOD TO ADD DATA AT FRONT AND THE TREE OF THE DEQUE.

       4.IN CLASS DEQUE DEFINE INSERT_REAR() METHOD TO ADD DATA AT THE REAR END OF THE DEQUE

       5.IN DEQUE CLASS .DEFINE DELETE_FRONT() METHOD TO REMOVE FRONT ELEMENT FROM THE LIST

       6.IN DEQUE CLASS .DEFINE DELETE_REAR() METHOD TO REMOVE REAR ELEMENT FROM THE LIST

       7.IN DEQUE_CLASS DEFINE GET_FRONT() METHOFD TO RETURN FRONT ELEMENT OF THE DEQUE

       8.IN DEQUE_CLASS DEFINE GET_REAR() METHOFD TO RETURN REAR ELEMENT OF THE DEQUE

       9.IN DEQUE CLASS ,DEFINE SIZE() METHOD TO RETURN SIZE() OF THE DEQUE THAT IS NUMBER OF ITEM PRESENT IN DEQUE

       10.IN DEQUE CLASS DEFINE PRINT_DEQUE() METHOD TO PRINT ALL ELEMENT IN  DEQUE






"""

class Deque:
    def __init__(self):   ###1-----
        self.item=[]

    def is_empty(self):   ##2------
        return len(self.item)==0

    def insert_front(self, data):   #3-----
        self.item.insert(0, data)
    
    def insert_rear(self, data): ##4-----
        self.item.append(data)
 
    def delete_front(self):   ###5-----
        if not self.is_empty():
            self.item.pop(0)
        else:
            raise IndexError("Deque is empty")

    def delete_rear(self):   ##6-------
        if not self.is_empty():
            self.item.pop()
        else:
            raise IndexError("Deque is empty")

    def get_front(self):   ###7------
        if not self.is_empty():
            return self.item[0]
        else:
            raise IndexError("Deque is empty")

    def get_rear(self):  ###8--------
        if not self.is_empty():
            return self.item[-1]
        else:
            raise IndexError("Deque is empty")

    def size(self):  ####9--------
        return len(self.item)

    def print_deque(self):  ### 10---------
        print(self.item)


d1 = Deque()
d1.insert_front(10)
d1.insert_front(20)
d1.insert_rear(30)
d1.insert_rear(40)
d1.print_deque()
print(d1.get_front())
print(d1.get_rear())