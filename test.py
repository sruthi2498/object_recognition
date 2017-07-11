import os
#fpath=os.path.join("data/pos", "annotations.txt")
fpath="bg.txt"
f=open(fpath,'a+')
add='/home/sruthi/dev/opencv_workspace/data/neg/'

rows=[]
for row in f:
	row=row.rstrip()
	#row=row.replace('/home/sruthi/dev/opencv_workspace/data/pos/','')
	#print row
	row=add+row
	#row=row.replace()
	rows.append(row)
	print row
	row=""

for row in rows:
	print row
	#f.write(row+"\n")