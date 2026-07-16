accept an integer an print hello world n times
n=int(input("please enter your number"))
for i in range(n):
     print("hello world")
print natural number up to n
n=int(input("enter your number"))
for i in range(n):
     print(i)
print natural number n to reverse
n=int(input("enter your number"))
for i in range(n,0,-1):
     print(i)
table you want
n=int(input("Enter number which  table you want"))
for n in range(n,(n*10)+1,n):
     print(n)
sum of up to n
n=int(input("enter your number"))
sum=0
for i in range(1, n+1):
     sum=sum+i
print(f"your number sum is{sum}")
factorial of n  number
n=int(input("enter your number:-"))
fact=1
for i in range( 1,n+1):
     fact=fact*i
     print(f"your factorial is {fact}")
sum ofall odd and even numbers in a range separaretly
n=int(input("enter your number"))
odd=0
even=0
for i in range(1, n+1):
     if i%2==0:
          even=even + i
     else:
          odd = odd + i
print({odd }, {even})
factors of numbersa
fACTORS OF NUMBER
n=int(input("enter number which number factors you want:-"))
sum=0
for i in range(1, n+1):
     if n%i==0:
          sum=sum+1
          print(i,{sum})
CHECK IT IS AN PERFECT NUMBER OR NOT
n=int(input("enter your number"))
sum=0
for i in range(1 , n):
     if n%i==0:
          sum=sum+i
if sum==n:
     print("its an perfect number")
else:
     print("not percet number")
n=int(input("enter your number"))
for i in range(1 ,n+1,1):
     if n%n==0 and n%1==0:
          print("its prime number")
     else:
          print("its not prime number ")
check it is an prime number or not
n=int(input("enter your number"))
count=0
for i in range(1 ,n+1):
     if n%i==0:
          count = count + 1
          print(f"{count},{i}")
if count==2:
     print("it is an  prime number")
else:
     print("it is not a prime number")
reverse a string by using for loop or find its palaindrome or not
a=input("enter your  word").strip().lower()
b=""
for i in range(len(a)-1,-1,-1):
          b= b + a[i]
print(b)
if b==a:
     print("yes your string is palalindrome")
else:
     print("not palaindrome")
cont all character different in string
a=input("enter your words").strip()
alf=0
specialchr=0
num=0
for i in a:
     if i.isalpha():
          alf=alf+1
     elif i .isnumeric():
          num =num+1
     else:
          specialchr=specialchr+1
     print(f"total alfa is {alf}\n total num is {num}\n total special chr is {specialchr}")
While loop question
seprate each digit of a number AND PRINT IT ON  THE NEW LINE  using while loop
a=int(input("enter your number"))
while a>0:
     print(a%10)
     a=a//10
reverse numbes using while loop and check num is pallandrome or not
a=int(input("enter your number"))
rev=0
copy=a
while a>0:
     rev=rev*10+a%10
     a=a//10
print(rev)
if rev==copy:
     print("your number is pallendrome")
else:
     print("your number is not pallendrome")
create guess game
import random
num= random.randint( 1 ,10)
tries=0
while True:
     guess=int(input("please guess the number:-"))
     if num==guess:
          tries+=1
          print(f"your are guess rigth and it take {tries} tries")
     elif num>guess:
          print("Go little higher")
          tries +=1
     elif  num<guess:
          print(" Go little lower")
          tries +=1
     else:
          tries +=1
def pallindrome(st):
     rev=""
     for i in range(len(st)-1,-1,-1):
          rev = st[i] + rev

          if rev == st:
               print(f" {st} is a pallendrome")
          else:
               print(f" {st} is not a pallendrome")

pallindrome("mam")


questions of list
print all negative and positive elements of list
l=[12,-34,65,-78,-34,65,34]
print("postive element are:-")
for i in l:
     if i>=0:
          print(i)

print("negative elements are:-")
for i in l:
     if i<0:
          print(i)
find the greatest  element of list and index value too
l=[120 ,450,650 ,370]
largest=l[0]
index=0
for i in range(len(l)):
     if l[i]>largest:
          largest=l[i]
          index=i

print(f"The greatest element of list is :- {largest} at index value {i}")
find the mean of list
list=[23,49,50,34,60]
sum=0
mean=0
for i in list:
     sum= sum + i
     mean=sum/len(list)
print(f"the mean of the list is :- {mean}")
find second largest number
l=[20,60,70,90,]
largest=l[0]
sec_largest=l[0]
index=0

for i in range(len(l)):
     if l[i]>largest:
          sec_largest=largest
          largest=l[i]
          index= i-1
     elif sec_largest<l[i] and l[i]<largest:
          sec_largest=[i]
          index=i

print(f"second largest number is :-{sec_largest} \n at index value :-{index}")

check list shorted or not
l=[1,2,3,4,5,]
for i in range(len(l)-1):
    if l[i]<l[i+1]:
        continue
    else:
        print("not shorted")
        break
else:
    print("list is shorted")
set in pythone
create a set
a={1,5,6,3}
print(a)
chck duplicate in set accept or not
a={1,2,2,3,}
print(a)
a=hash("hello")
print(a)
b=hash((1,2,3))
print(b)
c=hash([2,4,5])
print(c)
for numbers
a={1,2,8,3,5,6,4}
for i in a:
     print(i)
for mixing
a={1,2,"hello",34}
for i in a:
     print(i)
method of set
.add
a={1,2,3,4}
a.add(6)
print(a)
.remove
a={1,2,3,4}
a.remove(3)
print(a)
.pop
a = {1,8, 2, 3, 4}
a.pop()
print(a)
mmethods of two sets
.union
a={1,2,3,4,5}
b={4,5,6,7,8}
# union=a.union(b)
union=b|a
print(union)
.intersection
a={1,2,3,4,5}
b={4,5,6,7,8}
c=a.intersection(b)
short a&b
print(c)
.difference
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
c = a.difference(b)
# short a-b
print(c)
symmatric diff
a = {1, 2, 3, 4, 5 ,10}
b = { 6, 7, 8,25,4}
c = b.symmetric_difference(a)
# short a^b
print(c)

questions of dictionary
sum of all  elements in dictionary

a={1:200,2:200,3:300}
sum=0
for i in a:
    sum = sum + a[i]
print(f"The sum of the element is:- {sum}")

programe for marge two dictionery
a={1:100,2:200,3:300}
b={4:400,5:500,6:600}
for i in b:
     a[i]=b[i]
print(a)

find occurence of each element in list by using dictionary

a=[1,1,1,4,5,4,4,7,7,5,5]
d={}
for i in a:
     if i in d.keys():
          d[i] += 1
     else:
          d[i]=1
print(d)

 program to combine two dictionary by adding values for common keys
a={1:100,2:200,3:300}
b={1:400,5:500,3:600}
for i in a:
     if i in b.keys():
          b[i]+=a[i]
     else:
          b[i]=a[i]
print(b)
