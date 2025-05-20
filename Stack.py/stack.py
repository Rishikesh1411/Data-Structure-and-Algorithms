"""
     1.DEFINE A CLASS STACK TO IMPLEMENT STACK DATA STRUCTURE USING LIST ,DEFINE INIT() METHOD TO CREATE AN EMPTY LIST OBJECT AS INSTANCE OBJECT MEMEBER OF OBJECT
     2.DEFINE A METHOD IS_EMPTY() TO CHECK IF THE STACK IS EMPTY IN STACK CLASS
     3.IN STACK CLASS DEFINE PUSH() METHOD TO ADD DATA ONTO THE STACK
     4.IN CLASS STACK DEFINE POP() METHOD TO REMOVE TOP ELEMENT FROM THE STACK
     5.IN STACK CLASS DEFINE PEEK() METHOD TO RETURN TOP ELEMENT ON THE STACK
     6.IN STACK CLASS DEFINE SIZE () METHOD TO RETURN SIZE OF THE STACK THAT IS NUMBER OF ITEMS PRESENT IN THE STACK
     7.implement a way to restrict us eof insert() method of list class from stack object


"""
class stack(list):  ## stack is the child class of list

  def __init__(self): # add a default value for items
    self.stack = []

  def is_empty(self):  ## SELF IS ALSO OBJECT OF STACK AND LIST
    return len(self)==0


  def push(self,data):  ## self is like a object
    self.append(data)

  def pop(self):
    if not self.is_empty():
       return super().pop()  ## super avoid to infiinite recursion
    else:
      raise IndexError("stack is empty")

  def peek(self):
    if not self.is_empty():
      return self[-1]
    else:
      raise IndexError("stack is empty")



  def size(self):
    return len(self)

  def print_stack(self):
    print(self)

#s1.stack()
#s1.insert(1,10)  how to avoid it

  def insert(self,index,data):
    raise AttributeError("no attribute 'insert' in stack" )

s1=stack() # you can now create a stack without passing any arguments
s1.push(10)
s1.push(20)
s1.push(30)
print(s1.peek())
s1.print_stack()
print("the len of  stack is",s1.size())
