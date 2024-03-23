class listnode:
    def __init__(self,val):
        self.val=val
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
        self.size=0
    def addele(self,val):
        e=listnode(val)
        if(self.head==None):
            self.head=e
            self.size+=1
            return
        else:
            t=self.head
            while(t.next!=None):
                t=t.next
            t.next=e
            self.size+=1
    def reverse_list(self,data):
        prev=None
        next1=None
        curr=data
        while(curr):
            next1=curr.next
            curr.next=prev
            prev=curr
            curr=next1
        return prev
    def palindrome(self):
        t=self.head
        flag=True
        if(self.size%2==0):
            c=self.size//2
        else:
            c=(self.size+1)//2
        for i in range(1,c):
            t=t.next
            rev=self.reverse_list(t)
            while(self.head and rev):
                if(self.head.val!=rev.val):
                    flag=False
                    break
                self.head=self.head.next
                rev=rev.next
        if flag:
            print(True)
        else:
            print(False)
l=LinkedList()
n=int(input("no of elements for linkedlist:"))
print("Enter elements:")
for i in range(0,n):
    b=int(input())
    l.addele(b)
l.palindrome()
                
                
        
