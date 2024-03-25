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
    def deletemid(self):
        prev=self.head
        temp=self.head.next
        n=0
        while(n<(self.count-2)//2):
            temp=temp.next
            prev=prev.next
            n+=1 
        prev.next=temp.next
        temp.next=None
    def display(self):
        temp=self.head
        while(temp!=None):
            print(temp.val,end=' ')
            temp=temp.next
        print()
l=linkedList()
val=[]
for i in range(0,4):
    r=int(input())
    l.addele(r)
l.display()
l.deletemid()
l.display()

    
            
        
        
