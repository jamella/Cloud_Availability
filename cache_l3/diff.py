#!/usr/bin/python
# File Name: diff.py

"""
	This file is used to process the data from two different files
"""

import os
import string
import sys

def process():
	data1 = open('original_assoc_num', 'r')
	activities1 = data1.readlines()
	data1.close()

	data2 = open('interfere_assoc_num', 'r')
	activities2 = data2.readlines()
	data2.close()

	data3 = open('diff_assoc_num', 'w')

	for i in range(2048):
		first0 = int(activities1[i].split(' ')[0])
		second0 = int(activities2[i].split(' ')[0])
		diff0 = first0 - second0
		first1 = int(activities1[i].split(' ')[1])
		second1 = int(activities2[i].split(' ')[1])
		diff1 = first1 - second1
		first2 = int(activities1[i].split(' ')[2])
		second2 = int(activities2[i].split(' ')[2])
		diff2 = first2 - second2
		first3 = int(activities1[i].split(' ')[3])
		second3 = int(activities2[i].split(' ')[3])
		diff3 = first3 - second3
		first4 = int(activities1[i].split(' ')[4])
		second4 = int(activities2[i].split(' ')[4])
		diff4 = first4 - second4
		first5 = int(activities1[i].split(' ')[5])
		second5 = int(activities2[i].split(' ')[5])
		diff5 = first5 - second5
		
		data3.write("%d %d %d %d %d %d\n" % (diff0, diff1, diff2, diff3, diff4, diff5))
	data3.close()

process()
