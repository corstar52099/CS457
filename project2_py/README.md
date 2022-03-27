#CS457 Project 2

##Execution instructions
This code uses a driver script 'run.py' contained in the main directory

This driver code can accept parameters

Usage:

~>python3 run.py param {Optional}

Parameters:
	There are three possible parameters:
	-None: Passing no parameters will allow the program to execute and accept input from command line
	-Test: This parameter will use the sql like test script found in the Scripts folder
	-c: This parameter expects custom sql like scripts to be fed to the driver.
		This parameter requires the use of the optional paramerter which will take the form of a script name that
		the user will place in the Scripts folder.
##Directories
There are two directories to be concerned with. Scripts and source
Scripts will contain sql like .txt scripts that will be fed to the driver to execute the program
source contains source code that will run the program