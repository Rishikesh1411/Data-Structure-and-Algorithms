"""
      1.define a class node to describe a node of circular doubly link list
      2.define a cdll to implement circular linked list with init() method to create and initialise start referense veriable
      3.define a method is_empty() to check if the linked list is empty in cdll class
      4.in class cdll define a method inser_at _start() to insert an element at the starting of the list
      5.in class cdll define a method insert_at_last() to insert an element at the end of the list
      6.in class cdll ,define a method search () to find the node with specified element value
      7.in class cdll,define a method insert_after() to insert a newcode after a given node of the list
      8.in class cdll,define a method to print all the element of tjhe list
      9.in class cdll,implement iterator for sll to access all the element of the list in a sequence
      10.in class cdll define a method delete_first() to delete first element from the list
      11.in class cdll,define a method delete_last() to delete last element from list
      12.delete the item in between the cll list



"""



class Node:
  def __init__(self,data=None,next=None,prev=None):
    self.data=data
    self.next=next
    self.prev=prev

class CDLL:
  def __init__(self,start=None):
    self.start=start

  def is_empty(self):
    return self.start==None


  def insert_at_start(self,data):
    n=Node(data)
    if self.start==None:
      n.next=n
      n.prev=n
    else:
      n.next=self.start
      n.prev=self.start.prev
      self.start.prev.next=n
      self.start.prev=n
    self.start=n

  def insert_at_last(self,data):
    n=Node(data)
    if self.start==None:
      n.next=n
      n.prev=n
      self.start=n
    else:
      n.next=self.start
      n.prev=self.start.prev
      n.prev.next=n
      self.start.prev=n

  def search(self,data):
    temp=self.start
    if temp==None:
      return None
    if temp.data==data:
      return temp
    else:
      temp=temp.next

    while temp!=self.start:
      if temp.data==data:
        return temp
      temp=temp.next
    return None

  def insert_after(self,temp,data):
    if temp is not None:
      n=Node(data)
      n.next=temp.next
      n.prev=temp
      temp.next.prev=n
      temp.next=n

  def print(self):
    temp=self.start
    if temp is not None:
      print(temp.data,end='<->')
      temp=temp.next
      while temp is not self.start:
        print(temp.data,end="<->")
        temp=temp.next

  def del_first(self):
    if self.start is not None:
      if self.start.next==self.start:
        self.start=None
      else:
        self.start.prev.next=self.start.next
        self.start.next.prev=self.start.prev
        self.start.next=self.start

  def del_last(self):
    if self.start is not None:
      if self.start.next==self.start:
        self.start=None
      else:
        self.start.prev.prev.next=self.start
        self.start.prev=self.start.prev.prev

  def del_item(self,data):
    if self.start is not None:
        temp=self.start
        if temp.data==data:
          self.del_first()
        else:
          temp=temp.next
          while temp is not self.start:
            if temp.data==data:
              temp.next.prev=temp.prev
              temp.prev.next=temp.next


mylist=CDLL()
mylist.insert_at_start(10)
mylist.insert_at_last(20)
mylist.insert_at_last(30)
mylist.insert_at_last(40)
mylist.insert_after(mylist.search(30),35)
mylist.print()





"""
class Node:
  def __init__(self,data=None,next=None,prev=None):
    self.data=data
    self.next=next
    self.prev=prev

class CDLL:
  def __init__(self,start=None):
    self.start=start

  def is_empty(self):
    return self.start==None


  def insert_at_start(self,data):
    n=Node(data)
    if self.start==None:
      n.next=n
      n.prev=n
    else:
      n.next=self.start
      n.prev=self.start.prev
      self.start.prev.next=n
      self.start.prev=n
    self.start=n

  def insert_at_last(self,data):
    n=Node(data)
    if self.start==None:
      n.next=n
      n.prev=n
      self.start=n
    else:
      n.next=self.start
      n.prev=self.start.prev
      n.prev.next=n
      self.start.prev=n

  def search(self,data):
    temp=self.start
    if temp==None:
      return None
    if temp.data==data:
      return temp
    else:
      temp=temp.next

    while temp!=self.start:
      if temp.data==data:
        return temp
      temp=temp.next
    return None

  def insert_after(self,temp,data):
    if temp is not None:
      n=Node(data)
      n.next=temp.next
      n.prev=temp
      temp.next.prev=n
      temp.next=n

  def print(self):
    temp=self.start
    if temp is not None:
      print(temp.data,end='<->')
      temp=temp.next
      while temp is not self.start:
        print(temp.data,end="<->")
        temp=temp.next

  def del_first(self):
    if self.start is not None:
      if self.start.next==self.start:
        self.start=None
      else:
        self.start.prev.next=self.start.next
        self.start.next.prev=self.start.prev
        self.start.next=self.start

  def del_last(self):
    if self.start is not None:
      if self.start.next==self.start:
        self.start=None
      else:
        self.start.prev.prev.next=self.start
        self.start.prev=self.start.prev.prev

  def del_item(self,data):
    if self.start is not None:
        temp=self.start
        if temp.data==data:
          self.del_first()
        else:
          temp=temp.next
          while temp is not self.start:
            if temp.data==data:
              temp.next.prev=temp.prev
              temp.prev.next=temp.next


  def __iter__(self):
    return CDLLIterator(self.start)

class CDLLIterator:

  def __init__(self,start):
    self.current=start
    self.start=start
    self.count=0

  def __iter__(self):
    return self

  def __next__(self):
    if self.current is None:
      raise StopIteration
    if self.current==self.start and self.count==1:
      raise StopIteration
    else:
      self.count=1
      data=self.current.data
      self.current=self.current.next
      return data

mylist=CDLL()
mylist.insert_at_start(10)
mylist.insert_at_last(20)
mylist.insert_at_last(30)
mylist.insert_at_last(40)
mylist.insert_after(mylist.search(30),35)

for x in mylist:
  print(x,end="<->")

print()





"""



