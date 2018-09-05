import math,os

#INPUT FUNCTION
def inp():
	try:
		x=float(input("Enter a Number"))
	except:
		print("YOU DIDN'T ENTER A NUMBER.")
	else:
		return x;

#CHOICE FUNCTION
def choice(n):
	notdone=True
	while notdone:
		a=0
		b=0
		if n==1:
			a=inp()
			b=inp()
			answer=a+b
			notdone=False
		elif n==2:
			a=inp()
			b=inp()
			answer=a-b
			notdone=False
		elif n==3:
			a=inp()
			b=inp()
			answer=a*b
			notdone=False
		elif n==4:
			a=inp()
			while b==0:
				b=inp()
				if b==0:
					print("please enter a NON-ZERO VALUE")
			answer=a/b
			notdone=False
		elif n==5:
			a=inp()
			answer=math.sqrt(a)
			notdone=False
		elif n==6:
			a=inp()
			answer=a**(1/3)
			notdone=False
		elif n==7:
			a=inp()
			answer=math.log2(a)
			notdone=False
		elif n==8:
			a=inp()
			answer=math.log10(a)
			notdone=False
		elif n==9:
			a=inp()
			answer=math.sin(math.radians(a))
			notdone=False
		elif n==10:
			a=inp()
			answer=math.cos(math.radians(a))
			notdone=False
		elif n==11:
			a=inp()
			answer=math.tan(math.radians(a))
			notdone=False
		elif n==12:
			a=inp()
			answer=math.factorial(a)
			notdone=False
		else:
			notdone=True
	return answer

#MENU FUNCTION
def menu():
	print('1. Addition\n2. Subtraction\n3. Multiplication \n4. Division \n5. Square Root \n6. Cube Root \n7. Log(base 2) \n8. Log(base 10) \n9. Sin \n10. Cos \n11. Tan \n12. Factorial')

#ASK FOR RESTART
def restart():
	done=False
	while done==False:
		zeta=input('DO YOU WANT TO EXIT? [Y/N]')
		if(zeta.lower()=='y' or zeta.lower()=='n'):
			done=True
			return zeta.lower()=='y'
		else:
			print('Please enter Y or N.')


#MAIN FUNCTION
def main():
	print('WELCOME TO THE SCIENTIFIC CALCULATOR:')
	print('Enter the type of operation you want to carry:')
	menu()
	ch=inp()
	answer=choice(ch)
	print("YOUR ANSWER IS: ", answer)

#REAL PROG	
done=False
while done==False:
	os.system('cls')
	main()
	done=restart()