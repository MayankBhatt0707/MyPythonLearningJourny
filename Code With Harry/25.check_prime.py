num = int(input("Enter a number: "))

l = int(num/2)

for i in range (2, l):
    if num % i == 0:
        print (f"{num} is not prime")
        break
else:
    print (f"{num} is prime")
    
