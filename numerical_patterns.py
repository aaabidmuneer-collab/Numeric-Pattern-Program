# numerical patterns

# Numeric Pattern Program

a= int(input("Enter number of rows: "))

for i in range(1, a + 1):
    
    for j in range(i, 0, -1):
        print(j, end=" ")
    
    print()