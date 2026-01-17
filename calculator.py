def add(a,b):
    return a+b
def sub(a,b):
    return abs(a-b)
def mul(a,b):
    return a*b
def div(a,b):
    try:
     return a/b
    except Exception as e:
        return e

while True:
    print("*******CALCULATOR*************")
    print("1.Addition\n2.substraction\n3.multiplication\n4.division\n5.exit\n")
    choice=int(input("enter your choice : "))
    if choice in {1,2,3,4}:
        a=int(input("enter no."))
        b=int(input("enter no."))

    if choice==1:
        print("Result: ",add(a,b))
    elif choice==2:
        print("Result: ",sub(a,b))
    elif choice==3:
        print("Result: ",mul(a,b))
    elif choice==4:
        print("Result: ",div(a,b))
    elif choice==5:
        break
    else:
       print("invalid input")