"""
1.define a class stack to implement stack data structure by inherit list class

2.define a method is_empty() to check if the stack is empty in stack class

3.in stack class define push() method to add data onto the stack

4.in stack class define pop() method to remove top elemen tfrom the stack

5.in stack class define peek() method to return top element on the stack

6.in stack class define size() method to return size of the stack that is number of items present in the stack

7.implement a way to restrict use() of insert method of list class from the stack object



"""
"""
class List:
    def __init__(self):
        self.data = []

    def append(self, item):
        self.data.append(item)

    def insert(self, index, item):
        self.data.insert(index, item)

    def pop(self):
        if self.data:
            return self.data.pop()
        else:
            return None

    def remove(self, item):
        if item in self.data:
            self.data.remove(item)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        return self.data[index]

    def __setitem__(self, index, value):
        self.data[index] = value

    def __str__(self):
        return str(self.data)

# Example usage:
my_list = List()
my_list.append(1)
my_list.append(2)
my_list.insert(1, 3)
print(my_list)  # Output: [1, 3, 2]

print(my_list[1])  # Output: 3

my_list.remove(2)
print(my_list)  # Output: [1, 3]

print(len(my_list))  # Output: 2

"""

"""--INVIDUAL CLASS LIST IN OOPS


class List:
    def __init__(self):
        self.list = []

    def append(self, data):
        self.list.append(data)

    def pop(self):
        if len(self.list) > 0:
            return self.list.pop()
        else:
            raise IndexError("List is empty")

    def size(self):
        return len(self.list)

    def print_list(self):
        print(self.list)



"""

# Example usage:

class stack(list):  ## stack is the child class of list

  def is_empty(self):  ## SELF IS ALSO OBJECT OF STACK AND LIST
    return len(self)==0

  def push(self,data):  ## self is like a object
    self.append(data)

  def pop(self):
    if not self.is_empty():
       return super().pop()  ## super avoid to infiinite recursion-overriiding--
    else:
      raise IndexError("stack is empty")

  def peek(self):
    if not self.is_empty():
      return self[-1]
    else:
      raise IndexError("stack is empty")

  def size(self):
    return len(self)

#s1.stack()
#s1.insert(1,10)  how to avoid it

  def insert(self,index,data):
    raise AttributeError("no attribute 'insert' in stack" )

  def print_stack(self):
    print(self)



s1=stack() # you can now create a stack without passing any arguments
s1.push(10)
s1.push(20)
s1.push(30)
print(s1.peek())
print(s1.size())
print("removed element from stack is",s1.pop())
print(s1.size())
s1.print_stack()




# # ##stack extending list (1)
# #
# # 1.define a class stack to implement stack data struucture by extending list class
# class stack(list):  ## stack is the child class of list

#   def is_empty(self):  ## SELF IS ALSO OBJECT OF STACK AND LIST
#     return len(self)==0



# # 2.define a method is_empty() to check if the stack is empty in stack class
# class stack(list):  ## stack is the child class of list

#   def is_empty(self):  ## SELF IS ALSO OBJECT OF STACK AND LIST
#     return len(self)==0



# # 3.in stack class define push() method to add data onto the stack
# class stack(list):  ## stack is the child class of list

#   def is_empty(self):  ## SELF IS ALSO OBJECT OF STACK AND LIST
#     return len(self)==0

#   def push(self,data):  ## self is like a object
#     self.append(data)



# # 4.in stack class pop() method to remove top element from the stack
# class stack(list):  ## stack is the child class of list

#   def is_empty(self):  ## SELF IS ALSO OBJECT OF STACK AND LIST
#     return len(self)==0

#   def push(self,data):  ## self is like a object
#     self.append(data)

#   def pop(self):
#     if not self.is_empty():
#        return super().pop()  ## super avoid to infiinite recursion
#     else:
#       raise IndexError("stack is empty")

# """ when same func write in list class and stack class then it is called overriding givess infinite recursion"""



# # 5.in stack class define peek() method to return top element on the stack
# class stack(list):  ## stack is the child class of list

#   def is_empty(self):  ## SELF IS ALSO OBJECT OF STACK AND LIST
#     return len(self)==0

#   def push(self,data):  ## self is like a object
#     self.append(data)

#   def pop(self):
#     if not self.is_empty():
#        return super().pop()  ## super avoid to infiinite recursion
#     else:
#       raise IndexError("stack is empty")

#   def peek(self):
#     if not self.is_empty():
#       return self[-1]
#     else:
#       raise IndexError("stack is empty")


# # 6.in stack class define size() method to return size of the stack that is number of items present in the stack
# class stack(list):  ## stack is the child class of list

#   def is_empty(self):  ## SELF IS ALSO OBJECT OF STACK AND LIST
#     return len(self)==0

#   def push(self,data):  ## self is like a object
#     self.append(data)

#   def pop(self):
#     if not self.is_empty():
#        return super().pop()  ## super avoid to infiinite recursion
#     else:
#       raise IndexError("stack is empty")

#   def peek(self):
#     if not self.is_empty():
#       return self[-1]
#     else:
#       raise IndexError("stack is empty")

#   def size(self):
#     return len(self)

#   def print_stack(self):
#     print(self)


# # 7.implement a way to restrict us eof insert() method of list class from stack object
# class stack(list):  ## stack is the child class of list
#   def __init__(self): # add a default value for items
#     self.stack = []
#   def is_empty(self):  ## SELF IS ALSO OBJECT OF STACK AND LIST
#     return len(self)==0

#   def push(self,data):  ## self is like a object
#     self.append(data)

#   def pop(self):
#     if not self.is_empty():
#        return super().pop()  ## super avoid to infiinite recursion
#     else:
#       raise IndexError("stack is empty")

#   def peek(self):
#     if not self.is_empty():
#       return self[-1]
#     else:
#       raise IndexError("stack is empty")

#   def size(self):
#     return len(self)

# #s1.stack()
# #s1.insert(1,10)  how to avoid it

#   def insert(self,index,data):
#     raise AttributeError("no attribute 'insert' in stack" )

#   def print_stack(self):
#     print(self.stack)

# s1=stack() # you can now create a stack without passing any arguments
# s1.push(10)
# s1.push(20)
# s1.push(30)
# print(s1.peek())
# s1.print_stack() # remove self here
