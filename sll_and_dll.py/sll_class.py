####stack_implement_using_sll.py
"""
    1.define a class node to describe a node of singly link list
    2.define a sll to implement singly linked list with init() method to create and initialise start referense veriable
    3.define a method is_empty() to check if the linked list is empty in sll class
    4.in class sll define a method inser_at _start() to insert an element at the starting of the list
    5.in class sll define a method insert_at_last() to insert an element at the end of the list
    6.in class sll ,define a method search () to find the node with specified element value
    7.in class sll,define a method insert_after() to insert a newcode after a given node of the list
    8.in class sll,define a method to print all the element of tjhe list
    9.in class sll,implement iterator for sll to access all the element of the list in a sequence
    10.in class sll define a method delete_first() to delete first element from the list
    11.in class sll,define a method delete_last() to delete last element from list
    12.delete the item in between the sll list




"""

class Node:
  def __init__(self,data=None,next=None):
    self.data=data
    self.next=next

class SLL:

  def __init__(self,start=None):
    self.start=start

  def is_empty(self):
     return self.start==None

  def insert_at_start(self,data):
    n=Node(data)
    n.next=self.start
    self.start=n
    

  def insert_at_last(self,data):
    newnode=Node(data)
    if not self.is_empty():
      temp=self.start
      while temp.next is not None:
        temp=temp.next
      temp.next=newnode
    else:
      self.start=newnode

  def search(self,value):
    temp=self.start
    while temp is not None:
      if temp.data==value:
        return temp
      temp=temp.next
    return None

  def insert_after(self,data,temp):
    if temp is not None:
      n=Node(data,temp.next)
      temp.next=n

  def print_list(self):
    temp=self.start
    while temp is not None:
      print(temp.data,end='->')
      temp=temp.next

  def del_first(self):
    if self.start is not None:
      self.start=self.start.next

  def del_last(self):
    if self.start is None:
      pass
    elif self.start.next is None:
      self.start=None
    else:
      temp=self.start
      while temp.next.next is not None:
        temp=temp.next
      temp.next=None

  def del_data(self,data):
    if self.start is None:
      pass
    elif self.start.next is None :
      if self.start.data==data:
        self.start=None
    else:
      temp=self.start
      if temp.data==data:
        self.start=temp.next
      else:
        while temp.next is not None:
          if temp.next.data==data:
            temp.next=temp.next.next
            break

          temp=temp.next


mylist=SLL()
mylist.insert_at_start(30)
mylist.insert_at_start(20)
mylist.insert_at_last(40)
mylist.insert_after(25,mylist.search(20))
mylist.print_list()
mylist.del_data(30)
mylist.print_list()


"""
####9.in class sll,implement iterator for sll to access all the element of the list in a sequence


class Node:
  def __init__(self,data=None,next=None):
    self.data=data
    self.next=next

class SLL:

  def __init__(self,start=None):
    self.start=start

  def is_empty(self):
     return self.start==None

  def insert_at_start(self,data):
    n=Node(data,self.start)
    self.start=n

  def insert_at_last(self,data):
    newnode=Node(data)
    if not self.is_empty():
      temp=self.start
      while temp.next is not None:
        temp=temp.next
      temp.next=newnode
    else:
      self.start=newnode
  def search(self,value):
    temp=self.start
    while temp is not None:
      if temp.data==value:
        return temp
      temp=temp.next
    return None

  def insert_after(self,data,temp):
    if temp is not None:
      n=Node(data,temp.next)
      temp.next=n

  def print_list(self):
    temp=self.start
    while temp is not None:
      print(temp.data,end='->')
      temp=temp.next

  def __iter__(self):
    return SLLIterator(self.start)

class SLLIterator:
  def __init__(self,start):
    self.current=start

  def __iter__(self):
    return self

  def __next__(self):
    if not self.current:
      raise StopIteration
    data=self.current.data
    self.current=self.current.next
    return data


mylist=SLL()
mylist.insert_at_start(30)
mylist.insert_at_start(20)
mylist.insert_at_last(40)
mylist.insert_after(25,mylist.search(20))

mylist.print_list()
for x in mylist:
  print(x,end='')

print()







"""