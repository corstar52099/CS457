import sys
import os
import subprocess
from source import project2

# AUTHOR: Cory Starks
# Date: 03/26/2022
# Class: CS457
# Assignment: Project 2


arg_list = sys.argv

if (len(arg_list) == 1):
	project2.project2Script()
elif (arg_list [1] == 'test'):
	try:
		with open("./Scripts/testScript.txt") as f:
			testStr = f.read()
			testArr = testStr.split(";\n")
		print("Running testScript.txt\n------OUTPUT------")
		project2.project2Script(testArr)
	except Exception as e:
		print("Run test script has failed becasue of %s" % e)
elif (arg_list[1] == 'c'):
	try:
		with open("./Scripts/%s" % arg_list[2]) as f:
			customStr = f.read()
			customArr = testStr.split(";\n")
		print("Running %s\n------OUTPUT------" % arg_list[2])
		project2.project2Script(customArr)
	except Exception as e:
		print("Run custom script has failed becasue of %e")
		print("Usage ~python3 run.py (test|c) (|yourScript.txt)")
else:
	print("Usage ~python3 run.py (test|c) (|yourScript.txt)")