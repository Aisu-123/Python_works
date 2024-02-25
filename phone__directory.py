d={}
k={}
while True:
    print("select your choice \n1.Add \n2.View \n3.Add/Update \n4.Delete \n5.Exit")
    a=int(input('enter your choice:'))    
    if a==1:
        d={}
        n=input('enter your name:')   
        d['name']=n
        p=int(input('enter no of phone no:'))
        ph=[]
        for i in range(p):
            p=int(input(' phone no:')) 
            ph.append(p)  
        d['phone number']=ph
        ad=input('enter the address:')    
        d['address']=ad
        ed=input('enter the emailaddress:')    
        d['address']=ed
        k[n]=d
        print(k)
    if a==2:
            for i,j in k.items():
                for l in j: 
                    print(l+':',j[l])
                print('******************')    
    if a==3:#add/update
        print(k)
        m=input('enter the student name you want to update:')
        if m in k.keys():
            c=input('which field you want to update/ add:')
            z=k[m]
            if c in z.keys():
                print(c)
                if m==z[c]:
                    y=z[c]=input('enter new name:')
                    k[y]=k.pop(m)
                    print(k)
                elif c=='phone number':
                    ph=z['phone number']
                    for i in range(len(ph)):
                        print(ph[i])
                    e=int(input('enter phone number to add/update:'))
                    if e in ph:
                        print(e)
                        ph.remove(e)
                        e=int(input('updated number:'))
                        ph.append(e)    
                    else:
                        ph.append(e)
                    z['phone number']=ph    
                else :
                    z[c]=input('enter the value to update:')
                    print(k)
            else :
                x=input('enter new value:')
                z[c]=x
                d=z
                print(k)
        else :
            print('field not found')        
    if a==4:
        print(k)
        b=input('enter the student name you want to delete:')
        if b in k.keys():
            d=k[b]
            c=int(input('enter field you want to delete \n 1.student\n2.other field\n'))
            if c==1:
                if b in k.keys():
                    k.pop(b)
                    print('student deleted')
            elif c==2:
                nam=input('enter the field name you want to del:') 
                if nam in d.keys():
                    if nam=='phone number':
                        d['name']==k[b]
                        ph=d['phone number']
                        for i in range(len(ph)):
                            print(ph[i])
                        e=int(input('enter phone number to delete:'))
                        if e in ph:
                            ph.remove(e)
                    else:
                        d.pop(nam)
                        print('deleted')
            else:
                print('field not found')
        print(k)                
    if a==5:
        break