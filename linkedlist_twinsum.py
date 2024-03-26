class listnode:
    def __init__(self,val):
        self.val=val
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
        self.tail=None
    def addele(self,val):
        val=listnode(val)
        if(self.head==None):
            self.head=val
            self.tail=val
        else:
            self.tail.next=val
            self.tail=self.tail.next
    def delend(self):
        if(self.head==self.tail):
            m=self.head
            self.head=self.tail=None
            return m
        else:
            t=self.head
            t1=self.head.next
            while(t1.next!=None):
                t1=t1.next
                t=t.next
            m=t1
            t.next=None
            self.tail=t
            return m
    def delbeg(self):
        t=self.head
        if(self.head==self.tail):
            m=self.head
            self.head=self.tail=None
            return m.val
        else:
            m=t
            l=t.next
            t=None
            self.head=l
            return m.val
    def  maxsumneigh(self):
        sum=0
        while(self.head!=None):
            sum1=-100000
            if(self.head==self.tail):
                sum1=self.head.val
            else:
                sum1=self.head.val+self.tail.val
            sum=max(sum,sum1)
            self.delbeg()
            self.delend()
        return sum
l=linkedlist()
n=int(input())
for i in range(0,n):
    b=int(input())
    l.addele(b)
print(l.maxsumneigh())
            
            
        
