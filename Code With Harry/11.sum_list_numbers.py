l = []
sum = 0
for i in range(0,4):
    a = int(input(f"Enter number {i+1}: "))
    l.append(a)
    sum += l[i]
print(l)
print(sum)