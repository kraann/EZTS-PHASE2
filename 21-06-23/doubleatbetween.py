class Node:
    def _init_(self,data):
        self.data=data
        self.prev=None
        self.next=None
class dll:
    def _init_(self):
        self.head=None
        
    def insert__pos(self,pos):
        n=Node(44)
        temp=self.head
        for i in range(1,pos-1):
            temp=temp.next
        n.prev=temp
        n.next=temp.next
        temp.next.prev=n
        temp.next=n           
    def display(self):
        if self.head is None:
            print("Empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"<-->",end=" ")
                temp=temp.next 
                    
l=dll()
n1=Node(100)
l.head=n1
n2 = Node(200)
n2.prev=n1
n1.next=n2
n3=Node(300)
n3.prev=n2
n2.next=n3
l.insert__pos(2)
l.display()
