from os import system
#BINARY TO DECIMAL
def binaryToDecimal():
	'''
	Asks for a BINARY number OF 8 BITS and coverts it into a DECIMAL NUMBER
	INPUT: BINARY
	OUTPUT: DECIMAL
	'''
	done=False
	while done==False:
		x=inp()
		z=str(x)
		l=len(z)
		decimal=0
		if(x<=11111111 and l==8):
			done=True
			if z[0]=='1':
				decimal+=128
			if z[1]=='1':
				decimal+=64
			if z[2]=='1':
				decimal+=32
			if z[3]=='1':
				decimal+=16
			if z[4]=='1':
				decimal+=8
			if z[5]=='1':
				decimal+=4
			if z[6]=='1':
				decimal+=2
			if z[7]=='1':
				decimal+=1
		else:
			print('ENTER An 8 BIT BINARY')
	return decimal




#DECIMAL TO BINARY
def decimalToBinary():
	'''
	Asks for a DECIMAL number LESS THAN 256 and coverts it into an 8 binary number
	INPUT: DECIMAL
	OUTPUT: BINARY
	'''
	done=False
	binary=[0,0,0,0,0,0,0,0]
	while done==False:
		x=inp()
		if(x<256):
			done=True
			if (x>=128):
				binary[0]=1
				x-=128
			if(x>=64):
				binary[1]=1
				x-=64
			if(x>=32):
				binary[2]=1
				x-=32
			if(x>=16):
				binary[3]=1
				x-=16
			if(x>=8):
				binary[4]=1
				x-=8
			if(x>=4 ):
				binary[5]=1
				x-=4
			if(x>=2):
				binary[6]=1
				x-=2
			if(x==1):
				binary[7]=1
				x-=1
		else:
			print('ENTER A NUMBER LESS THAN 256')
	z=''.join(str(e) for e in binary)
	return z

#TAKE INPUT
def inp():
	try:
		x=int(input('Enter a NUMBER'))
	except:
		print('Please enter a valid integer')
	else:
		return x

#CHOOSE OPERATION
def conversionChoice():
	print('WHICH CONVERSION DO YOU WANT TO PERFORM \n 1. BINARY TO DECIMAL \n 2. DECIMAL TO BINARY')
	done=False
	while done==False:
		x=inp()
		if(x==1 or x==2):
			done = True
			if (x == 1):
				return 'btd'
			else:
				return 'dtb'
		else:
			print('PLEASE ENTER A VALID CHOICE')


#MAIN FUNCTION
def main():
	choice=conversionChoice()
	if choice == 'btd':
		answer=binaryToDecimal()
	else:
		answer=decimalToBinary()
	print("ANSWER: ", answer)

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



#FLOW
done=False
while done == False:
	system("cls")
	main()
	done = restart()
print('BYE!')
