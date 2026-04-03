#binary search
def binary_search(n):
    a=0
    b=len(n)-1
    ele=int(input("Enter the element to be searched: "))
    while a<=b:
        m=b-a//2
        if n[m]==ele:
            return f"Element was found at {m} location"
        elif ele<n[m]:
            b=m-1
        else:
            a=m+1
    return "Element was not found"
k=int(input("Enter the number of elements in the list: "))
n=[]
print("Enter the elements of list in ascending order.")
for i in range(k):
    n.append(int(input()))
print(binary_search(n))

#stack implementation using lists
def push(stack,top,a):
    ele=int(input("Enter the element to be pushed: "))
    if top==a-1:
        print("Stack is Overflow.") 
        return 
    top+=1
    stack.append(ele)
    print("Push complete.")

def pop(stack,top,a):
    if top<0:
        print("Stack is Underflow.")
        return 
    rem=stack[top]
    stack.remove(rem)
    top-=top
    print(f"Popped {rem}")
    print("Pop complete.")

def peek(stack,top):
    if top<0:
        print("Stack is Underflow.")
        return 
    print(stack[top])

stack=[]
cont=True
a=int(input("Enter maximum number of stack elements: "))
while cont==True:
    top=len(stack)-1
    top=len(stack)-1
    x=int(input("Enter the operation to be performed:\n1.Push.\n2.Pop.\n3.Peek.\n4.Exit\n: "))
    if x==1:
        push(stack,top,a)
    elif x==2:
        pop(stack,top,a)
    elif x==3:
        peek(stack,top)
    else:
        cont=False
        print("Exiting...")

#Queue implementation using list
def enqueue(queue,rear,n):
    ele=int(input("Enter the element to be added: "))
    if rear<n:
        queue.append(ele)
        print(f"Element {ele} is added to queue.")
        rear+=1
    else:
        print("Queue is Overflow")

def dequeue(queue,front,n):
    if front<0:
        ele=queue[front]
        queue.remove(ele)
        print(f"Element {ele} has been removed.")
        front+=1
    else:
        print("Queue is Underflow")

def display(queue):
    print(queue)

n=int(input("Enter the maximum number of elements allowed on the queue: "))-1
queue=[]
front=0
cont=True
while cont==True:
    rear=len(queue)-1
    x=int(input("Enter your choice:\n1.Enqueue\n2.Dequeue\n3.Display\n4.Exit  "))
    if x==1:
        enqueue(queue,rear,n)
    elif x==2:
        dequeue(queue,front,n)
    elif x==3:
        display(queue)
    else:
        cont=False
        print("Exiting....")