"""
     1.DEFINE A CLASS NODE TO DESCRIBE A NODE OF A DOUBLY LINK LIST
     2.DEFINE A CLASS DLL WITH REFRENCE THAT INITIALIZE TO THE NODES
     3.DEFINE A method is empty () to check if the linked list is empty in dll class
     4.IN CLASS DLL, DEFINE A METHOD INSERT AT START TO INSEERT AN ELEMENT AT THE STARTING OF THE LIST
     5.IN CLASS DLL, DEFINE A METHOD INSERT AT LAST TO INSEERT AN ELEMENT AT THE ENDING OF THE LIST
     6.IN CLASS DLL DEFINE A METHOD SEARCH () TO FIND THE NODE WITH SPECIFIC ELEMENT VALUE
     7.IN CLASS DLL, DEFINE A MMETHOD INSERT_AFTER () T INSERT A NEWCODE AFTER A GIVEN NODE OF THE LIST
     8.IN CLASS DLL,DEFINE A METHOD TO PRINT ALL THE ELEMENT OF THE LIST
     9.IN CLASS DLL IMPLEMENT ITERATOR FOR DLL TO ACESS ALL THE ELEMENT OF THE LIST IN A SEQUENCE
     10.delete at start
     11.delete at last
     12.delete specific node



"""
class Node:

  def __init__(self,data=None,next=None,prev=None):
    self.data=data
    self.next=next
    self.prev=prev

class DLL:
  def __init__(self,start=None):
    self.start=start

  def is_empty(self):
    return self.start==None

  def insert_at_start(self,data):
    n=Node(None,data,self.start)
    if not self.isempty():
      self.start.prev=n
    self.start=n
  ###insert at last
  def insert_at_last(self,data):
    temp=self.start
    if self.start!=None:
      while temp.next is not None:
        temp=temp.next
    n=Node(temp,data,None)
    if temp==None:
      self.start=n
    else:
      temp.next=n

  ## search

  def saerch(self,data):
    temp=self.start
    while temp is not None:
      if temp.data==data:
        return temp
      temp=temp.next
    return None

  def insert_after(self,temp,data):
    if temp is not None:
      n=Node(temp,data,temp.next)
      if temp.next is not None:
        temp.next.prev=n
      temp.next=n
  ##### print =====

  def print(self):
    temp=self.start  ### TRAVERSING
    while temp is not None:
      print(temp.data,end="<->")
      temp=temp.next

  ## del at start

  def del_start(self):
    if self.start is not None:  ##self.start=node1
      self.start=self.start.next ## SELF.START.NEXT=NODE2
      if self.start is not None:
        self.start.prev=None

  ## DEL LAST

  def delete_last(self):
    if self.start==None:
      pass
    elif self.start.next is None:
      self.start=None
    else:
      temp=self.start
      while temp.next is not None:
        temp=temp.next
      temp.prev.next=None

  ## def delete specific element


  def delete_item(self,data):
    if self.start  is None:
      pass
    else:
      temp=self.start
      # if temp.data==data:  ## if 1 st node will delete
      #   self.start=temp.next
      #   temp.next.prev=None
      while temp is not None:
        if temp.data==data:
          if temp.next is not None:
            temp.next.prev=temp.prev
          if temp.prev is not None:
            temp.prev.next=temp.next
          else:
            self.start=temp.next
          break
        temp=temp.next

















# class Node:

#   def __init__(self,data=None,next=None,prev=None):
#     self.data=data
#     self.next=next
#     self.prev=prev

# class DLL:
#   def __init__(self,start=None):
#     self.start=start

#   def is_empty(self):
#     return self.start==None

#   def insert_at_start(self,data):
#     n=Node(None,data,self.start)
#     if not self.is_empty():
#       self.start.prev=n
#     self.start=n
#   ###insert at last
#   def insert_at_last(self,data):
#     temp=self.start
#     if self.start is not None:
#       while temp.next is not None:
#         temp=temp.next
#     #The first argument to Node is assigned to Node.prev
#     #Change the order of arguments so that temp is assigned to Node.data
#     n=Node(data,None,temp)
#     if temp==None:
#       self.start=n
#     else:
#       temp.next=n

#   ## search

#   def saerch(self,data):
#     temp=self.start
#     while temp is not None:
#       if temp.data==data:
#         return temp
#       temp=temp.next
#     return None

#   def insert_after(self,temp,data):
#     if temp is not None:
#       n=Node(temp,data,temp.next)
#       if temp.next is not None:
#         temp.next.prev=n
#       temp.next=n
#   ##### print =====

#   def print(self):
#     temp=self.start  ### TRAVERSING
#     while temp is not None:
#       print(temp.data,end="<->")
#       temp=temp.next

#   ## del at start

#   def del_start(self):
#     if self.start is not None:  ##self.start=node1
#       self.start=self.start.next ## SELF.START.NEXT=NODE2
#       if self.start is not None:
#         self.start.prev=None

#   ## DEL LAST

#   def delete_last(self):
#     if self.start==None:
#       pass
#     elif self.start.next is None:
#       self.start=None
#     else:
#       temp=self.start
#       while temp.next is not None:
#         temp=temp.next
#       temp.prev.next=None

#   ## def delete specific element

#   def delete_item(self,data):
#     if self.start  is None:
#       pass
#     else:
#       temp=self.start
#       # if temp.data==data:  ## if 1 st node will delete
#       #   self.start=temp.next
#       #   temp.next.prev=None
#       while temp is not None:
#         if temp.data==data:
#           if temp.next is not None:
#             temp.next.prev=temp.prev
#           if temp.prev is not None:
#             temp.prev.next=temp.next
#           else:
#             self.start=temp.next
#           break
#         temp=temp.next

# ###### how to form iterator
#   def __iter__(self):
#     return DLLiterator(self.start)

# class DLLiterator:
#   def __init__(self,start):
#     self.current=start

#   def __iter__(self):
#     return self
