def fact(n):
    if n==0 | n==1:
        return 1
    else:
        return n*(fact(n-1))
num=int(input("enter a number"))
factorial=fact(num)
print(f"factorial of {num} is: {factorial}")
