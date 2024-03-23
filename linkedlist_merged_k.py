class listnode:
    def __init__(self,val):
        self.val=val
        self.next=None
def merge1(l1,l2):
    b=listnode(0)
    dummy=b
    while(l1 and l2):
        if l1.val<l2.val:
            dummy.next=listnode(l1.val)
            l1=l1.next
        else:
            dummy.next=listnode(l2.val)
            l2=l2.next
        dummy=dummy.next
    if l1!=None:
        dummy.next=l1
    else:
        dummy.next=l2
    return b.next
def mergegroups(arr):
    result=None
    for data in arr:
        result=merge1(result,data)
    return result
def printval(d):
    while(d!=None):
        print(d.val,end=' ')
        d=d.next
n=int(input())
lists=[]
for i in range(0,n):
    m=int(input())
    d=list(map(int, input().split()))
    current=None
    for j in range(0,m):
        if not current:
            current = listnode(d[j])
            lists.append(current)
        else:
            current.next = listnode(d[j])
            current = current.next
print(lists)
res=mergegroups(lists)
printval(res)
            
            
        
        
            
