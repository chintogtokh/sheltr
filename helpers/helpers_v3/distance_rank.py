import csv
import math

'''

229 numbers

'''

# with open('ITERATION_2_TMP.csv', 'wrb') as csvfile:
#     readr = csv.reader(csvfile, delimiter=',')
#     # readr.next()
#     readr.next()
#     for line in readr:
#         print json.dumps(row_to_obj(line))
# 		#if(line[0]=="BROWN HILL"):
#             #print line
#             #print line[620]
# #print json.dumps(row_to_obj(line))


r = csv.reader(open('ITERATION_2_TMP.csv')) # Here your csv file
lines = list(r)
for i,v in enumerate(lines):
	if i==0:
		continue
	for uniindex in xrange(170,399):
		naive = 100/(math.log(float(lines[i][uniindex])+1))+50
		if naive>100:
			lines[i][uniindex+229]=100
		else:
			lines[i][uniindex+229]=naive
writer = csv.writer(open('output.csv', 'w'))
writer.writerows(lines)