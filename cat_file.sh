#!/bin/sh

# Concatenate files into a single one
SRC=/home/doan/scratch2/doan/coling10/coling10/program/CV-CV10
DESC=/home/doan/scratch2/doan/coling10/SignificanceTest/10fold

for i in `ls $SRC/fold1/|grep test.out-POS-prefix-suffixtagger-AllSem1`
do
	#echo $i	
	cat $SRC/fold*/$i > $DESC/$i
done

