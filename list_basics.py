# a=[1,2,3,4]
# b=["a","b","c"]
# print(type(a))
# print(type(b))
# print(len(a))
# print(a[0])
# print(a[-4])
# print(a[1:4])
# print(a[-4:-1])
# print(a[::-1])

# -------changable---------


# a[0]="python"
# print(a)
# del(a[0])
# print(a)
# del(a)
# print(a)

# ----------------------------

# a=[2,4,5,6,7]
# a[0:2]=[8,5]
# print(a)

# a=[1,2,3,4,5]
# a[0:2]=[8,6,5]
# print(a)

# a=[1,2,3,4,5]
# a[0:2]=[3]
# print(a)

# ----------------------------------

# a=["a","b","c"]
# print("a" in a)

# ------------------------------------

# s="python"
# e=list(s)
# print(e)


# ------------------------------------append------------

# a=[1,2,3,4,5]
# a.append(100)
# print(a)

# ----------------------------------insert---------------

# a=[1,2,3,4,5]
# a.insert(0,200)
# print(a)

# ---------------------------------extend------------------

# a=[1,2,3,4,5]
# b=[10,20,30]
# a.extend(b)
# print(a)


# a=[1,2,3,4,5]
# b="hello"
# a.extend(b)
# print(a)

# ------------------------------remove----------------------

# a=[1,2,3,4,5]
# a.remove(4)
# print(a)


# -----------------------------pop-------------------------

# a=[1,2,3,4,5]
# a.pop()
# print(a)

# a=[1,2,3,4,5]
# a.pop(2)
# print(a)

# --------------------------clear----------------------------

# a=[1,2,3,4,5]
# a.clear()
# print(a)

# --------------------------pop------
# a=[1,2,3,4,5]
# s=a.pop()
# print(a)

# --------------------------------sorting---------

#  a=[1,2,4,3,5]
#  a.sort()
#  print(a)

# ------------------------------reverse------------

# a=[1,2,4,3,5]
# a.reverse()
# print(a)

# -----------------------------reverse sorting----------

# a=[1,2,4,3,5]
# a.sort(reverse=True)
# print(a)

# -----------------------------------

# a=["python","java","php","angular","javascript","html"]
# a.sort()
# print(a)

# ------------------------------------------

# a=["python","PYTHON","javascript","JAVASCRIPT"]
# a.sort()
# print(a)

# -------------------------------------------

# a=["Python","python","PYTHON"]
# a.sort()
# print(a)

# --------------------------------------------

# a=["python","java","php","angular","java","javascript","html","java"]
# print(a.count("java"))
# print(a.index("java"))

# ----------------------list comprehension------

# a=[2,4,6,8,10]
# b=[i/2 for i in a]
# print(b)

# ------------------------------------------------

# a=["abc","def","axy","xyz"]
# b=[i for i in a if "a" in i]
# print(b)

# ---------------------------------------------

# l1=[1,2,3]
# l2=[10,20,30]
# p=[i*j for i in l1 for j in l2]
# print(p)

# -------------------------------------------------

# a=[1,2,3,4,5,6,7,8,9,10]
# b=[i for i in a if i%2==0]
# print(b)

# -------------------------------------------------

# a=["mom","malayalam","bat","ant"]
# b=[i for i in a if i[::-1]==i]
# print(b)