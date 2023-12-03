str1 = input("Enter your comment:\n")
if "make a lot of money" in str1 or "Buy Now" in str1 or "Subscribe This" in str1 or "Click This" in str1:
    print ("It\'s a spam comment")
else:
    print ("Not a spam comment")