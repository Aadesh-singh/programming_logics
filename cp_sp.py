
print("Enter the cost price: ")
cp=int(input())
print("Enter the selling price: ")
sp=int(input())
if(cp>sp):
    cp=cp-sp
    print("INCURRED LOSS of : ",cp)
else:
    sp=sp-cp
    print("Hurray!!!,Made Profit of : ",sp)



