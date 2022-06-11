a = input("Please enter a value for a :  ")
b = input("Please enter a value for b :  ")
if int(a) > int(b):
    print(a, "is greater than ", b)
elif int(a) == int(b):
    print("Both the values are same")
else:
    print(b, "is greater than ", a)

