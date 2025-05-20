class Queue:
    def __init__(self):
        self.item = []
        self.item_count=0

    def is_empty(self):
        return len(self.item) == 0 or  self.item_count == 0


    
    def enqueue(self,data):
        self.item.append(data)
        self.item_count += 1

    def dequeue(self):
        return self.item.pop(0)
        self.item_count -= 1

    def get_rear(self):   ##  last and rear element in queue
        return  self.item[-1]

    def get_front(self):  ## peek and front or first  element in queue
        return self.item[0]


    def size(self):
        return self.item_count
    
    def print_queue(self):
        print(self.item,end="<->")

s1=Queue()
s1.enqueue(10)
s1.enqueue(20)
s1.enqueue(30)
s1.enqueue(40)
s1.enqueue(50)
s1.print_queue()
print("poped element from queue is :",s1.dequeue())
print("peek/front element is :",s1.get_front())
print("size of queue is :",s1.size())
print("rear  element is :",s1.get_rear())



    

    


