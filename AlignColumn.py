# Align classifier for comparison purpose
# Run:
# python AlignColumn.py ../outputs/i2b2-major-voting.txt ../outputs/i2b2-CRF-base-voting.txt ../outputs/i2b2-SVM-base-voting.txt > ../outputs/i2b2-majorvsCRF-basedvsSVM-based.txt

import os,sys

Hash={}

def readinp(file,pivot):
	index=0
	fin1=open(file)
	for line in fin1.readlines():
		if len(line.strip()) > 0:
			lines = line.strip().split('\t')
			#Hash[(index,pivot)]=(lines[-2],lines[-1])
			Hash[(index,pivot)]=(lines[-2],lines[0])
		else:
			Hash[(index,pivot)]=('','')
			
		index = index + 1
	fin1.close()

def main():

	readinp(sys.argv[1],'0')
	readinp(sys.argv[2],'1')
	readinp(sys.argv[3],'2')

	len1= len(Hash)/3
	for i in range(0,len1):
		print Hash[(i,'0')][1] + '\t' + Hash[(i,'1')][1] + '\t' + Hash[(i,'2')][0]+ '\t' + Hash[(i,'2')][1]


if __name__=="__main__":
	main()

