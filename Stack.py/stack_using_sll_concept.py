"""

     1.DEFINE A CLASS STACK DATA STRUCTURE USING SINGLY LINK LIST CONCEPT.DEFINE INIT() METHOD TO INITIALISE START REFERENCE VARIABLE AND ITEM_COUNT VARIABLE TO KEEP TRACK OF NUMBER OF ELEMENTS IN THE STACK
     2.DEFINE A METHIOD IS_EMPTY() TO CHECK IF THE STACK IS EMPTY IN STACK CLASS
     3.IN STACK CLASS,DEFINE PUSH() METHOD TO ADD DATA ONTO THE STACK
     4.IN STACK CLASS DEFINE POP() METHOD TO REMOVE TOP ELEMENT FROM THE STACK
     5.IN SATCK CLASS DEFINE PEEK() METHOD TO RETURN TOP ELEMENT ON THE STACK
     6.IN STACK CLASS DEFINE SIZE() METHOD TO RETURN SIZE OF THE STACK THAT IS NUMBER OF ITEMS PRESENT IN STACK
     7.how to print alll element in stack extend sll


"""

class Node:
  def __init__(self,item=None,next=None):
    self.item=item
    self.next=next

class stack:
  def __init__(self):
    self.start=None
    self.item_count=0

  def is_empty(self):
    return self.start==None or self.item_count==0

  def push(self,data):
    n=Node(data,self.start)
    self.start=n
    self.item_count+=1

  def pop(self):
    if not self.is_empty():
      data=self.start.item
      self.start=self.start.next
      self.item_count-=1
      return data
    else:
      raise IndexError("Stack is empty")

  def peek(self):
    if not self.is_empty():
      return self.start.item
    else:
      raise self.is_empty("Stack is empty")

  def size(self):
    return self.item_count

  def print(self):
    if not self.is_empty():
      temp=self.start
      while temp:
        print(temp.item,end="<-> ")
        temp=temp.next
    else:
      raise self.is_empty("Stack is empty")

s1=stack()
s1.push(10)
s1.push(20)
s1.push(30)
print("total element is ",s1.size())
print("peek element is ",s1.peek())
print("pop element is ",s1.pop())
print("all element is",s1.print())
s1.print()







