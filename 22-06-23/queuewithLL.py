class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class queue:
    def __init__(self):
        self.head=None
        self.last=None

    def enqueue(self,data):
        if self.last is None:
            self.head=Node(data)
            self.last=self.head
        else:
            self.last.next=Node(data)
            self.last=self.last.next
            return to_return
a_queue=queue()
while True:
    print('enqueue <value>')
    print('dequeue')
    print('quit')
    do=input('what would you like to do?')
    operation=do[0].strip().lower()
    if operation=='enqueue':
        a_queue.enqueue(int(do[1]))
    elif operation=='dequeue':
        dequeued=a_queue.dequeue()
        if dequeued is None:
            print("stack is empty")
        else:
            print("dequeued value:",int(dequeued))
    elif operation=='quit':
        break
    else:
        print("select correct option:")
            
