class listnode:
    def __init__(self,val):
        self.val=val
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
        self.head1=None
        self.final=None
    def addele(self,val):
        t=listnode(val)
        if(val%2==0):
            if(self.head==None):
                self.head=t 
                return
            else:
                temp=self.head
                while(temp.next!=None):
                    temp=temp.next
                temp.next=t 
        else:
            if(self.head1==None):
                self.head1=t 
                return
            else:
                temp=self.head1
                while(temp.next!=None):
                    temp=temp.next
                temp.next=t 
    def oddeven(self):
        teven=self.head
        todd=self.head1
        self.final=todd
        t=self.final
        while(t.next!=None):
            t=t.next
        t.next=teven
            
    def display(self):
        temp=self.final
        while(temp!=None):
            print(temp.val,end=' ')
            temp=temp.next
l=linkedlist()
n=int(input())
b=input()
b=b.split(' ')
for i in range(0,n):
    l.addele(int(b[i]))
l.oddeven()
l.display()
    
    
            
        
        
        
    
        
