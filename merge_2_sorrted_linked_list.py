class listnode:
    def __init__(self,val):
        self.val=val
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
        self.head1=None
    def addele1(self,val):
        temp=listnode(val)
        if self.head is None:
            self.head=temp
            return
        else:
            t=self.head
            while(t.next!=None):
                t=t.next
            t.next=temp
    def addele2(self,val):
        temp=listnode(val)
        if(self.head1==None):
            self.head1=temp
            return
        else:
            t=self.head1
            while(t.next!=None):
                t=t.next
            t.next=temp
    def merge_sorted(self):
        t1=self.head
        t2=self.head1
        t=listnode(0)
        dump=t
        while(t1 and t2):
            if(t1.val<t2.val):
                dump.next=listnode(t1.val)
                t1=t1.next
            else:
                dump.next=listnode(t2.val)
                t2=t2.next
            dump=dump.next
        if(t1!=None):
            dump.next=t1
        else:
            dump.next=t2
        return t.next
l=LinkedList()
n=int(input("no of elements for linkedlist 1:"))
print("Enter elements:")
for i in range(0,n):
    b=int(input())
    l.addele1(b)
m=int(input("no of elements for linkedlist 2:"))
print("Enter elements:")
for i in range(0,m):
    b=int(input())
    l.addele2(b)
t=l.merge_sorted()
while(t!=None):
    print(t.val,end=' ')
    t=t.next



            
                
                
    
    
        
    
    
                
                
