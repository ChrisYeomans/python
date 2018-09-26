import sys, math

someNum = sys.stdin.readline()
g = 9.81

def hAtX(x, thet, grav, vel,):
	return(x*math.tan(thet) - grav*(x**2)*(1+(math.tan(thet))**2)/(2*vel**2))

for i in sys.stdin:
	inpLst = i.split()
	v = float(inpLst[0])
	theta = float(inpLst[1])
	theta = math.radians(theta)
	d = float(inpLst[2])
	h1 = float(inpLst[3])
	h2 = float(inpLst[4])
	height = hAtX(d, theta, g, v)
	#print(height)
	if (height >= h1+1) & (height <= h2-1):
		print("Safe")
	else:
		print("Not Safe")