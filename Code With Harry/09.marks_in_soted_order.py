l = []
for i in range (0,6):
    marks = int(input(f"Enter marks for student {i+1}: "))
    l.append(marks)
print(l)
l.sort()
print(l)
