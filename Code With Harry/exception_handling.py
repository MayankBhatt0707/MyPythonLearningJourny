try:
    lst = [int(x) for x in input().split()]
    i = int(input("Enter Index: "))
    print(lst[i])
        
except Exception as e:
        print("Exception Occured: ", e)
        lst = 0
finally:
            print(lst)
        