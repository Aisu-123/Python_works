# 1.Check whether 100 greater than 1000 or not
# 2.check whether the number is odd or even
# 3.check whether a number is +ve or -ve
# 4.Factorial of a number
# 5.To find the count of a number
# 6.To find the sum of the count of the number
# 7.to find prime number with for loop
#  8.to find prime number with while loop   
# 9.to find the prime numbers in a range
# 10.to find the number of vowels in a sentence





# --------1.Check whether 100 greater than 1000 or not-------------


# a=100
# if a>1000:
#     print ("a is greater than 1000")
#     if a>50:
#         print ("a is greater than 50")
#     else :
#         print ("a is not greater than 50")
# else:
#     print ("a is not greater than 1000")



#---------2.check whether the number is odd or even--------



# a=int (input("enter a number:"))
# if a%2==0 :
#     print ( "it is an even number")
# else :
#     print ("it is an odd number")



# ----------3.check whether a number is +ve or -ve-------



# a=int(input("enter a number:"))
# if a>0 :
#     print ("a is a positive number")
# elif a<0 :
#     print ("a is a negative number")
# elif a==0 :
#     print ("a is zero")
# else :
#     print ("a is not zero")


# ---------4.Factorial of a number------------


# n=int(input("enter the a number :"))
# fact=1
# if n<0:
#     print("negative number have no factorial")
# elif n==0 :
#     print ("factorial of zero is 1")
# else :
#     for i in range(1,n+1):
#          fact=fact*i
#     print ("factorial of",n,"is",fact)


# ---------5.To find the count of a number-------



# n=int(input("enter a number:"))
# i=1
# while i<n:
#     i+=1
#     n//=10
# print(i)


# -------6.To find the sum of the count of the number-------



# n=int(input("enter a number:"))
# i=0
# s=0
# while i<n:
#     p=n%10
#     s=s+p
#     n//=10
# print(s)




# ---------7.to find prime number with for loop-----------



# n=int(input("Enter the number:"))
# for i in range (2,n):
#     if n%i==0:
#         print("it is not a prime")
#         break



#     else:
#         print("it is a prime")
#         break
        

# ----------8.to find prime number with while loop----------
    


# n=int(input("enter a number:"))
# i=2
# while i<n:
#     if n%i==0:
#         print("it is not a prime")
#         break
#         i+=1
#     else:
#         print("it is a prime")
#         break



# -----------9.to find the prime numbers in a range-----------



# f=int(input("enter the first number:"))
# l=int(input("enter the last number:"))
# for i in range(f,l):
#     for j in range(2,i):
#         if i%j==0:
#             break
#         else:
#             print(i)
#             break




# ---------------10.to find the number of vowels in a sentence---------



# a="Welcome to the world of python"
# v="aeiouAEIOU"
# c=0
# for i in a:
#     for j in v:
#         if i==j:
#             c=c+1
#             print("num of vowels:",c)
        

# -----------------------ARMSTRONG NUMBER-----------------------


# n=153
# sum=0
# num1=n
# length=len(str(n))
# while(n>0):
#     temp=n%10
#     sum=sum+pow(temp,length)
#     n=n//10
# if sum==num1:
#     print("it is armstrong number")
# else:
#     print("it is not armstrog number")

# --------------------------Pallindrome or not-----------------------

# b="level"
# x=lambda a:a==a[::-1]
# y=x(b)
# if y==True:
#     print("its pallindrome")
# else:
#     print("its not pallindrome")

# --------------------method2 (without slicing method)---------------------------------

a=str(input("enter a string:"))
j=-1
flag=0
for i in a:
    if i != a[j]:
        flag=1
        break
    j=j-1
if flag ==1:
    print("it is not pallindrome")
else:
    print( "it is pallindrome")