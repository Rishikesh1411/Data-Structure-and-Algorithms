"""
       ASSIGNMENT -17

       1.DEFINE A NODE CLASS WITH INSTANCE MEMBER VERIABLE ITEM PRIORITY AND NEXT

       2.DEFIEN A CLASS PRIORITYQUEUE TO IMPLEMENT PRIORITY QUEUE DATA STRUCTURE USING SINGLY LINK LIST .PROVIDE __INIT__()
        METHOD TO CREATE A START REFRENCE VERIABLE (INITIALLY CONTAINING NONE) AN D(ITEM_COUNT==0 I INITIALLY)
       
       3.DEFINE A PUSH() METHOD IN PRIORITY QUEUE CLASS TO INSERT NEW DATA WITH GIVEN PRIORITY.

       4.DEFINE A PIOP METHOD IN PRIORITY QUEUE CLASSS WHICH RETURNS THE HIGHEST PRIORITY DATA
        STORED IN THEN PRIORITY QUEUE DATA STRUCTURE .RAISE EXCEPTION IF PRIOROITY QUEUE IS EMPTY.

       5.DEFINE A IS_EMPTY() METHOD IN PRIORITY QUEUE CLASS TO CHECK IF THE PRIORITY QUEUE IS EMPTY()

       6.IN CLASS PRIORITYQUEUE,DEFINE A METHOOD SIZE() TO RETURN THE NUMBER OF ELEMENTS PRESENT IN THE PRIORITY QUEUE



"""

class Node:  ####1--
    def __init__(self, item, priority):
        self.item = item
        self.priority = priority
        self.next = None


class  PriorityQueue:  ####2--
    def __init__(self):
        self.start = None
        self.item_count=0

    
    def push(self,data, priority): # ####3----
        new_node = Node(data, priority)       ## priority of first element is min than new node data
        if not self.start  or priority<self.start.priority:
            new_node.next=self.start
            self.start=new_node
        else:
            current=self.start
            while current.next  and current.next.priority<=priority:
                current = current.next
            new_node.next=current.next   
            current.next=new_node
        self.item_count+=1

        
    def is_empty():  ###5-----
        return self.item_count==0 or self.start==None

    

    def pop(self): ##4---
        if self.is_empty():
            raise Exception("Priority Queue is empty")      
        data=self.start.item
        self.start=self.start.next
        self.item_count-=1
        return data


    def  size(self): ##6---
        return self.item_count

    def print_p(self):
        current = self.start
        while current:
            print(f"data is {current.item} and index is  {current.priority}")
            current=current.next
        print()



p1=PriorityQueue()
p1.push(1, 3)
p1.push(2, 1)
p1.push(3, 2)
print(p1.size())  # Output: 3
p1.print_p()


p=PriorityQueue()
p.push("amit",6)
p.push("vivek",4)
p.push("rishi",0)
p.print_p()






            


          

           



