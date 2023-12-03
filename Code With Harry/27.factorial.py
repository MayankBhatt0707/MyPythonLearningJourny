n = int(input("Enter a number for which you want the factorial: "))
fact = 1

if n==0 or n==1:
    fact = 1
else:
    for i in range (1, n+1):
        fact = fact * i

print (fact)