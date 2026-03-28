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

#fibonacci series
def fibonacci(n):
    if n==0: 
        return "Invalid number"
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

x=int(input("Enter the number fibonacci elements required: "))
print(fibonacci(x))
