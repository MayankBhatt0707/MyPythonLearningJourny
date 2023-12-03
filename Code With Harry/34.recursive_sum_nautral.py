def sum(n):
    if n==1:
        return 1
    else:
        total = n + sum(n-1)
        return total

n = int(input("Enter the range for natural numbers: "))
print(sum(n))