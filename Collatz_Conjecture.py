from os import system
#TAKE INPUT
def inp():
	try:
		x=int(input('Enter a NUMBER'))
	except:
		print('Please enter a valid integer')
	else:
		return x
#ASK FOR RESTART OR EXIT
def restart():
	ask=True
	while ask==True:
		res=input('DO YOU WANT TO EXIT ? [Y/N]')
		if(res.lower()=='y' or res.lower()=='n'):
			ask=False
			return res.lower()=='y'
		else:
			print('PLEASE ENTER "Y" FOR YES AND "N" FOR NO')
#MAIN
def main():
	x=inp()
	k=0
	while x!=1:
		k+=1
		if x%2==0:
			x/=2
			print(x,'\n')
		else:
			x=(3*x)+1
			print(x,'\n')
	print('Steps: ',k,'\n')
#FLOW
done=False
while done == False:
	system("cls")
	main()
	done = restart()
print('BYE!')
