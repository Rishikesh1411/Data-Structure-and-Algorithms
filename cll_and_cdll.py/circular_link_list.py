"""
      1.define a class node to describe a node of circular link list
      2.define a cll to implement circular linked list with init() method to create and initialise start referense veriable
      3.define a method is_empty() to check if the linked list is empty in cll class
      4.in class cll define a method inser_at _start() to insert an element at the starting of the list
      5.in class cll define a method insert_at_last() to insert an element at the end of the list
      6.in class cll ,define a method search () to find the node with specified element value
      7.in class cll,define a method insert_after() to insert a newcode after a given node of the list
      8.in class cll,define a method to print all the element of tjhe list
      9.in class cll,implement iterator for sll to access all the element of the list in a sequence
      10.in class cll define a method delete_first() to delete first element from the list
      11.in class cll,define a method delete_last() to delete last element from list
      12.delete the item in between the cll list
 


"""

class Node:
  def __init__(self,item=None,next=None):
    self.item=item
    self.next=next

class CLL:
  def __init__(self,last=None):
    self.last=last


  def is_empty(self):
    return self.last==None

  def insert_at_start(self,data):
    n=Node(data)
    if self.is_empty():
      n.next=n
      self.last=n
    else:
      n.next=self.last.next
      self.last.next=n

  def insert_at_last(self,data):
    n=Node(data)
    if self.is_empty():
      n.next=n
      self.last=n
    else:
      n.next=self.last.next
      self.last.next=n
      self.last=n  ## due to n will last node so veriable will change

  def search(self,data):
    if self.is_empty():
      return None
    temp=self.last.next
    while temp!=self.last:
      if temp.item==data:
        return
      temp=temp.next
    if temp.item==data:
      return temp
    return None

  def insert_after(self,temp,data):
    if temp is not None:
      n=Node(data,temp.next)
      temp.next=n
      if temp==self.last:
        self.last=n


  def print_list(self):
    if not self.is_empty():
      temp=self.last.next
      while temp!=self.last:
          print(temp.item,end='<->')
          temp=temp.next
      print(temp.item)

  def del_first(self):
    if not self.is_empty():
      if self.last.next==self.last:
        self.last=None
      else:
        self.last.next=self.last.next.next

  def del_last(self):
    if not self.is_empty():
      self.last=None
    else:
      temp=self.last.next
      while temp.next!=self.last:
        temp=temp.next
      temp.next=self.last.next
      temp=self.last

  def del_item(self,data):
    if not  self.is_empty():
      if self.last.next==self.last:
        if self.last.item==data:
          self.last=None

      else:
        if self.last.next.item==data:
          self.del_first()
        else:
          temp=self.last.next
          while temp!=self.last:
            if temp.next==self.last:
              self.del_last()
              break
            if temp.next.item==data:
              temp.next=temp.next.next
              break
            temp=temp.next


cll=CLL()
cll.insert_at_start(10)
cll.insert_at_start(20)
cll.insert_at_last(30)
cll.insert_at_last(40)
cll.insert_after(cll.search(10),50)
cll.print_list()






"""
class Node:
  def __init__(self,item=None,next=None):
    self.item=item
    self.next=next

class CLL:
  def __init__(self,last=None):
    self.last=last


  def is_empty(self):
    return self.last==None

  def insert_at_start(self,data):
    n=Node(data)
    if self.is_empty():
      n.next=n
      self.last=n
    else:
      n.next=self.last.next
      self.last.next=n

  def insert_at_last(self,data):
    n=Node(data)
    if self.is_empty():
      n.next=n
      self.last=n
    else:
      n.next=self.last.next
      self.last.next=n
      self.last=n  ## due to n will last node so veriable will change

  def search(self,data):
    if self.is_empty():
      return None
    temp=self.last.next
    while temp!=self.last:
      if temp.item==data:
        return
      temp=temp.next
    if temp.item==data:
      return temp
    return None

  def insert_after(self,temp,data):
    if temp is not None:
      n=Node(data,temp.next)
      temp.next=n
      if temp==self.last:
        self.last=n


  def print_list(self):
    if not self.is_empty():
      temp=self.last.next
      while temp!=self.last:
          print(temp.item,end='<->')
          temp=temp.next
      print(temp.item)

  def del_first(self):
    if not self.is_empty():
      if self.last.next==self.last:
        self.last=None
      else:
        self.last.next=self.last.next.next

  def del_last(self):
    if not self.is_empty():
      self.last=None
    else:
      temp=self.last.next
      while temp.next!=self.last:
        temp=temp.next
      temp.next=self.last.next
      temp=self.last

  def del_item(self,data):
    if not  self.is_empty():
      if self.last.next==self.last:
        if self.last.item==data:
          self.last=None

      else:
        if self.last.next.item==data:
          self.del_first()
        else:
          temp=self.last.next
          while temp!=self.last:
            if temp.next==self.last:
              if self.last.item==data:
                self.del_last()
              break
            if temp.next.item==data:
              temp.next=temp.next.next
              break
            temp=temp.next

  def __iter__(self):
    if self.last==None:
      return CLLiterator(None)
    else:
      # Return an instance of the iterator, not the class itself
      return CLLiterator(self.last.next)

class CLLiterator:
  def __init__(self,start):
    self.current=start
    self.first=start

  def __iter__(self):
    return self

  def __next__(self):
    if self.current==None:
      raise StopIteration
    data=self.current.item
    self.current=self.current.next
    # Compare with self.first to stop after a full circle
    if self.current==self.first:
       raise StopIteration

    return data




cll=CLL()
cll.insert_at_start(10)
cll.insert_at_start(20)
cll.insert_at_last(30)
cll.insert_at_last(40)
cll.insert_after(cll.search(10),50)
## 20 10 50 30 40

for x in cll:
  print(x,end=' ')
print()















"""




