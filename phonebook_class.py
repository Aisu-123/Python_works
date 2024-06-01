d={}
k={}
class phonebook:
        k={}
    
class add(phonebook):
            d={}
            def create(self):
                    name=input("enter your name:")
                    address=input("enter the address:")
                    phnum=int(input("enter the phnnum:"))
                    email=input("enter the email:")
                    self.d["name"]=name
                    self.d["address"]=address
                    self.d["phnum"]=phnum
                    self.d["email"]=email
                    self.k[name]={"name":name,"address":address,"phnum":phnum,"email":email}
            def show(self):
                    print(self.k)

    
class update(phonebook):
            def udn(self):
                    udname=input("which name do you want to update:")
                    temp=self.k.pop(udname)
                    newname=input("enter newname:")
                    self.k[newname]=temp
                    self.k[newname]["name"]=newname
                    print(self.k)
            def udadd(self):
                    udname=input("which name do you want to update:")

                    newaddress=input("enter the new address:")
                    self.k[udname]["address"]=newaddress
                    print(self.k)
            def udphn(self):
                    udname=input("which name do you want to update:")
                    newphnum=int(input("enter new phnumber:"))
                    self.k[udname]["phnum"]=newphnum
                    print(self.k)
            def udeml(self):
                    udname=input("which name do you want to update:")
                    newemail=input("enter new email:")
                    self.k[udname]["email"]=newemail
                    print(self.k)
class delete(phonebook):
        def delrow(self):
               self.delname=input("which name do you want to delete:") 
               del self.k[self.delname]
               print(self.k)
        def delfield(self):
               self.delname=input("which name do you want to delete:")
               delfd=input("which field do you want to update:")
               del self.k[self.delname][delfd]
               print(self.k)
while True: 
    a=int(input("enter your choicen"))

    if a==1:
            obj=add()
            obj.create()
            obj.show()

    if a==2:
        a1=int(input("enter your choicen"))
        obj1=update()
        if a1==1:
            obj1.udn()
        elif a1==2:
            obj1.udadd()
        elif a1==3:
            obj1.udphn()
        elif a1==4:
            obj1.eml()
    if a==3:
        a2=int(input("enter your choice:"))
        obj2=delete()
        if a2==1:
               obj2.delrow()
        elif a2==2:
               obj2.delfield()