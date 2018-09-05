pi=0
i=1
j=0;
z=10**8
while i<z:
    if j%2==0:
        pi+=4/(i)
    else:
        pi-=4/(i)
    j+=1
    i+=2
print(pi)