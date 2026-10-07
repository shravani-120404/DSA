num=int(input("enter: "))
sum=0
n=num
while num>0:
    sum=sum*10+(num%10)
    num//=10
if  n==sum:
    print("num is palindrome")
else:
    print("num is not palindrome") 