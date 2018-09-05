a=0
b=1
try:
	n=int(input('Enter N'))
except:
	print('Enter an Integer')
else:
	print('N is equal to ', n)
i=2
while i<n:
	c=a+b
	a=b
	b=c
	i+=1
print(c)