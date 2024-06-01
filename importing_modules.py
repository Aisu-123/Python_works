# import math
# x=math.factorial(5)
# print(x)

# -------------------------------------------

# from math import factorial
# x=factorial(5)
# print(x)

# -----------------------------------random-----------

# import random
# l1=[1,2,3,4,5,6,7,8,9]
# print(random.choices(l1))
# s="hello"
# print(random.choices(s))
# l2=["apple","ball","cat","dog"]
# print(random.choices(l2))
# x=random.random()
# print(x)
# random.shuffle(l1)
# print(l1)
# x=random.randint(1,10)
# print(x)
# x=random.randrange(1,9,5)                                                                      
# print(x)
# x=random.sample(l1,2)
# print(x)

# --------------------------6digits,100 lottery,2 winners----------------

# import random
# a=[]
# for i in range(100):
#     x=random.randrange(100000,999999)
#     a.append(x)
#     print(a)
# print(random.choices(a))
# print(random.choices(a))

# -------------------------the dice who gets the 5 will be the winner----------

# import random
# for i in range(5):
#     x=random.randint(1,5)
#     print(x)
#     if x==5:
#         print("you won")
#         break
# else:
#     print("you lost")

# --------------select 3 numbers randomly which was divisible by 5 in between 100 to 999-----

# import random
# count=0
# for i in range(100,900):
#     x=x=random.randint(100,999)
#     if(x%5==0):
#         print(i)
#         count+=1
#     if count==3:
#         break


