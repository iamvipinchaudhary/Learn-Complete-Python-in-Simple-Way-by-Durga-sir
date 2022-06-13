# Biggest three Numbers
n1 = int(input("Enter first number:"))
n2 = int(input("Enter second Number:"))
n3 = int(input("Enter third Number:"))
if n1 > n2 and n1 > n3:
    print("Biggest Number is:", n1)
elif n2 > n3:
    print("Biggest Number is:", n2)
elif n1 == n2 == n3:
    print("All Numbers are equal:")
else:
    print("Biggest Number is:", n3)
