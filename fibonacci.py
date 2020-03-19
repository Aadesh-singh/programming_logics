list=[]
for i in range(1,20):
    if (len(list) < 1):
        list.append(1)
    elif(len(list) == 1):
        list.append(1)
    else:
        c = list[i-3]+ list[i-2]
        list.append(c)

print('Febonacci series : ',list)


    
