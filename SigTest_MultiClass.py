# Statistical testing using randomization experiments
# Testing for individual fields
# Written by Son Doan, Oct 2011.
# To compare system 1 to system 2
# Example, to check system1 and system 2 in the input file
# Input file: Index from 0, GOLD standard is index -2
# System 1: Column index in the input file
# System 2: Column index in the input file
# Example, to compare CRF vs Majority systems
# python SigTest_MultiClass.py ./i2b2-major-voting.txt 1 4 output

import os
import sys
import re
import random

# Running time 
R=1000

# Two systems
Sys1 = []
Sys2 = []

#Combination set
Combine = []
path="/export/home/scratch2/doan/coling10/SignificanceTest/src"

# Calculate F-score of system A
def calF(A):
	pid=os.getpid()
	#print pid
	file1=path + "/" + str(pid)
	file2=path + "/" + str(pid) + "_score"
	fout = open(file1,'w')
	for item in A:
		if len(item[2])>0:
			fout.write(item[0] + '\t' + item[3] + '\t' +item[2] + '\n')
		else:
			fout.write('' + '\t' + item[3] + '\t' +item[2] + '\n')
	
	fout.close()
	cmd = path + '/conlleval.pl < ' + file1+ '>' + file2
	os.system(cmd)
	FA = getF(file2)

	# Remove temporary files
	os.remove(file1)
	os.remove(file2)
	return FA

# Parsing output files to get information about performance
# Get information about performance of a system
def getF(file1):
	fin = open(file1)
	# F1 is the array including F1=[All,Dosage,Du,Freq,Med,Mode,Reason]
	F1 = []
	for lines in fin.readlines():	
		#print lines
		if re.search("accuracy",lines):
			line1 = lines.split("FB1: ")
			all = line1[1].strip()
			F1.append(all)
		if re.search("do:",lines):
			line1 = lines.split("FB1: ")
			all = line1[1].strip().split()[0]
			F1.append(all)
		if re.search("du: ",lines):
			line1 = lines.split("FB1: ")
			all = line1[1].strip().split()[0]
			F1.append(all)
		if re.search("f: ",lines):
			line1 = lines.split("FB1: ")
			all = line1[1].strip().split()[0]
			F1.append(all)
		if re.search("m: ",lines):
			line1 = lines.split("FB1: ")
			all = line1[1].strip().split()[0]
			F1.append(all)
		if re.search("mo: ",lines):
			line1 = lines.split("FB1: ")
			all = line1[1].strip().split()[0]
			F1.append(all)
		if re.search("r: ",lines):
			line1 = lines.split("FB1: ")
			all = line1[1].strip().split()[0]
			F1.append(all)
	#print F1
	return F1
	fin.close()	

def loadFile(file, sys1, sys2):
	fin = open(file)
	# Processing in training data first 
	idx = 0
	for line in fin.readlines():
		line1 = line.split('\t')
		# Check only system outputs contain only "B-" or "I-"
		# System 1 is in the first column
		# System 2 is in the second column
		
		#print line1
		Out1 = line1[int(sys1)].strip()	
		Out2 = line1[int(sys2)].strip()	
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

	loadFile(sys.argv[1],sys.argv[2],sys.argv[3])
	fout1 = open(sys.argv[4],'w')

	# Randomization sampling for statistical testing
	# Running for 1000 times, if the difference between two system is greater than diff then they are statistically different
	num = len(Sys1)
	diff = float(calF(Sys1)[0]) - float(calF(Sys2)[0])
	diff_m = float(calF(Sys1)[4]) - float(calF(Sys2)[4])
	diff_mo = float(calF(Sys1)[5]) - float(calF(Sys2)[5])
	diff_do = float(calF(Sys1)[1]) - float(calF(Sys2)[1])
	diff_f = float(calF(Sys1)[3]) - float(calF(Sys2)[3])
	diff_du = float(calF(Sys1)[2]) - float(calF(Sys2)[2])
	diff_r = float(calF(Sys1)[6]) - float(calF(Sys2)[6])
	fout1.write(" ---- debug : different ----- \n")
	fout1.write(str(calF(Sys1))+"\n")
	fout1.write(str(calF(Sys2))+"\n")
	fout1.write(str(calF(Sys1)[0])+"\n")
	fout1.write(str(calF(Sys2)[0])+"\n")
	fout1.write(str(diff)+"\n")
	fout1.write(str(diff_m)+"\n")
	fout1.write("------------------\n")
	# Array count for calculating p-value
	count = {}
	count['sys']=0
	count['med']=0
	count['mod']=0
	count['do']=0
	count['freq']=0
	count['du']=0
	count['re']=0
	for time in range(0,R): 	
		A = random.sample(Combine,num)
		B = set(Combine) - set(A)
		# calculate the difference between two sets
		eval1 = calF(A)
		eval2 = calF(B)
		# Calculate for systems
		diffx = float(eval1[0]) - float(eval2[0])
		diffx_do = float(eval1[1]) - float(eval2[1])
		diffx_du = float(eval1[2]) - float(eval2[2])
		diffx_f = float(eval1[3]) - float(eval2[3])
		diffx_m = float(eval1[4]) - float(eval2[4])
		diffx_mo = float(eval1[5]) - float(eval2[5])
		diffx_r = float(eval1[6]) - float(eval2[6])

		#print diffx
		if abs(diffx) >= abs(diff):
			count['sys'] = count['sys'] + 1
		if abs(diffx_m) >= abs(diff_m):
			count['med']= count['med'] + 1
		if abs(diffx_mo) >= abs(diff_mo):
			count['mod'] = count['mod'] + 1
		if abs(diffx_do) >= abs(diff_do):
			count['do'] = count['do'] + 1
		if abs(diffx_f) >= abs(diff_f):
			count['freq'] = count['freq'] + 1
		if abs(diffx_du) >= abs(diff_du):
			count['du'] = count['du'] + 1
		if abs(diffx_r) >= abs(diff_r):
			count['re'] = count['re'] + 1

		fout1.write('Time: ' + str(time) +  '  Diff: ' + str(diffx) + "\n")

	fout1.write("p-value between two systems \n")

	p_val= float(count['sys'])/float(R)
	p_val_m= float(count['med'])/float(R)
	p_val_mo= float(count['mod'])/float(R)
	p_val_do= float(count['do'])/float(R)
	p_val_f= float(count['freq'])/float(R)
	p_val_du= float(count['du'])/float(R)
	p_val_r= float(count['re'])/float(R)
	
	fout1.write("If the value is less than 0.05 then the difference is significant\n")
	fout1.write("p-value for the whole system : " + str(p_val)+"\n")
	fout1.write("p-value for 		 med: " + str(p_val_m) +"\n")
	fout1.write("p-value for 	 	mode: " + str(p_val_mo) +"\n")
	fout1.write("p-value for 		dose: " + str(p_val_do) + "\n")
	fout1.write("p-value for 		freq: " + str(p_val_f) + "\n")
	fout1.write("p-value for 		  du: " + str(p_val_du) + "\n")
	fout1.write("p-value for 		  re: " + str(p_val_r) + "\n")

	fout1.close()


