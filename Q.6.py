a=int(input("Enter the lenght of the side: "))
b=int(input("Enter the lenght of the side: "))
c=int(input("Enter the lenght of the side: "))
if (a+b)>c and (a+c)>b and(b+c)>a:
    print("Yes")
else:
    print("No")