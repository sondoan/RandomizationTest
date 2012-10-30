#!/bin/bash

# Calculate parallel for significant test
# Simply run in bash shell

PYTHON=/usr/bin/python
SRC=/export/home/scratch2/doan/coling10/SignificanceTest

#qsub -S $PYTHON $SRC/src/SigTest_MultiClass.py $SRC/outputs/i2b2-major-voting.txt 0 2 $SRC/results/RulevsSVM.out
#qsub -S $PYTHON $SRC/src/SigTest_MultiClass.py $SRC/outputs/i2b2-major-voting.txt 0 1 $SRC/results/RulevsCRF.out
#qsub -S $PYTHON $SRC/src/SigTest_MultiClass.py $SRC/outputs/i2b2-major-voting.txt 1 2 $SRC/results/CRFvsSVM.out
#qsub -S $PYTHON $SRC/src/SigTest_MultiClass.py $SRC/outputs/i2b2-major-voting.txt 0 4 $SRC/results/RulevsMajority.out
#qsub -S $PYTHON $SRC/src/SigTest_MultiClass.py $SRC/outputs/i2b2-major-voting.txt 1 4 $SRC/results/CRFvsMajority.out
#qsub -S $PYTHON $SRC/src/SigTest_MultiClass.py $SRC/outputs/i2b2-major-voting.txt 2 4 $SRC/results/SVMvsMajority.out

#qsub -S $PYTHON $SRC/src/SigTest_MultiClass.py $SRC/outputs/i2b2-CRF-base-voting.txt 0 3 $SRC/results/CRFvsCRF-based.out
#qsub -S $PYTHON $SRC/src/SigTest_MultiClass.py $SRC/outputs/i2b2-CRF-base-voting.txt 1 3 $SRC/results/SVMvsCRF-based.out

#qsub -S $PYTHON $SRC/src/SigTest_MultiClass.py $SRC/outputs/i2b2-CRF-base-voting.txt 0 3 $SRC/results/CRFvsSVM-based.out
#qsub -S $PYTHON $SRC/src/SigTest_MultiClass.py $SRC/outputs/i2b2-CRF-base-voting.txt 1 3 $SRC/results/SVMvsSVM-based.out

#qsub -S $PYTHON $SRC/src/SigTest_MultiClass.py $SRC/outputs/i2b2-majorvsCRF-basedvsSVM-based.txt 0 3 $SRC/results/MajorityvsSVM-based.out
#qsub -S $PYTHON $SRC/src/SigTest_MultiClass.py $SRC/outputs/i2b2-majorvsCRF-basedvsSVM-based.txt 1 3 $SRC/results/CRF-basedvsSVM-based.out
#qsub -S $PYTHON $SRC/src/SigTest_MultiClass.py $SRC/outputs/i2b2-majorvsCRF-basedvsSVM-based.txt 0 1 $SRC/results/MajorityvsCRF-based.out

#qsub -S $PYTHON $SRC/src/SigTest_MultiClass.py $SRC/outputs/i2b2-RulevsCRF-basedvsSVM-based.txt 0 3 $SRC/results/RulevsSVM-based.out
#qsub -S $PYTHON $SRC/src/SigTest_MultiClass.py $SRC/outputs/i2b2-RulevsCRF-basedvsSVM-based.txt 0 1 $SRC/results/RulevsCRF-based.out

# Compared Sydney system
qsub -S $PYTHON $SRC/src/SigTest_MultiClass.py $SRC/outputs/SydneyvsSVM-basedvsCRF-basedvsMajorvsMedExvsCRFvsSVM.txt 0 1 $SRC/results/SydneyvsSVM-based.out
qsub -S $PYTHON $SRC/src/SigTest_MultiClass.py $SRC/outputs/SydneyvsSVM-basedvsCRF-basedvsMajorvsMedExvsCRFvsSVM.txt 0 2 $SRC/results/SydneyvsCRF-based.out
qsub -S $PYTHON $SRC/src/SigTest_MultiClass.py $SRC/outputs/SydneyvsSVM-basedvsCRF-basedvsMajorvsMedExvsCRFvsSVM.txt 0 3 $SRC/results/SydneyvsMajority.out
qsub -S $PYTHON $SRC/src/SigTest_MultiClass.py $SRC/outputs/SydneyvsSVM-basedvsCRF-basedvsMajorvsMedExvsCRFvsSVM.txt 0 4 $SRC/results/SydneyvsMedEx.out
qsub -S $PYTHON $SRC/src/SigTest_MultiClass.py $SRC/outputs/SydneyvsSVM-basedvsCRF-basedvsMajorvsMedExvsCRFvsSVM.txt 0 5 $SRC/results/SydneyvsCRF.out
qsub -S $PYTHON $SRC/src/SigTest_MultiClass.py $SRC/outputs/SydneyvsSVM-basedvsCRF-basedvsMajorvsMedExvsCRFvsSVM.txt 0 8 $SRC/results/SydneyvsSVM.out

#### For 10 fold results

#qsub -S $PYTHON $SRC/src/SigTest_MultiClass.py $SRC/10fold/test.out-POS-prefix-suffixtagger-AllSem1AllSem1-new4-Post2-DRT-Vote3-Majority 0 1 $SRC/10fold-results/RulevsCRF.out
#qsub -S $PYTHON $SRC/src/SigTest_MultiClass.py $SRC/10fold/test.out-POS-prefix-suffixtagger-AllSem1AllSem1-new4-Post2-DRT-Vote3-Majority 0 2 $SRC/10fold-results/RulevsSVM.out
#qsub -S $PYTHON $SRC/src/SigTest_MultiClass.py $SRC/10fold/test.out-POS-prefix-suffixtagger-AllSem1AllSem1-new4-Post2-DRT-Vote3-Majority 0 4 $SRC/10fold-results/RulevsMajority.out
#qsub -S $PYTHON $SRC/src/SigTest_MultiClass.py $SRC/10fold/test.out-POS-prefix-suffixtagger-AllSem1AllSem1-new4-Post2-DRT-Vote3-Majority 1 2 $SRC/10fold-results/CRFvsSVM.out
#qsub -S $PYTHON $SRC/src/SigTest_MultiClass.py $SRC/10fold/test.out-POS-prefix-suffixtagger-AllSem1AllSem1-new4-Post2-DRT-Vote3-Majority 1 4 $SRC/10fold-results/CRFvsMajority.out
#qsub -S $PYTHON $SRC/src/SigTest_MultiClass.py $SRC/10fold/test.out-POS-prefix-suffixtagger-AllSem1AllSem1-new4-Post2-DRT-Vote3-Majority 2 4 $SRC/10fold-results/SVMvsMajority.out

#qsub -S $PYTHON $SRC/src/SigTest_MultiClass.py $SRC/10fold/test.out-POS-prefix-suffixtagger-AllSem1AllSem1-new4-Post2-DRT-Vote3-CRF 1 3 $SRC/10fold-results/SVMvsCRF-based.out
#qsub -S $PYTHON $SRC/src/SigTest_MultiClass.py $SRC/10fold/test.out-POS-prefix-suffixtagger-AllSem1AllSem1-new4-Post2-DRT-Vote3-CRF 0 3 $SRC/10fold-results/CRFvsCRF-based.out
#qsub -S $PYTHON $SRC/src/SigTest_MultiClass.py $SRC/10fold/test.out-POS-prefix-suffixtagger-AllSem1AllSem1-new4-Post2-DRT-Vote3-SVM 0 3 $SRC/10fold-results/CRFvsSVM-based.out
#qsub -S $PYTHON $SRC/src/SigTest_MultiClass.py $SRC/10fold/test.out-POS-prefix-suffixtagger-AllSem1AllSem1-new4-Post2-DRT-Vote3-SVM 1 3 $SRC/10fold-results/SVMvsSVM-based.out

#qsub -S $PYTHON $SRC/src/SigTest_MultiClass.py $SRC/10fold/test.out-POS-prefix-suffixtagger-AllSem1AllSem1-new4-Post2-DRT-Vote3-MajorityVSCRF-basedVSSVM-based 0 1 $SRC/10fold-results/MajorityVSCRF-based.out
#qsub -S $PYTHON $SRC/src/SigTest_MultiClass.py $SRC/10fold/test.out-POS-prefix-suffixtagger-AllSem1AllSem1-new4-Post2-DRT-Vote3-MajorityVSCRF-basedVSSVM-based 0 3 $SRC/10fold-results/MajorityVSSVM-based.out
#qsub -S $PYTHON $SRC/src/SigTest_MultiClass.py $SRC/10fold/test.out-POS-prefix-suffixtagger-AllSem1AllSem1-new4-Post2-DRT-Vote3-MajorityVSCRF-basedVSSVM-based 1 3 $SRC/10fold-results/CRF-basedVSSVM-based.out

#qsub -S $PYTHON $SRC/src/SigTest_MultiClass.py $SRC/10fold/test.out-POS-prefix-suffixtagger-AllSem1AllSem1-new4-Post2-DRT-Vote3-RuleVSCRF-basedVSSVM-based 0 1 $SRC/10fold-results/RuleVSCRF-based.out
#qsub -S $PYTHON $SRC/src/SigTest_MultiClass.py $SRC/10fold/test.out-POS-prefix-suffixtagger-AllSem1AllSem1-new4-Post2-DRT-Vote3-RuleVSCRF-basedVSSVM-based 0 3 $SRC/10fold-results/RuleVSSVM-based.out


