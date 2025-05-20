"""
    WRITE A PYTHON FUNCTION TO IMPLEMENT BUBBLE SORT.

"""

def bubble_sort(datalist):
    for r in range(1,len(datalist)):
        for i in range(len(datalist)-r):
            if datalist[i]>datalist[i+1]:
                datalist[i],datalist[i+1]=datalist[i+1],datalist[i]

l=[34,67,12,89,25,50]



bubble_sort(l)
print(l)

