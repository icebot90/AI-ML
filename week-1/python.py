# #prime numbers
# def prime_number(n):
#     for i in range(2,n//2):
#         if n%i==0:
#             return False
#     return True

# a=int(input("Enter a number: "))
# if prime_number(a) is True:
#     print(f"{a} is a prime number")
# else:
#     print(f"{a} is not a prime number")

# #fibonacci series
# def fibonacci(n):
#     a=0
#     b=1
#     fibo=[a,b]
#     for i in range(n-2):
#         fibo.append(a+b)
#         temp=a
#         a=b
#         b=temp+b
#     return fibo

# x=int(input("Enter the number fibonacci elements required: "))
# print(fibonacci(x))

#fibonacci series using recursion
def fibonacci_rec(n):
    if n<=1:
        return n
    else:
        return fibonacci_rec(n-1)+fibonacci_rec(n-2)
c=int(input("Enter the number of terms required: "))
if c<=0:
    print("Enter a positive integer")
else:
    for i in range(c):
        print(fibonacci_rec(i))