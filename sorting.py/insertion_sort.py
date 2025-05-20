"""
     write a python function to implement insertion  sort

"""
def insertion_sort(list):
    for i in range(1,len(list)):
        temp=list[i]

        j=i-1
        while j>=0 and temp<list[j]:
            list[j+1]=list[j]
            j-=1
        list[j+1]=temp



mylist=[25,37,11,14,60,82,18,41]
insertion_sort(mylist)
print(mylist)