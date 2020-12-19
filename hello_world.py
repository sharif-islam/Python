# sharif
from math import *
from random import randint #small number
import random  #large number
from collections import deque
from queue import Queue
'''

sjdgjvwrsbd sdv
sdvnjsf

name = "sharif"
age = 23
print("hello    world\n my name " + name + " is "+ name) use (+),if print any string in a line
print("hello    world\n my name " ,age, " is "+ name) use (,) if use integer value in a line

a = 18
b = 4
t =0
ab = int(input())
print(ab , "\n") use it for newline after every output
name1 = input()
print(name1)   print function automatically create a newline after every statement 
print(a/b) simple divide with floating value
print(a//b) without floating value. simple for integer part
print(2**3) it means (a^b) 
i = 1
sum =0
while i<=5:
    sum+=i
    i = i+1
print(sum)
'''
''' use it for comment line '''
'''
num = 65
num1 =51
num2 = 60
print(f"{num} + {num1} = {num+num1}")   output format for this line,here f means format  65 + 51 = 116

str = "sharif islam"
number = "01994478218"
print(str,end = " ") here print function has no create newline.just create space for (end = " ")

print(number)

print(max(num,num1))    for max value
print(min(num,num1))    for min value
print(abs(1-4))         absolute difference
print(pow(2,3))         for power (a^b)
print(sqrt(7))          for square root
print(round(3.45))      if floating value less then .5 it return integer part
print(round(3.55))      if floating value greater or equal .5 then it return upper part means (integer part+ 1)
print(floor(3.5))       it return lower part means integer part
print(ceil(3.6))        it return upper part means (integer part+1 )

if num>num1:    if statement formula   if a>b : 
    if num>num2:
        print(num)
    else:
        print(num2)
elif num1 > num:
    if num1>num2:
        print(num1)
    else:
        print(num2)
elif num2>num:
    if num2> num1:
        print(num2)
    else:
        print(num1)

print(num1 if num1>num2 else num2)   simple if else statement in one line.  a will be answer if a>b otherwise b.so we write it simply (a if a>b else b)

mark = 87
if 80<= mark <= 100:   another conditional statement of if 
    print("A+")
#subject =["10","20","30","40","50"]   (#) use for single line command /// string type array
subject = [10,20,30,40,50,15,15]     integer type array
print(subject)   print all element in array
print(subject[2])  print a specific position in array
print(subject[2:])    print all value from a specific point (always maintain 0 base index)
#print("31" not in subject)  check a value present in array or not ..always return boolean value
#print(subject + ["11"])      print a value after all element..it's not add value with full array..just for print 
print(subject * 3)         print array 3 times continuously one by one  
#subject.append("15")     add a value in array at last position ("")means string value add 
subject.append(15)        simply add value at last position, it means integer value add
subject.insert(2,100)     insert a value at position x (x always zero base)
subject.remove(20)        remove x from array
print(subject)      
subject.reverse()         reverse full array
subject.pop()             delete element from last
print(subject)     
print(len(subject))       size of the array
subject2 = subject.copy()         array copy to other array
pos = subject2.index(100)        it return first index of value x
print(pos)
cnt = subject.count(15)        how much time has a value in this array
print(cnt)
print(subject2)

number = list(range(10))      list use for range..here 10 means (0,1,2...9) not include 10
print(number)
number = list(range(5,10))   here 5-9
print(number)
number = list(range(2,10,2))    here start from 2,but print up-to 9,but after every two numbers.. that means 2,4,6,8
print(number)
for x in number:            for loop using formula ,here number means array or list
    print(x)

# 2+4+6+8.....+n
n = int(input())
sum1=0
for x in range(2,n+1,2):  if calculate all even value uo-to n using for loop
    sum1= sum1+x
print(sum1)

n = 5;
for i in range(n+1):
    print((n-i)*" ", end = " ")       print(5*" ") means print 5 space
    print(i*"*")                      here print(i*"*" means i times print *
guess = int(input())
#ran = randint(1,5)                   create a random number from range [1-5] .it use for small random number
ran = int(random.random()* 100) #  0-99   create a number within [0 99].... cz we use (* 100).if we use (*1000) ,create a number within [0 999]
print(ran)
if guess == ran :
    print("yes")
else:
    print("no")
#list
n = int(input())    input a array
a = input();
a = a.split()   split it into part by part
sum=0;
for i in a :
    sum = sum + int(i)
print(sum)

# number of digits,letters,words in a string
a = input("Enter a string ")
digit=0
letter=0
word=1
for i in a:
    x = i.lower()    convert it to upper case to lower case
    if 'a'<=x<='z':
        letter = letter+1   count how much letter in this string
    elif '0'<=i<='9':
        digit = digit+1     how much digit in this string
    else:
        word=word+1        count number of words in this string

print(letter)
print(digit)
print(word)

# A basic code for matrix input from user

R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))

# Initialize matrix
matrix = []
print("Enter the entries rowwise:")

# For user input 4
for i in range(R):  # A for loop for row entries
    a = []
    for j in range(C):  # A for loop for column entries
        a.append(int(input()))
    matrix.append(a)

# For printing the matrix
for i in range(R):
    for j in range(C):
        print(matrix[i][j], end=" ")
    print()
#dictionary
studentid= {
    1 : "mainul",
    2 : "rakib",
    3 : "robin",
    4 : "sharif",
}
print(studentid.get(4, "not a valid key"))  (here has two part)always they print value according to id.. if get(2) print rakib.. if id person not present in dictionary,then print "Not a valid key"  
#tuple
student= (

     ("mainul",23,3.24),
      "rakib",
      "sharif",
)
print(student[0])     here print all information of student 0

#set    set has always reamin unique element
st = {1,5,2,3,6}
print(st)
st1 = set([7,8,6,5])
st1.add(1)        add element in set
st1.remove(7)     remove element from set
print(st1)
print(1 in st1)      check 1 is present in this set or not,,,return boolean value
print(st | st1) #union      
print(st & st1) #intersection
print(st - st1) #difference


#another set input from user

l1 = set(map(int, input().split()))        input a line in set format
n = int(input())
l2 = set()
for i in range(n):         
  for j in map(int, input().split()):
      l2.add(j)       input n set... then add all element in one set
print(l1)
print(l2)



#stack    stack means last in first out 
book =[]
book.append("C")   add element in stack
book.append("C++")
book.append("Java")
print(book)
book.pop()      pop top element 
print(book)
print("top item is :",book[-1])       find top element ...always use -1 for top element
book.pop()
book.pop();
if not book :      check stack is empty or not 
    print("no book in list")
else:
    print("have some books in stock")


#deque
bank = deque(["ami","tmi","se"])
print(bank)
bank.popleft()
print(bank)
bank.append("amra")
print(bank)
print(bank[-1])

#queue

q = Queue(maxsize=3)      declare max size of queue

print(q.qsize())     print queue size

q.put('a')      adding element in queue
q.put('b')
q.put('c')

print("\nFull: ", q.full())   check queue is full or not,according to maxsize
print("\nElements dequeued from the queue")
print(q.get())   print front element of queue and delete it
print(q.get())
print(q.get())

print("\nEmpty: ", q.empty())   check queue is empty or not

q.put(1)
print("\nEmpty: ", q.empty())    return true or false
print("Full: ", q.full())       return true or false




#create function

def add(x,y):
    sum = x+y
    return sum
for i in range(5):
    ab = int(input())
    ba = int(input())
    ress = add(ab,ba)
    print(ress)

#x argument pass
def student(*details):
    print(details)
    print(details[0])
student(101,"sharif")
student(104,"arif")

#xx argument pass
def student(**details):
    print(details)

student(id=101,name = "sharif")
student(id = 104,name = "arif")
#xx argument pass
def student(id,name):
    print(id,name)

student(id=101,name = "sharif")
student(id = 104,name = "arif")

#debug
def addition(*nums):
    sum=0
    for tot in nums:
        sum = sum+tot     
        print(sum)   for check debugging  
    return sum
ans1 = addition(10,20)
print(ans1)

#(lambda parameter : expression) (parameter value)  pototype of lambda function
#  lambda function works for single expression or single line of code
p = int(input())
q = int(input())
a = (lambda a,b : a*a + 2*a*b + b*b) (p,q)
print(a)


#map function 

def square(x):
    return x*x
num = [1,2,3,4,5]
result = list(map(square,num))     map works for two parameter one is function ,another is array ,map always return an iterable object 
print(result)

# filter function

def check(x):
    if x%2==0:
        return x
num = [1,2,3,4,5]
result = list(filter(check,num))     #filter check if the funtion condition is true then return otherwise remove from list
print(result)

#list comprehensions
# [expression for item in list]    pototype of list comprehensions
num = [1,2,3,4,5]
result = [x*x for x in num]
result = [x*x for x in num if x%2==0]
print(result)

# zip function use for combine multiple list into one list
roll = [5,9,25]
name = ["sharif","rakib","mainul"]
result = list(zip(roll,name,"abcd")) #last part will go oe after another 
print(result)

# recursion function
def fact(n):
    if n==1:
        return 1
    else:
        return n * fact(n-1)
result =fact(5)
print(result)

#file read 


file = open("stdnt.txt","r")
#text = file.read()   # full file read
#print(text)
#text = file.readlines()  # use all things are print into one line
#print(text)
#text = file.readlines()[0]  # use all print first line
#size = len(text)

#use for loop

for line in file:
    print(line)
#print(size)
file.close()


#write in file

file = open("stdnt.txt","a")   # if use (a) before element are remain in life,if use (w) delete before element from file
file.write("\njoyanto chakroborty")
file.close()

#swapping
a = 20
b = 10
a,b = b, a         #swap a to b
print("a = ",a)
print("b = ",b)

#exception handling part

list = [8,0,4]
try:
    result = list[0]/list[3]
    print(result)
    print("done")
except ZeroDivisionError:    #if dividing by zero
    print("Dividing is zero is not possible")
except ValueError:
    print("you have to insert only integer")
except IndexError:     # if index out of bound
    print("Index error")
finally:                  #finally block always work, have any exception or not 
    print("Successful")
    
#use raise exception 

def voter(n):
    if n<18:
        raise ValueError("invalid voter")
    return "you are allow to vote"
try:
    print(voter(17))
except ValueError as e:   #assign ValueError in e
    print(e)
'''

