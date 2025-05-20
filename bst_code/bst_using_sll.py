"""
   ASSIGNMENT-20

   1.DEFINE A CLASS NODE WITH INSTANCE VERIABLE ,LEFT RIGHT AND ITEM .THE VERIABLE LEFT AND RIGHT ARE USED 
    TO REFER LEFT AND RIGHT CHILD NODE.THE  ITEM VERIABLE IS USED TO HOLD DATA ITEM

   2.DEFINE A CLASS BST  to implement binary search tree DATA STRUCTURE .MAKE __INIT__()
   METHOD TO CREATE ROOT INSTANCE VERIABLE TO HOLD THE REFERENCE OF ROOT NODE.

   3.IN CLASS BST ,DEFINE INSERT METHOD TO STORE NEW DATA ITEM IN THE BINARY SEARCH TREE

   4.IN CLASS BST DEFIEN SEARCH METHOD TO FIND A GIVEN ITEM IN  THE BINARY SAERCH TREE
    AND RETURNS THE NODE REFERENCE.IT RETURNS NONE IF SEARCH FAILS

   
   5.IN CLASS BST ,DEFINE A METHOD TO IMPLEMENT INORDER TRAVERSAL

   6.IN CLASS BST ,DEFINE A METHOD TO IMPLEMENT PRE-ORDER TRAVERSAL


   7.IN CLASS BST ,DEFINE A METHOD TO IMPLEMENT POST-ORDER TRAVERSAL


  ASSIGNMENT-21

  1. IN CLASS BST ,DEFINE A METHOD TO FIND MINIMUM VALUE ITEM NODE

  2.IN CLASS BST DEFINE A METHOD TO FIND MAXIMUM VALUE ITEM NODE

  3.IN CLASS BST DEFINE A METHOD TO DELETE A NODE FROM BINARY SEARCH TREE

  4.IN CLASS BST DEFIEN A METHOD SIZE TO RETURN THE NUMBER OF ELEMENTS PRESENTS IN THE BST





"""

class TreeNode:  ######1------
    def __init__(self, item=None):
        self.item=item
        self.left=None
        self.right=None


class BST:  ####2------- its holds (root veriable) the reference of root node
    def __init__(self,root=None):
        self.root=root
        

    def insert(self,data):  ###3----------------
        self.root=self.rinsert(self.root,data)

    def rinsert(self,root,data):
        if root is None:
            return TreeNode(data)
        if data<root.item:
            root.left=self.rinsert(root.left,data)
        elif data>root.item :
            root.right = self.rinsert(root.right,data)
        return root

    
    def search(self, data):  ###4----------------
        return self.rsearch(self.root,data)

    def rsearch(self,root,data):
        if root  is None or root.item==data:
            return root           
        if  data<root.item:
            
            return self.rsearch(root.left,data)
        elif data> root.item:
            return  self.rsearch(root.right,data)

    
    def inorder_traversal(self): ###5-----
        result =[]
        self.rinorder_traversal(self.root,result)
        return result

    def rinorder_traversal(self,root,result):
        if root :
            self.rinorder_traversal(root.left,result)
            result.append(root.item)
            self.rinorder_traversal(root.right,result)
    

    
    def pre_order_traversal(self): ###6-----
        result =[]
        self.rpre_order_traversal(self.root,result)
        return result

    def rpre_order_traversal(self,root,result):
        if root :
            result.append(root.item)
            self.rpre_order_traversal(root.left,result)          
            self.rpre_order_traversal(root.right,result)


    
    def post_order_traversal(self): ###7-----
        result =[]
        self.rpost_order_traversal(self.root,result)
        return result

    def rpost_order_traversal(self,root,result):
        if root :
            self.rpost_order_traversal(root.left,result)          
            self.rpost_order_traversal(root.right,result)
            result.append(root.item)

    ###ASSIGNMENT -21

    def min_item_node(self,temp): #temp=self.root(root node)  ##1
        root=temp
        while root.left is not None:
            root=root.left
        return root.item

    def max_item_node(self,temp):  #####2-------
        root=temp
        while  root.right is not None:
            root=root.right
        return root.item

    def delete(self,data): ###3-----
        self.root=self.rdelete(self.root,data)

    
    def  rdelete(self,root,data): #root=self.root(root node)  #data= item to in node
        if root is None:
            return root
        if data<root.item:
            root.left=self.rdelete(root.left,data)
        elif data>root.item:
            root.right=self.rdelete(root.right,data)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left               
            ##above 2 case not run then(node have two child)
            root.item=self.min_item_node(root.right) # min value-for successor/max_valur for pridicisor
            root.right=self.rdelete(root.right,root.item)
        return root

    
    def size(self):
        return len(self.inorder_traversal())


### test code----
bst=BST()
bst.insert(50)
bst.insert(30)
bst.insert(20)
bst.insert(40)
bst.insert(70)
bst.insert(60)
print(bst.inorder_traversal())
print(bst.size())
