class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

    
class Sll:
    def __init__(self,start):
        self.start=None
        self.item_count=0

    def is_empty(self):
        return self.start==None or  self.item_count==0

    def insert_at_start(self,data):
        n=Node(data)
        if  self.is_empty():
            self.start=n
        else:
            n.next=self.start
            self.start=n

    
    def insert_at_last(self,data):
        n=Node(data)
        if self.is_empty():
            self.start=n
        else:
            curr=self.start
            while curr.next is not None:
                curr=curr.next
            n.next=curr.next
            curr.next=n
            



