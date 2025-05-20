## sll--
### creation of node----
class Node:
    def __init__(self,data=None):  #### instance method/constructor
        self.data = data        
        self.next = None

    ### function  ---

def print_sll(temp):
    while(temp):
        print(temp.data)
        temp = temp.next

## object of  node class

node1=Node(10)
node2=Node(20)
node3=Node(30)
node4=Node(40)


### connection of nodes--
node3.next=node2
node2.next=node1
node1.next=node4

print(node2.next.data)


print_sll(node3)


### print--

# temp=node1
# while temp:
#     print(temp.data)
#     temp=temp.next



""" 
   1.deletion
   2.insertion
   3.is_empty
   4.traversing


"""


