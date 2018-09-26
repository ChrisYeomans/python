import sys, math

num = int(sys.stdin.readline())
grps = math.floor(num/3)
arrLst = []
totCst = 0

for i in sys.stdin:
	arrLst.append(int(i))

arrLst = sorted(arrLst, reverse=True)

j = 0
while j+2<len(arrLst):
	totCst+=arrLst[j]+arrLst[j+1]
	#print(arrLst)
	#print(totCst)
	j+=3

while j < len(arrLst):
	totCst+=arrLst[j]
	j+=1

print(totCst)