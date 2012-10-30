# Add column from 2 files into 1 file
# Run:
# python AddColumn.py <file 1> <file 2> 
# Example:
# python AddColumn.py ../outputs/251CRF.out ../outputs/251SVM.out > CRFvsSVM.out

import os,sys

Hash={}

def readinp(file,pivot):
	index=0
	fin1=open(file)
	for line in fin1.readlines():
		if len(line.strip()) > 0:
			lines = line.strip().split('\t')
			line1='\t'.join(lines[0:-1])
			Hash[(index,pivot)]=(line1,lines[-1])
			#Hash[(index,pivot)]=(lines[-2],lines[0])
		else:
			lines = line.split('\t')
			line1='\t'.join(lines[0:-1])
			Hash[(index,pivot)]=(line1,lines[-1].strip())
			
		index = index + 1
	fin1.close()

def main():

	readinp(sys.argv[1],'0')
	readinp(sys.argv[2],'1')

	len1= len(Hash)/2
	for i in range(0,len1):
		print Hash[(i,'0')][1] + '\t' + Hash[(i,'1')][0] + '\t' + Hash[(i,'1')][1]

if __name__=="__main__":
	main()

