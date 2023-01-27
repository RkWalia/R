num=int(input("Enter number of row: "))

for i in range(0,num+1):
    k=ord("A")+i
    for j in range(0,i+1):
        print(chr(k),end="")
        k+=1
    print()