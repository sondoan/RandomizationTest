# Statistical testing using randomization experiments
# Written by Son Doan, Oct 2011.
# Given 2 outputs
# To compare system 1 to system 2
# Example, to check system1 at column 1 and system 2 at column 2 in the file test1.out
# python SigTest.py test1.out 

import os
import sys
import re
import random

# Two systems
Sys1 = []
Sys2 = []

#Combination set
Combine = []

# Calculate F-score of system A
def calF(A):
	fout = open('./tmp','w')
	for item in A:
		if len(item[2])>0:
			fout.write(item[0] + '\t' + item[3] + '\t' +item[2] + '\n')
		else:
			fout.write('' + '\t' + item[3] + '\t' +item[2] + '\n')
	
	fout.close()
	cmd = './conlleval.pl < ./tmp > ./tmp-score'
	os.system(cmd)
	FA = getF("./tmp-score")
	return FA

# Parsing output files to get information about performance
# Get information about performance of a system
def getF(file1):
	fin = open(file1)
	F1 = ''
	for lines in fin.readlines():	
		if re.search("accuracy",lines):
			line1 = lines.split("FB1: ")
			F1 = line1[1].strip()
			break
	return float(F1)
	fin.close()	

def loadFile(file):
	fin = open(file)
	# Processing in training data first 
	idx = 0
	for line in fin.readlines():
		line1 = line.split('\t')
		# Check only system outputs contain only "B-" or "I-"
		# System 1 is in the first column
		# System 2 is in the second column
		
		Out1 = line1[-1].strip()	
		Out2 = line1[1]	
		# ---------------------------------------
		# Add only if there are B- or I- on predictions
		#line2 = line1[2] + line1[1]
		#if line2 !='OO' and len(line2.strip())>0:
		#print line2
		# ---------------------------------------
		#line2 = line1[2] + line1[1]

		Sys1.append(("1",idx,Out1,line1[-2]))
		Sys2.append(("2",idx,Out2,line1[-2]))

		Combine.append(("1",idx,Out1,line1[-2]))
		Combine.append(("2",idx,Out2,line1[-2]))
		idx = idx + 1

	#print idx
    	fin.close

if __name__=="__main__":
	loadFile(sys.argv[1])
	diff = calF(Sys1) - calF(Sys2)
	# Randomization sampling for statistical testing
	# Running for 1000 times, if the difference between two system is greater than diff then they are statistically different
	num = len(Sys1)
	k = 0
	print "------------------"
	print calF(Sys1)
	print calF(Sys2)
	print diff
	print "------------------"
	for time in range(0,1000): 	
		A = random.sample(Combine,num)
		B = set(Combine) - set(A)
		# calculate the difference between two sets
		eval1 = calF(A)
		eval2 = calF(B)
		diffx = eval1 - eval2
		#print diffx
		if abs(diffx) >= abs(diff):
			k = k + 1
		if k==50:
			print "Not statistically!"
			sys.exit()
		print 'Time: ' + str(time) +  '  Diff: ' + str(diffx) 
	print "Statistically!"	

