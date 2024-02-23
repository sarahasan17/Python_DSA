class node:
    def __init__(self,data):
        self.data=data;
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    def insert_at_begin(self,data):
        new_node=node(data)
        if(self.head==None):
            self.head=new_node
            return
        else:
            new_node.next=self.head
            self.head=new_node
    def insert_at_end(self,data):
        new_node=node(data)
        if(self.head==None):
            self.head=new_node
            return
        else:
            temp=self.head
            while(temp.next!=None):
                temp=temp.next
            temp.next=new_node
    def insert_at_pos(self,data,pos):
        new_node=node(data)
        if(pos==0):
            new_node.next=self.head
            self.head=new_node
            return
        temp=self.head
        temp1=temp.next
        c=0
        while(c==pos):
            temp=temp.next
            temp1=temp1.next
            c+=1
        temp.next=new_node
        new_node.next=temp1
    def delete_end(self):
        if(self.head.next==None):
            self.head=None
        temp=self.head
        temp1=temp.next
        while(temp1.next!=None):
            temp=temp.next
            temp1=temp1.next
        temp.next=None
        
    def delete(self,pos):
        if(pos==0):
            self.head=self.head.next
            return
        else:
            c=0
            temp=self.head
            temp1=temp.next
            while(c!=pos-1):
                c+=1
                temp=temp.next
                temp1=temp.next
                    
            temp.next=temp1.next
    def display(self):
        temp=self.head
        while(temp!=None):
            print(temp.data)
            temp=temp.next
ll=linkedlist()
ll.insert_at_begin(1)
ll.insert_at_begin(2)
ll.insert_at_end(3)
ll.insert_at_pos(4,2)
ll.delete(3)
ll.delete_end()
ll.display()
        
