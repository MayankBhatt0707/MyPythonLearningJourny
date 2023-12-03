# Total Marks: 100

m1 = int(input("Enter marks of 1st subject: "))
m2 = int(input("Enter marks of 2nd subject: "))
m3 = int(input("Enter marks of 3rd subject: "))
m4 = int(input("Enter marks of 4th subject: "))

marks_percent = (m1+m2+m3+m4)/4

if (marks_percent >=40):
    if (m1 >= 33 and m2 >= 33 and m3 >= 33 and m4 >= 33):
        print("Congratulations! You are pass!")
    else:
        print("Better Luck next time!!")
