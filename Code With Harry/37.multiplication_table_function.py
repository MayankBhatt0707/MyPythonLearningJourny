def mult_table(number):
    result = ""
    for i in range(1,11):
        result += f"{number} * {i} = {i*number} \n"
    return result
    
            
    
n = int(input("Enter the number for which you want to print multiplication table: "))
print(mult_table(n))