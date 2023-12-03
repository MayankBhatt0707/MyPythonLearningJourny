a= int(input("Enter number 1: "))
b= int(input("Enter number 2: "))
c= int(input("Enter number 3: "))


def greatest(a,b,c):
    if a>b and a>c:
        return (f"{a} is the greatest")
    elif b>a and b>c:
        return (f"{b} is the greatest")
    else:
        return (f"{c} is the greatest")
    
print(greatest(a,b,c))