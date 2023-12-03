a = {
    "Pankha" : "Fan",
    "Kela" : "Banana",
    "Bharat" : "India",
    "Jhanda" : "Flag"
}

print(f"Your options are {a.keys()}")
b = input("Enter a word in Hindi to find its meaning: ")

print (f"{b} in english is {a.get(b)}" )
