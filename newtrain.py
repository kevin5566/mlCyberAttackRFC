import sys
from sets import Set

data_path = sys.argv[1] #'/home/lab249/ML2016/final/data/'
data = Set([])

file = open(data_path + 'train', 'r')
for line in file:
	data.add(line)
file.close()

file = open('newtrain.txt', 'w')
for i in range(len(data)):
	file.write(data.pop())
file.close()
