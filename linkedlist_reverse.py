class node:
    def __init__(self,val):
        self.val=val
        self.next=None
class linkedList:
    def __init__(self):
        self.head=None
        self.count=0
    def addele(self,val):
        t=node(val)
        if(self.head==None):
            self.head=t   
            self.count+=1 
            return
        else:
            temp=self.head
            while(temp.next!=None):
                temp=temp.next
            temp.next=t 
            self.count+=1 
    def display(self):
        temp=self.head
        while(temp!=None):
            print(temp.val,end=' ')
            temp=temp.next
        print()
    def reverse(self):
        prev=None
        curr=self.head
        next_node=None
        while(curr):
            next_node=curr.next
            curr.next=prev
            prev=curr
            curr=next_node
        self.head=prev
l=linkedList()
val=[]
for i in range(0,4):
    r=int(input())
    l.addele(r)
l.display()
l.reverse()
l.display()

    
            
        
        
