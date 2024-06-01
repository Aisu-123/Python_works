# x=lambda a:a*a*a
# print(x(2))

# ------------------------------sum---------------

# x=lambda a,b:a+b
# print(x(2,2))

# -----------------------------filter method print even----------

a=[1,2,3,4,5,6,7,8,9,10]
x=list(filter(lambda a:a%2==0,a))
print(x)

# ----------------------------map mathod----------------

# a=[1,2,3,4,5,6,7,8,9,10]
# x=list(map(lambda a:a*2,a))
# print(x)

# ---------------------------reduce method-------------

# import 
# a=[1,2,3,4,5,6,7,8,9,10]
# x=list(reduce(lambda d,f:d+f,a))
# print(x)

# ----------------------print numbers divisible by 5----------

# a=[5,10,14,20,12,25,22]
# x=list(filter(lambda a:a%5==0,a))
# print(x)

# ----------------------square of each element------------------

# a=[5,10,14,20,12,25,22]
# x=list(filter(lambda a:a*a,a))
# print(x)

# --------------------------filter all people age more than 18-------

# a=[5,10,14,20,12,25,22]
# x=list(filter(lambda a:a>18,a))
# print(x)

# -------------------------------using function------------------------

# ---------------------------find even numbers and make a new list------

# a=[1,2,3,4,5,6]
# def functionname(x):
#     x=list(filter(lambda a:a%2==0,a))
#     print(x)
# functionname(a)

# --------------------------check the given string is pallindrome or not--------

# b="level"
# x=lambda a:a==a[::-1]
# y=x(b)
# if y==True:
#     print("its pallindrome")
# else:
#     print("its not pallindrome")

# ------------------------------eliminate the duplications-------------------

# a=[1,2,4,5,1,2,3,5,1]
# z=[]
# def functionname(a):
#     for i in a:
#         if i not in z:
#             z.append(i)
#     print(z)
# functionname(a)

# -----------------------------------------pass by refference----------------------------------

# def display(x):
#     x[0]=100
#     print(x)
# x=[1,2,3]
# display(x)
# print(x)