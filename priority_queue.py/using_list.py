### priority queue using list--
"""
   ASSIGNMENT-16


   1.DEFINE A PRIORITY QUEUE TO IMPLEMENT PRIORITY QUEUE DATA STRUCTURE USING LIST .
   PROVIDE __INIT__() METHOD TO CREATE A LIST OBJECT (INITIALLY EMPTY).

   2.DEFINE A PUSH METHOD() IN PRIORITY QUEUE CLASS TO INSERT NEW DATA WITH GIVEN PRIORITY

   3.DEFINE A POP METHOD IN PRIRITY QUEUE CLASS,WHICH RETURNS  THE HIGHEST PRIORITY DATA STORED 
    IN THE PRIORITY QUEUE DATA STRUCTURE RAISE EXCEPTION IF PRIORITY QUEUE IS EMPTY.

   4.DEFINE  A IS_EMPTY() METHOD IN PRIORITY QUEUE CLASS TO CHECK IF THE PRIORITY QUEUE IS EMPTY.

   5.IN CLASS PRIRITY QUEUE DEFINE A METHOD SIZE() TO RETURN THE NUMBER OF ELEMENTS
   PRESENT IN THE PRIORITY QUEUE.



   A.ON THE BASE OF RANK-WHICH RANK IS LOW WHOSE PRIRITY WILL HIGH

   B.ON THE BASIS OF NUM-WHICH  NUM IS LOW WHOSE PRIRITY WILL LOW



"""

class priorityqueue:##======1
    def __init__(self):
        self.items=[]


    def push(self,data,priority_no):  ###2------
        idx=0
        while idx<len(self.items) and self.items[idx][1]<=priority_no:
            idx+=1
        self.items.insert(idx,(data,priority_no))

    def is_empty(self):##4---
        return len(self.items)==0

    
    def pop(self):  ## 3-in the  case of rank-highest priority element held on first index 
        if self.is_empty():
            raise Exception("Priority Queue is Empty")
        else:
            return self.items.pop(0)[0]

    def size(self):###5------
        return  len(self.items)

    def print_q(self):
        print(self.items)


p1=priorityqueue()
p1.push(10,5)
p1.push(20,3)
p1.push(30,7)
p1.push(40,9)
p1.print_q()
p1.pop()
p1.print_q()


p=priorityqueue()
p.push("amit",6)
p.push("vivek",4)
p.push("rishi",0)
p.print_q()
print(p1.is_empty())
print(p1.size())


        


