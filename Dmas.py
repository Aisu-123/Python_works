while True:
    a=int(input("select from the choice: \n1.add \n2.substract \n3.multiplication \n4.division \nEnter your choice:"))
    b=int(input("enter the first number:"))
    c=int(input("Enter the second number:"))

    if a==1:
        def show(b,c):
            print(b+c)

        show(b,c)
        
    elif a==2:
        def show(b,c):
            print(b-c)

        show(b,c)
        
    elif a==3:
        def show(b,c):
            print(b*c)

        show(b,c)
    elif a==4:
        def show(b,c):
            print(b/c)

        show(b,c)
    else :
        print("invalid")
        break