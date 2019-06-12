from os import system
import math

#INPUT FUNCTION
def inp():
	fin=False
	while fin==False:
		try:
			i=float(input("*Enter a value*"))
		except:
			print("ENTER A NUMERIC VALUE")
		else:
			fin=True
			return i

#ASK NUMBER OF POINTS
def number():
	print("ENTER THE NUMBER OF POINTS: ")
	num=inp()
	return int(num)

#TOFETCHCOORD
def coord():
    print("ENTER X , Y , AND Z :")
    print("X: ")
    x=inp()
    print("Y: ")
    y=inp()
    print("Z: ")
    z=inp()
    return (x,y,z)

#CREATE A MULTIDIMENSIONAL LIST
def graph(length):
	i=0
	gra=[()]*length
	while i<length:
		(x,y,z)=coord()
		gra[i]=(x,y,z)
		print(f"Point {i+1} is {gra[i]}" )
		i+=1
	return gra

#CALCULATE ALL POSSIBLE DISTANCES
def distance_calc(p,length):
	t=p
	dicti={}
	for i in range (length):
		for j in range (i+1,length):
			(x,y,z)=(p[i][0]-p[j][0],p[i][1]-p[j][1],p[i][2]-p[j][2])
			d=math.sqrt((x**2)+(y**2)+(z**2))
			str1="DISTANCE between ("+ str(p[i])+")("+ str(p[j])+")"
			dicti[str1]=d
	return dicti

#SHORTEST DISTANCE
def shorty(dicti):
	x=list(dicti.values())
	y=99999999
	k=1040
	for i in range (len(x)):
		if x[i]<y:
			y=x[i]
			k=i
	return (y,k)

#MAIN
def main():
	length=number()
	plane=graph(int(length))
	dicti=distance_calc(plane,length)
	(z,k)=shorty(dicti)
	print(f"SHORTEST DISTANCE: {z}")
	co=list(dicti.keys())
	print(co[k])

#RESTART
def restart():
	ask=True
	while ask==True:
		res=input('DO YOU WANT TO EXIT ? [Y/N]')
		if(res.lower()=='y' or res.lower()=='n'):
			ask=False
			return res.lower()=='y'
		else:
			print('PLEASE ENTER "Y" FOR YES AND "N" FOR NO')

done=False
while done==False:
	system("cls")
	main()
	done=restart()
print("BYE!")
