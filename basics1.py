# ------------------to just print something-----------

# print("hello world")

# ------------------to get the type of a string-------------

# a=10
# print(type(a))

# ------------------to get the type of a string--------------


# b="hello"
# print(type(b))

#--------------------to add 2 strings----------

# a="hello"
# print(a+"world") 

# -------------------to give a space between 2 strings------

# a="hello"
# print(a,"world") 


# ---------------to find the length of a string------


# a="hello"
# print(len(a)) 



# ---------------------------------------SLICING-----------------------------------------

# a="hello"
# print(a[1:3])
# values displays according to the index position 
# 
# -----------------------------------------------

# a="hello"
# print(a[-2:-1])
# values displays according to index position from the right side 

# ------------------------------------------------

a="hello"
print(a[ :4])
# values displays till the fourth index position

# ------------------------------------------------

# a="hello"
# print(a[0: ])
# values displays from the 0th index position till it ends

# ------------------------------------------------

# a="hello"
# print(a[::-1])
# values displays from the end to front

# -------------------------------------------------

# a="hello"
# del a[0]
# it won't works..delete according to index position
# del[a]
# it works to delete the complete value

# -------------------------------------------------


# a="Welcome to the world of python"

# print(a.capitalize())
# first letter of the sentence will bw capitalized

# print(a.title())
# capitalize the first letter of the each word in a sentence

# print(a.upper())
# capitalize all

# print(a.lower())
# all will be in small letter

# print(a.index("e"))
# index position of first coming preferred letter

# print(a.find("o"))
# shows the index position of the first coming preferred letter

# print(a.swapcase())
# it shows the capitalized one to small and small letters to capital

# print(a.casefold())
# it shows all small letters

# print(a.rfind("p")) 
# last occurence of the value.-1 means not exist

# print(a.rindex("o"))
# last occurence of the values index position

# print(a.replace("e","pppp"))
# replace the value e to pppp

# print(a.isalpha())
# checks all are alphabets

# print(a.isnumeric())
# chacks all are numeric

# print(a.isalnum())
# checks whether it is combination of alphabets and letters


# ------------------slicing--------------------


# a=[1,2,3,4]
# print(type(a))
# print(a[0])
# print(a[-1])
# print(a[1:4])
# print(a[-5:-1])
# print(a[::-1])
# a[0]="python" 
# print(a)
# del a[0]
# print(a)

# -------------spacing---------------


# a="hello"
# print(a.center(20," "))
# print(a.center(20,"*"))

# ----------------spliting-----------

# a="hello world"
# x=a.split(" ")
# print(x)


# a="hello world"
# x=a.split("#")
# print(x)

# --------reverse--------
# a="hello world"
# x=a.rsplit("#")
# print(x)

# -------------------------------

# a="hello"
# x=a.startswith("h")
# print(x)

# a="hello"
# x=a.endswith("o")
# print(x)

# --------------------------------
