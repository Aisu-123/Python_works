
# ----------------------print num of lowercase----------------


# a="My World"
# c=0
# s=0
# for i in a:
#     if i.isupper()==True:
#         c=c+1
#     elif i.islower()==True:
#         s=s+1
# print("num of lowercase:",s)



# ----------------------print in words of a number----------------


# d=["zero","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","foueteen","fifteen","sixteen","seventeen","eighteen","ninteen"]
# s=["","","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninty"]
# a=int(input("enter a number:"))
# if a<=19:
#     print(d[a]) 
# elif a<100:
#     z=a%10
#     p=a//10
#     if z==0:
#         print(s[p])
#     else:
#         print((s[p])+d[z])
# else:
#     print("not defined")


# ------------------------------------reverse the given string-------------------------



# a="welcome"
# print(a[::-1])

# --------------------------------------no: of alphabets in a string--------------------


# a="python123@"
# c=0
# for i in a:
#     if i.isalpha()==True:
#         c=c+1
#         print("number of alphabets:",c)


# ---------------------------------------no: of numbers present in a string------------------


# a="welcome2023"
# c=0
# for i in a:
#     if i.isnumeric()==True:
#         c=c+1
#         print("the number of numbers:",c)


#---------------------------------------if a number present in a string,find the sum----------

# a="Hai963"
# s=0
# c=0
# for i in a:
#     if i.isnumeric()==True:
#         c=int(i)
#         s=s+c
#         print("sum of numbers:",s)


#---------------------------------no: of vowels present in a string-------------------------

# a="Welcome to python"
# v="AEIOUaeiou"
# c=0
# for i in a:
#     for j in v:
#         if i==j:
#             c=c+1
#             print("number of vowels:",c) 

# ---------------------------------num of uppercases and lowercases present in string--------

# a="My World"
# c=0
# z=0
# for i in a:
#     if i.isupper()==True:
#         c=c+1
#     elif i.islower()==True:
#         z=z+1
#     print("num of uppercases:",c)
#     print("num of lowercases:",z)


# ------------------------------------reverse the sentence----------------------------------


# a="Have a nice day"
# c=a.split(" ")
# print(c)
# b=c[::-1]
# print(b)
# x=".".join(b)
# print(x)