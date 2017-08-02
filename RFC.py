import sys
from sklearn.ensemble import RandomForestClassifier

## transfer class variable to 0-1 vector list ##
f=open('./class_to_vector.txt','r')
tranlist=[]
for line in f:
    line=line.strip().split(', ')
    tranlist.append(line)

## training Y transfer list ##
## according to "training_attack_types.txt" ##
classlist=['guess_passwd.', 'nmap.', 'loadmodule.', 'rootkit.', 'warezclient.', 'smurf.', 'portsweep.', 'neptune.', 'normal.', 'spy.', 'ftp_write.', 'phf.', 'pod.', 'teardrop.', 'buffer_overflow.', 'land.', 'imap.', 'warezmaster.', 'perl.', 'multihop.', 'back.', 'ipsweep.', 'satan.']

'''
ynew=['r2l', 'probe', 'u2r', 'u2r', 'r2l', 'dos', 'probe', 'dos', 'normal', 'r2l', 'r2l', 'r2l', 'dos', 'dos', 'u2r', 'dos', 'r2l', 'r2l', 'u2r', 'r2l', 'dos', 'probe', 'probe']
output=['dos','u2r','r2l','probe','normal']
'''

## First, train normal and abnormal ##
ynew=['abnormal', 'abnormal', 'abnormal', 'abnormal', 'abnormal', 'abnormal', 'abnormal', 'abnormal', 'normal', 'abnormal', 'abnormal', 'abnormal', 'abnormal', 'abnormal', 'abnormal', 'abnormal', 'abnormal', 'abnormal', 'abnormal', 'abnormal', 'abnormal', 'abnormal', 'abnormal']
output=['abnormal','normal']


## read training data ##
f=open('./newtrain.csv','r')
tmp=[]
X=[]
Y=[]
cnt=0
for line in f:
	cnt=cnt+1
	if cnt%10000==0:
		print cnt
	line=line.strip().split(',')
	tmp.append(float(line[0]))
	for i in range(len(tranlist)):
		for j in range(len(tranlist[i])):
			if line[i+1]==tranlist[i][j]:
				tmp.append(float(1))
			else:
				tmp.append(float(0))
	for i in range(4,len(line)-1):
		tmp.append(float(line[i]))
	X.append(tmp)   
	tmp=[]
	for i in range(len(classlist)):
		if line[-1]==classlist[i]:
			line[-1]=ynew[i]
			break
	for i in range(len(output)):
		if line[-1]==output[i]:
			tmp.append(float(1))
		else:
			tmp.append(float(0))
	Y.append(tmp)
	tmp=[]

import numpy
X=numpy.asarray(X)
Y=numpy.asarray(Y)

## training ##
rfc=RandomForestClassifier(n_estimators=500, max_features='log2')
rfc.fit(X,Y)

## read testing data ##
data_path = sys.argv[1]
f=open(data_path + 'test.in','r')
tmp=[]
testX=[]
cnt=0
for line in f:
	cnt=cnt+1
	if cnt%10000==0:
		print cnt
	line=line.strip().split(',')
	tmp.append(float(line[0]))
	for i in range(len(tranlist)):
		for j in range(len(tranlist[i])):
			if line[i+1]==tranlist[i][j]:
				tmp.append(float(1))
			else:
				tmp.append(float(0))
	for i in range(4,len(line)):
		tmp.append(float(line[i]))
	testX.append(tmp)   
	tmp=[]
testX=numpy.asarray(testX)

## testing ##
testY=rfc.predict(testX)

prdic=testY[:,0]

## Abnormal have 12 classes ##

ynew=['r2l', 'probe1', 'u2r', 'u2r', 'r2l', 'dos1', 'probe2', 'dos2', 'normal', 'r2l', 'r2l', 'r2l', 'dos3', 'dos4', 'u2r', 'dos5', 'r2l', 'r2l', 'u2r', 'r2l', 'dos6', 'probe3', 'probe4']
output=['dos1','u2r','r2l','probe1','dos2','dos3','dos4','dos5','dos6','probe2','probe3','probe4']
f=open('./newtrain.csv','r')

tmp=[]
X2=[]
Y2=[]
cnt=0
for line in f:
	cnt=cnt+1
	if cnt%10000==0:
		print cnt
	line=line.strip().split(',')
	tmp.append(float(line[0]))
	for i in range(len(tranlist)):
		for j in range(len(tranlist[i])):
			if line[i+1]==tranlist[i][j]:
				tmp.append(float(1))
			else:
				tmp.append(float(0))
	for i in range(4,len(line)-1):
		tmp.append(float(line[i]))
	if line[-1]!='normal.' :
		X2.append(tmp)   
	tmp=[]
	for i in range(len(classlist)):
		if line[-1]==classlist[i]:
			line[-1]=ynew[i]
			break
	for i in range(len(output)):
		if line[-1]==output[i]:
			tmp.append(float(1))
		else:
			tmp.append(float(0))
	if line[-1]!='normal' :
		Y2.append(tmp)
	tmp=[]

import numpy
X2=numpy.asarray(X2)
Y2=numpy.asarray(Y2)
Y3=Y2[:,0]+2*Y2[:,1]+3*Y2[:,2]+4*Y2[:,3]+Y2[:,4]+Y2[:,5]+Y2[:,6]+Y2[:,7]+Y2[:,8]+4*Y2[:,9]+4*Y2[:,10]+4*Y2[:,11]

rfc2=RandomForestClassifier(n_estimators=500, max_features='log2')
rfc2.fit(X2,Y3)

testY2=rfc2.predict(testX)
#output=['dos1','u2r','r2l','probe','dos2','dos3','dos4','dos5','dos6']
#prdic=testY2[:,0]+2*testY2[:,1]+3*testY2[:,2]+4*testY2[:,3]+testY2[:,4]+testY2[:,5]+testY2[:,6]+testY2[:,7]+testY2[:,8]
flag=testY[:,0]
flag.shape=(606779,1)
testY2.shape=(606779,1)
prdic=testY2*flag

idx=[]
for i in range(606779):
	idx.append(i+1)
idx=numpy.asarray(idx)
idx.shape=(len(idx),1)
idx=numpy.column_stack((idx,prdic))
idx=idx.astype(int)
numpy.savetxt('ans.csv',idx,delimiter=',',fmt='%s')

