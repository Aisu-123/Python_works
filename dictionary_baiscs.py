# a={"name":"ammu","age":10,"course":"python","place":"kochi","name":"anu"}
# print(type(a))
# print(len(a))

# ------------------------------doing same purpse to get the content----------


# print(a["name"])
# print(a.get("name"))


# print(a["ammu"])---------we will get error ,bcoz we can only give the key vales-------

# -------------------------to prrint only the keys----------------------------

# print(a.keys())

# ----------------------------to get only the values-----------------------------


# print(a.values())

# --------------------------------to get values and keys------------------------

# print(a.items())

# ----------------------------------------------------------------------

# for i in a:
#     print(i)

# for i in a:
#     print(a[i])

# for i in a.keys():
#     print(i)

# for i in a.keys():
#     print(a[i])


# for i in a.values():
#     print(i)


# for i in a.items():
#     print(i)

# ------------------------------to change----------------------------------------


# a["name"]="akku"
# print(a)

# -------------------------to add---------------------

# a["mark"]=100
# print(a)

# -----------------------------to update---------------------------

# a.update({"name":"babi"})
# print(a)

# a.update({"colour":"red"})
# print(a)

# ------------------------------to pop-----------------

# a.pop("name")
# print(a)

# a.popitem()
# print(a)

# -----------------------------to delete----------

# a.del()
# print(a)

# del a["age"]
# print(a)

# ---------------to clear-------------------

# a.clear()
# print(a)