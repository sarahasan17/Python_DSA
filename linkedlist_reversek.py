class listnode:
    def __init__(self,val):
        self.val=val
        self.next=None
def addele(val):
    t=listnode(0)
    dummy=t
    for i in val:
        dummy.next=listnode(i)
        dummy=dummy.next
    return t.next
def printele(valu):
    while(valu!=None):
        print(valu.val,end=' ')
        valu=valu.next
def reverse_k(data,k):
    def reverse_group(prop,k):
        prev=None
        curr=prop
        next_node=None
        c=0
        while(curr!=None and c<k):
            next_node=curr.next
            curr.next=prev
            prev=curr
            curr=next_node
            c=c+1 
        return prev,prop,curr
    l=listnode(0)
    l.next=data
    curr=l
    while(curr.next!=None):
        prev,start,end=reverse_group(curr.next,k)
        curr.next=prev
        start.next=end
        curr=start
    return l.next

l=[1,2,3,4,5,6]
t=addele(l)
t=reverse_k(t,3)
printele(t)
        
        
        
        
