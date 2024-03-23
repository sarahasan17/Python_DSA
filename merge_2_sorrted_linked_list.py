class listnode:
    def __init__(self,data):
        self.data=data
        self.next=None
def insertele(val):
        t=listnode(0)
        dummy=t
        for i in val:
            dummy.next=listnode(i)
            dummy=dummy.next
        return t.next
            
def mergeele(l1,l2):
    t=listnode(0)
    curr=t
    while(l1 and l2):
        if(l1.data<l2.data):
            curr.next=l1
            l1=l1.next
        else:
            curr.next=l2
            l2=l2.next
        curr=curr.next
    if l1:
        curr.next=l1
    else:
        curr.next=l2
    return t.next

l1=[1,2,3,6]
l2=[4,5,7]
m=insertele(l1)
n=insertele(l2)
merge=mergeele(m,n)
while merge:
    print(merge.data,end=' ')
    merge=merge.next
    
    
                
                
