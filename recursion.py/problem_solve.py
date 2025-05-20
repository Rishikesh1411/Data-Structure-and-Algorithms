""" 

   ASSIGNMENT-18

   1.WRITE A RECURCIVE FUNCTION TO PRINT FIRST N NATURAL NUMBER.

   2.WRITE A RECURCIVE FUNCTION TO PRINT FIRST N NATURAL NUMBER IN REVERSE ORDER.
   
   3.WRITE A RECURCIVE FUNCTION TO PRINT FIRST N ODD NATURAL NUMBER

   4.WRITE A RECURCIVE FUNCTION  TO PRINT FIRST N EVEN NATURAL NUMBER

   5.WRITE A RECURCIVE FUNCTION TO PRINT FIRST N  ODD NATURAL NUMBER IN REVERSE ORDER

   6.WRITE A RECURCIVE FUNCTION TO PRINT FIRST N  EVEN NATURAL NUMBER IN REVERSE ORDER.

   


"""

#####1

def nNatural(n):
    if n>0:
        nNatural(n-1)
        print(n,end="<->")

nNatural(4)


####2--
def nNaturalReverse(n):
    if n>0:
      print(n,end="<->")  
      nNaturalReverse(n-1)

nNaturalReverse(5)
    


#####3--
def nOddNatural(n):
    if  n>0:
        nOddNatural(n-1)
        print(2*n-1,end="<->")

nOddNatural(10)

####4--

def nEven(n):
    if n>0:
        nEven(n-1)
        print(2*n , end="<->")


nEven(10)

###5--
def nOddrev(n):
    if n>0:       
        print(2*n-1,end="<->")
        nOddrev(n-1)


nOddrev(5)


###6--

def nEvenrev(n):
    if n>0:      
        print(2*n,end="<->")
        nEvenrev(n-1)

nEvenrev(5)


    