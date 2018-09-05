def prime(n):
	i=2
	while i<n:
		if n%i==0:
			return False
		i+=1
	return True
		
##############################################################

try:
	n=int(input('Enter An Integer'))
except:
	print("You did not enter an Integer")
else:
	print('N is equal to ',n)
	print('List of Prime numbers :')
i=2
while i<=n:
	if prime(i):
		print (i)
	i+=1 
