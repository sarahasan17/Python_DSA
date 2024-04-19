class node:
    def __init__(self,val):
        self.data=val
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def insert(self,a):
        t=node(a)
        if self.head==None:
            self.head=t
        else:
            temp=self.head
            while(temp.next!=None):
                temp=temp.next
            temp.next=t
    def display_alt(self):
        t=self.head
        while(t!=None):
            print(t.data,end=' ')
            if(t.next!=None): t=t.next.next
            else: break
b=input()
b=b.split(' ')
l=LinkedList()
for i in b:
    l.insert(i)
l.display_alt()
