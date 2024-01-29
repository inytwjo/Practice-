nterm = int(input("Enter the nterm for Fibonacci Series: "))

num1=0
num2=1

print("Here is the Fibonacci Series: ")

for i in range(nterm): #looping until nterm 
    print(num1) #displaying first value as 0
    #fibonacci calculation: 
    newnum = num1 + num2
    num1 = num2
    num2 = newnum
