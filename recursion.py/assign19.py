"""
   ASSIGNMENT-19

   1.WRITE A RECURCIVE FUNCTION TO CALCULATE SUM OF FIRST N  NATURAL NUMBER

   2.WRITE A RECURCIVE FUNCTION TO CALCULATE SUM OF FIRST N  ODD NATURAL NUMBER

   3.WRITE A RECURCIVE FUNCTION TO CALCULATE SUM OF FIRST N  NATURAL EVEN NUMBER

   4.WRITE A RECURCIVE FUNCTION TO CALCULATE FACTORIAL OF A NUMBER

   5.WRITE A RECURCIVE FUNCTION TO CALCULATE SUM OF SQUARES OF FIRST N NATURAL NUMBER



"""

####1--
def sum_of_natural_number(n):
    if n == 1:
        return 1
    s=n+sum_of_natural_number(n-1)
    return s

print(sum_of_natural_number(5))


####2---
def sum_of_odd_number(n):
    if n == 1:
        return 1
    s= 2*n-1+ sum_of_odd_number(n-1)
    return s

print("sum of n odd number is:",sum_of_odd_number(10))

    
####3--

def sum_of_even_num(n):
    if  n == 1:
        return 2
    return 2*n +  sum_of_even_num(n-1)

print("sum of n even num is",sum_of_even_num(10))


####4--

def  factorial(n):
    if n == 1:
        return  1
    return n * factorial(n-1)

print("factorial of n natural num is",factorial(5))

####5---

def findsq(n):
    if n==1:
        return 1
    return n**2 + findsq(n-1)


print("sum of square of n  natuarl number is ",findsq(5))

