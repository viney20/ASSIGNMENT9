#Q.1- Name and handle the exception occured in the following program:
'''The exception is: ZeroDivisionError'''

#Q.2- Name and handle the exception occurred in the following program: l=[1,2,3] print(l[3]) 
## ANS: The exception is: IndexError -list index out of range
try:
    l=[1,2,3]
    print(l[3])
except:
    print("List index is out of range")


#Q.3- What will be the output of the following code:
"""Output:
An Exception NameError:Hi there will occur"""

#Q.4- What will be the output of the following code: 
"""Output when (a,b)=(2.0,3.0):
    -5.0

Output when (a,b)=(3.0,3.0): as exception occured except block will execute
    a/b result in 0
"""
#Q.5- Write a program to show and handle following exceptions: 1. Import Error 2. Value Error 3. Index Error 

#1. import error
try:
    import py #name of module that doesn't exist in python
except:
    print("such module doesn't exist in python")
    
#2. value error
try:
    n=int(input("Enter a number: "))
    print("you have entered ",n)
except:
    print("Nothing except integers is accepted")

#3. Index error
try:
   l=[1,2,3,4,5,6]
   n=int(input("Enter index >0 and <6 to get it's value "))
   print(l[n])
except:
    print("Index range is out of bound : 0<index<6")

    
