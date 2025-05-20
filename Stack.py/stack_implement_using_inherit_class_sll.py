""" 

     1.IMPORT MODULE CONTAINING SINGLY LINKED LIST CODE IN YOUR PYTHON FILE
     2.DEFINE A CLASS STACK TO IMPLEMENT STACK DATA STRUCTURE BY INHERITING SLL CLASS
     3.DEFINE A METHOD IS_EMPTY() TO CHECK IF THE STACK IS EMPTY IN STACK CLASS
     4.IN STACK CLASS DEFINE PUSH() METHOD TO ADD DATA ONTO THE STACK
     5.IN STACK CLASS DEFINE POP() METHOD TO REMOVE TOP ELEMENT FROM THE STACK
     6.IN SATCK CLASS DEFINE PEEK() METHOD TO RETURN TOP ELEMENT ON THE STACK
     7.IN STACK CLASS DEFINE SIZE() METHOD TO RETURN SIZE OF THE STACK THAT IS NUMBER OF ITEMS PRESENT IN THE STACK





"""

from sll_class import *

class Stack(SLL):

    def __init__(self):
        super().__init__()
        self.item_count=0
    
    def is_empty():
        return super().is_empty()

    def push(self,data):
        self.insert_at_start(data)
        self.item_count+=1

    def pop(self):
        if not super().is_empty():
            self.del_first()
            self.item_count-=1
        else:
            raise IndexError("stack is empty")

    def peek(self):
        if not super().is_empty():
            return self.start.data
        else:
            raise IndexError("stack is empty")

    def size(self):
        return self.item_count

    def print(self):
        self.print_list()


s1=Stack()
s1.push(10)
s1.push(20)
s1.push(30)
s1.push(40)
s1.push(50)
s1.print()
print("top element on the stack is : ",s1.peek())
s1.pop()
print("top element on the stack:",s1.peek())


    

        

