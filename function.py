# def functionname(a):
#     print("hello world",a)
# functionname("ammu")

# ---------------------------------------

# def functionname(a,b):
#     print("hello world",a,b)
# functionname("ammu",10)
# functionname("anu",10)

# -----------------------------------------

# def functionname(a,b=20):
#     print("hello world",a,b)
# functionname("ammu",10)
# functionname("anu")

# ------------------------------------------

# def show(a,b):
#     print(a+b)
# show(10,20)

# --------------------------------------------

# def show(a,b):
#     return(a+b)
# print(show(10,20))

# ---------------------------------------------

# def display(a):
#     for i in a:
#         print(i)
# a=["a","b","c","d"]
# display(a)

# -------------------------------------------------


# def show(a,b,c):
#     print(a,b,c)
# show("ammu","anu","abc")

# --------------------------------------------------

# def show(*a):
#     print(a)
# show("ammu","anu","abc")

# ----------------------------------------------------

# def display(**a):
#     print(a)
# display(a="ammu",b="anu",c="abc")

# -----------------------------------------------------

# def display(a,b,c):
#     print(a,b,c)
# display(a="ammu",b="anu",c="abc")

# ------------------------------------odd or even----------

# a=int(input("enter a number:"))
# def functionname(a):
#     if a%2==0:
#         print("it is even")
#     else:
#         print("it is odd")
# functionname(a)

# ---------------------------to find the length of a word in a string--------

# a=str(input("enter the string:"))
# def word(a):
#     w=input("enter the word you want:")
#     c=w.split()
#     for i in c:
#         print(len(i))
#         if len(i)%2==0:
#             print(i)
# word(a)

# --------------------------------recursion-------------------------

# def summing(n):
#     if n<=0:
#         return n
#     else:
#         return n+summing(n-1)
# print(summing(5))

# -------------------------------factorial with recursion----------------------------

# def fact(n):
    
#     if n<=1:
#         return n
#     else:
#         return n*fact(n-1)
# n=int(input("enter a number:"))
# print(fact(n))    

# --------------------------------fibonacci with recursion--------------------

# def fib(n):
#     if n<=1:
#         return n
#     else:
#         return(fib(n-1)+fib(n-2))
# n=int(input("enter a number:"))
# for i in range(n):
#     print(fib(i))

# --------------------------------cube------------------------------------------

# def cube(x):
#     return x*x*x
# a=int(input("enter a number:"))
# print(cube(a))

