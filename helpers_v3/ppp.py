import math
distance = 10
naive = 50/(math.log(float(distance)+1))
if naive>100:
	print 100
elif naive<0:
	print 0
else:
	print naive