list=[]
for i in range(1,5000):
    k=str(i)
    j=len(k)

    if(j==1):
        if(i==i*i*i):
            list.append(i)
    elif(j==2):
        p=int(k[0])
        h=int(k[1])
        if(i==(p*p*p)+(h*h*h)):
            list.append(i)
    elif(j==3):
        p=int(k[0])
        h=int(k[1])
        n=int(k[2])
        if(i==(p*p*p)+(h*h*h)+(n*n*n)):
            list.append(i)
    elif(j==4):
        p=int(k[0])
        h=int(k[1])
        n=int(k[2])
        f=int(k[3])
        if(i==(p*p*p)+(h*h*h)+(n*n*n)+(f*f*f)):
            list.append(i)
print('list of armstrong number : ',list)
