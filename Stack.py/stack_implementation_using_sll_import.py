"""

            1.IMPORT MODULE CONTAINING SINGLE LINKED LIST IN YOUR PYTHON FILE
            2.DEFINE A CLASS STACK TO IMPLEMENT STACK DATA STRUCTURE .DEFINE INIT() METHOD TO CREATE SINGLY LINKED LIST(SLL) OBJECT.
            3.DEFINE A METHOD IS_EMPTY() TO CHECK IF THE STACK IS EMPTY IN STACK CLASS
            4.IN CLASS STACK DEFINE PUSH() METHOD TO ADD DATA ONTO THE STACK
            5.IN STACK CLASS ,DEFINE POP() METHOD TO REMOVE TOP ELEMENT FROM THE STACK
            6.IN STACK CLASS DEFINE PEEK() METHOD TO RETURN TOP ELEMENT ON THE STACK
            7.IN STACK CLASS DEFIENE SIZE() METHOD TO RETURN SIZE OF THE STACK THAT IS NUMBER OF ITEMS PRESENT IN THE STACK



"""





from sll_class import *
###stack_implement_using_sll.py
class Stack:

    def __init__(self):
        self.mylist = SLL()
        self.count_item=0

    def is_empty(self):
        return self.mylist.is_empty()  or  self.count_item==0


    def push(self,data):
       self.count_item += 1
       self.mylist.insert_at_start(data) 


    def pop(self):
        if not self.is_empty():
            self.count_item -= 1
            self.mylist.del_first()

    def peek(self):
        if not self.is_empty():
            return self.mylist.start.data

    def size(self):
        return  self.count_item

    def print(self):
        self.mylist.print_list()


s=Stack()
s.push(10)
s.push(20)
s.push(30)
print("top element is",s.peek())
s.pop()
print("top element is",s.peek())
s.print()






        