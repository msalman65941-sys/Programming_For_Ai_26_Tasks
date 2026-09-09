rows=int(input("Enter Number Of Rows: "))
for i in range(1, rows+1):
    for j in range(i):
        print("*",end="")
    print()
print()
for i in range(rows, 0, -1):
    print("*" * i)