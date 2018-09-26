import sys

for i in sys.stdin:
	out = "Jolly"
	lst = i.split(" ")
	#print(lst)
	first = True
	lastDiff = 0
	diff = 0

	for j in range(len(lst)-2):
		diff = abs(int(lst[j+1]) - int(lst[j+2]))
		#print(diff)
		if first == True:
			lastDiff = diff
			first = False
			#print("initLastDiff")
			#print(diff)
		elif diff == lastDiff - 1:
			lastDiff = diff
			#print("redoLastDiff")
		else:
			out = "Not jolly"
			#print("not Jolly")
			break
	print(out)
