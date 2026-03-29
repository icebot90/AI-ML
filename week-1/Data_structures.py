# #binary search
# def binary_search(n):
#     a=0
#     b=len(n)-1
#     ele=int(input("Enter the element to be searched: "))
#     while a<=b:
#         m=b-a//2
#         if n[m]==ele:
#             return f"Element was found at {m} location"
#         elif ele<n[m]:
#             b=m-1
#         else:
#             a=m+1
#     return "Element was not found"
# k=int(input("Enter the number of elements in the list: "))
# n=[]
# print("Enter the elements of list in ascending order.")
# for i in range(k):
#     n.append(int(input()))
# print(binary_search(n))

#stack implementation using lists
def push(stack):
    top=len(stack)-1
    ele=int(input("Enter the element to be pushed: "))
    top+=1
    stack.append(ele)
    print("Push complete.")

def pop(stack):
    top=len(stack)-1
    stack.remove(stack[top])
    print("Pop complete.")

def show(stack):
    print(stack)

stack=[]
cont=True
while cont==True:
    x=int(input("Enter the operation to be performed:\n1.Push.\n2.Pop.\n3.Show.\n4.Exit\n: "))
    if x==1:
        push(stack)
    elif x==2:
        pop(stack)
    elif x==3:
        show(stack)
    else:
        cont=False
print("Thank You...")
