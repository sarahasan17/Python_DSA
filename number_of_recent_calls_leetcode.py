def finding(ping,valu):
    c=0
    l=[]
    m=[]
    for i in range(0,len(ping)):
        if(ping[i]=="RecentCounter"):
            c=0
            l=[]
        elif(len(l)==0):
            l.append(valu[i])
        else:
            t=valu[i]
            while(t-l[0]>3000):
                l.pop(0)
            l.append(t)
        m.append(len(l))
    return m
ping=["RecentCounter", "ping", "ping", "ping", "ping","ping"]
valu=[0,1,100, 3001, 3002,3100]
print(finding(ping,valu))
