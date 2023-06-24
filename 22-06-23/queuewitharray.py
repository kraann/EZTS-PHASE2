queue=[]
def enqueue():
    element=input("Enter element:")
    queue.append(element)
    print(element,"is added in queue")

def dequeue():
    if not queue:
        print("Queue is empty")
    else:
        e=queue.pop()
        print("removed element",e)

def display():
    print(queue)
while True:
    print("select operation 1.Enqueue 2.Dequeue 3.Display 4.Quit")
    choice=int(input())
    if choice==1:
        enqueue()
    elif choice==2:
        dequeue()
    elif choice==3:
        display()
    elif choice==4:
        print("             ************Thank You****************")
        print("             **************Exited******************")
        break
    else:
        print("select correct choice:")
