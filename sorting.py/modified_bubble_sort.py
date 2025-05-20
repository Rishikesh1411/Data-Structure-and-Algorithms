"""
    WRITE A PYTHON FUNCTION TO IMPLEMENT MODIFIED BUBBLE SORT.

"""
def mod_bubble_sort(datalist):
    flag=False
    for r in range(1,len(datalist)):
        flag=False
        for i in range(len(datalist)-r):
            if datalist[i]>datalist[i+1]:
                datalist[i],datalist[i+1]=datalist[i+1],datalist[i]
                flag = True
        if not flag:
            break



l=[34,67,12,89,25,50]
mod_bubble_sort(l)
print(l)
