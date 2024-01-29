nterm = int(input("Enter the nterm for Fibonacci Series: "))

num1=0
num2=1

print("Here is the Fibonacci Series: ")

for i in range(nterm):
    print(num1)
    newnum = num1 + num2
    num1 = num2
    num2 = newnum