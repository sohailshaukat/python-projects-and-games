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
i=n+1
while (prime(i)==False):
	i+=1
print('Next prime is ',i)