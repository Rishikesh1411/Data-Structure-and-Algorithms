"""

     ASSIGNMENT-29

     1.DEFINE A CLASS HEAP TO IMPLEMENT HEAP DATA STRUCTURE WITH__INIT__METHOD
     TO CREATE EMPTY HEAP LIST.

     2.IN CLASS HEAP ,DEFINE A METHOD CREATE HEAP FROM FROM A GIVEN LIST OF ELEMENTS

     3.IN CLASS HEAP,DEFIEN A METHOD INSERT TO INSERT A GIVEN ELEMENT IN THE HEAP AT APPROPRIATE POSITION.

     4.IN CLASS HEAP DEFINE A TOP METHOD WHICH RETURNS THE TOP ELEMENT OF THE HEAP.RAISE AN EXCEPTION IF HEAP IS EMPTY

     5.DEFIEN A CLASS EMPTY HEAP EXCEPTION TO DESCRIBE CUSTOM EXCEPTION.

     6.IN CLASS HEAP DEFIEN A METHOD DELETE WHICH DELETE THE TOP ELEMENT AND RETURNS IT .RAISE AN EXCEPTION IF HEAP IS EMPTY

     7.IN CLASS HEAP DEFIEN A METHOD HEAP SORT TO SORT A GIVEN LIST WITH THE HELP OF HEAP.



"""

class Heap:          ####1
    def __init__(self):
        self.heap=[]

    
    def create_heap(self,list1): #####2
        for e in list1:
            self.insert(e)

    def insert(self,e):
        index=len(self.heap)
        parent_index=(index-1)//2
        while index>0 and self.heap[parent_index]<e:
            if index==len(self.heap):
                self.heap.append(self.heap[parent_index])
            else:
                self.heap[index]=self.heap[parent_index]
            index=parent_index
            parent_index=(index-1)//2
        if index==len(self.heap):
            self.heap.append(e)
        else:
            self.heap[index]=e

    
    def top(self):
        if len(self.heap)==0:
            raise EmptyHeapException()
        return swelf.heap[0]

   
    def delete(self): ######6
        if len(self.heap)==0:
            raise Emptyheapexception
        if len(self.heap)==1:
            return self.heap.pop()
        max_value=self.heap[0]
        temp=self.heap.pop()
        index=0
        leftchildindex=(2*index+1)
        rightchildindex=2*index+2

        while leftchildindex <len(self.heap):
            if rightchildindex<len(self.heap):
                if self.heap[leftchildindex]>self.heap[rightchildindex]:
                    if self.heap[leftchildindex]>temp:
                        self.heap[index]=self.heap[leftchildindex]
                        index=leftchildindex
                    else:
                        break
                else:
                    if self.heap[rightchildindex]>temp:
                        self.heap[index]=self.heap[rightchildindex]
                        index=rightchildindex
                    else:
                        break
            else:  ##no right child
                if self.heap[leftchildindex]>temp:
                    self.heap[index]=self.heap[leftchildindex]
                    index=leftchildindex
                else:
                    break
            leftchildindex=2*index+1
            rightchildindex=2*index+2
        self.heap[index]=temp
        return max_value

    
    def heap_sort(self,list1):  ###7
        self.create_heap(list1)
        list2=[]
        try:
            while True:
                list2.insert(0,self.delete())
        except Emptyheapexception:
            pass
        return list2





                
class Emptyheapexception(Exception):
    def __init__(self,msg="EmptyHeap"):
        self.msg=msg
    
    def __str__(self):
        return self.msg


list1=[34,56,12,78,43,25,10,80,60]
h=Heap()
list1=h.heap_sort(list1)
print(list1)