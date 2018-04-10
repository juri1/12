import csv
import numpy as np

file1 = open('validpreds.csv', 'r')
reader = csv.reader(file1)
ctr = [0]

for line in reader:
    ctr.append(line[0])

file1.close()

line_count=0

c=20.0
lambda_1= 5.7*1e-07

file2 = open('bids.csv', 'w')
writer = csv.writer(file2)
bid=0.0

for i in ctr:
    line_count=line_count+1
    bid = np.sqrt((c/lambda_1)* i + c*c ) - c

    writer.writerow([bid])

file2.close()




