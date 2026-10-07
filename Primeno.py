n1=int(input("Enter start: "))
n2=int(input("Enter end: "))
for n in range(n1,n2+1):
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                break
        else:
            print(n)
