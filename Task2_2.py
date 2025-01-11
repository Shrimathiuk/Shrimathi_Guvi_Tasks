# 2. Write a pyramid of numbers 1 to 20 using For loop
levels = int(input("Enter number of rows: "))

for i in range(levels):
    for j in range(i+1):
        print(j+1, end=" ")
    print("\n")