"""
     write a python function to implement selection sort

"""

def selection_sort(list1):
    n=len(list1)
    for i in range(n-1):# if n-1 element has sorted then n th element will also sorted
        min_index=i
        for j in range(i+1,n):
            if list1[j]<list1[min_index]:
                min_index=j
        list1[i],list1[min_index]=list1[min_index],list1[i]

l=[34,67,12,89,25,50]
selection_sort(l)
print(l)