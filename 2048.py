import sys

def left(lst):
	for i in lst:
		pushLeft(i)
		combLeft(i)
		pushLeft(i)
	return(lst)

def pushLeft(lst):
	for j in range(len(lst)-1):
		tmpLst = lst[:]
		if (lst[j+1] != 0) & (lst[j] == 0):
			lst[j] = tmpLst[j+1]
			lst[j+1] = tmpLst[j]
			pushLeft(lst)
	return(lst)

def combLeft(lst):
	for j in range(len(lst)-1):
		tmpLst = lst[:]
		if (lst[j+1] == lst[j]):
			lst[j] = tmpLst[j]*2
			lst[j+1] = 0
	return(lst)

def right(lst):
	for i in lst:
		i.reverse()
		pushLeft(i)
		combLeft(i)
		pushLeft(i)
		i.reverse()
	return(lst)

def up(lst):
	outLst = [ [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0] ]
	for i in range(4):
		tmpLst = []
		for j in range(4):
			tmpLst.append(lst[j][i])
		pushLeft(tmpLst)
		combLeft(tmpLst)
		pushLeft(tmpLst)
		for e in range(4):
			outLst[e][i] = tmpLst[e]
	return(outLst)

def down(lst):
	outLst = [ [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0] ]
	for i in range(4):
		tmpLst = []
		for j in range(4):
			tmpLst.append(lst[j][i])
		tmpLst.reverse()
		pushLeft(tmpLst)
		combLeft(tmpLst)
		pushLeft(tmpLst)
		tmpLst.reverse()
		for e in range(4):
			outLst[e][i] = tmpLst[e]
	return(outLst)

l1 = list(map(int, sys.stdin.readline().split()))
l2 = list(map(int, sys.stdin.readline().split()))
l3 = list(map(int, sys.stdin.readline().split()))
l4 = list(map(int, sys.stdin.readline().split()))
dctn = int(sys.stdin.readline())

inpLst = []
inpLst.append(l1)
inpLst.append(l2)
inpLst.append(l3)
inpLst.append(l4)

if dctn == 0:
	for l in (left(inpLst)):
		print(' '.join(str(e) for e in l))
elif dctn == 1:
	for l in (up(inpLst)):
		print(' '.join(str(e) for e in l))
elif dctn == 2:
	for l in (right(inpLst)):
		print(' '.join(str(e) for e in l))
elif dctn == 3:
	for l in (down(inpLst)):
		print(' '.join(str(e) for e in l))
