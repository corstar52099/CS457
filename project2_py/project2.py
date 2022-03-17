from distutils import command
from genericpath import isfile
import os, shutil
from re import L, sub
import databaseHelper as db

# AUTHOR: Cory Starks
# Date: 02/21/2022
# Class: CS457
# Assignment: Project 1

if __name__ == "__main__":
    print("Welcome to Cory's database tool")
    curDatabase = None

    #make note of the starting directory
    startingDir = os.getcwd()

    #get the command input
    commandString = input()

    #Split up each individual command
    commandArray = commandString.split(";")

    #Main loop
    while (commandArray != 'exit'):

        #Print buffer
        loopCommands = db.databaseHelper()

        #loop by command
        for s in commandArray:

            #Split each individual command by space
            subCommand = s.split(" ")

            #Remove any empty elements in the command
            while ("" in subCommand):
                subCommand.remove("")
            
            #Skip this command if it's empty
            if (len(subCommand) == 0):
                continue

            if (subCommand[0].lower() == 'use'):

                #Use database with subCommand[1] being the database to use
                #and startingDir being the current working directory
                #function will return false if it failed to create database
                if(loopCommands.useDatabase(startingDir, subCommand[1])):

                    #update the current database
                    curDatabase = os.getcwd()

            elif (subCommand[0].lower() == 'create'):
                if (subCommand[1].lower() == 'database'):

                    #Create database with subcommand[2] as the database name
                    #and startingDir as the working directory
                    loopCommands.createDatabase(startingDir, subCommand[2])

                elif (subCommand[1].lower() == 'table'):

                    #Create table with subCommand[2] being the table name and
                    #subCommand[3: len(subCommand)] being the metadata of the table
                    loopCommands.createTable(curDatabase, subCommand[2], subCommand[3: len(subCommand)])
                else:
                    loopCommands.print_buffer.append("%s is not a valid create command" % subCommand[1])
            elif (subCommand[0].lower() == 'drop'):
                if (subCommand[1].lower() == 'table'):

                    #Drop a table with subCommand[2] being the table to drop
                    #and startingDir being the working directory.
                    loopCommands.dropTable(curDatabase, subCommand[2])

                elif (subCommand[1].lower() == 'database'):

                    #Drop a database with subCommand[2] being the database to drop
                    #and startingDir being the working directory
                    loopCommands.dropDatabase(startingDir, subCommand[2])
                else:
                    loopCommands.print_buffer.append("%s is not a valid drop command" % subCommand[1])
            elif (subCommand[0].lower() == 'alter'):
                if(subCommand[1].lower() == 'table'):

                    #Alter a table with subCommand[2] being the table to alter
                    #subCommand[3] being the function (add or delete) and
                    #subCommand[4:6]
                    loopCommands.alterTable(subCommand[2], subCommand[3], ' '.join(subCommand[4:6]))
                else:
                    loopCommands.print_buffer.append("%s is not a valid alter command" % subCommand[1])
            elif (subCommand[0].lower() == 'select'):
                if (subCommand[1].lower() == '*'):
                    if (subCommand[2].lower() == 'from'):

                        #Select from a table with subCommand[3] being the table name
                        #and startingDir being the working directory
                        loopCommands.selectFrom(curDatabase , subCommand[3])
                    else:
                        loopCommands.print_buffer.append("%s is not a valid select * command" % subCommand[1])
                else:
                    loopCommands.print_buffer.append("%s is not a valid select command" % subCommand[1])
            elif (subCommand[0].lower() == 'insert'):
                if (subCommand[1].lower() == 'into'):

                    valueString = ' '.join([str(elem) for elem in subCommand])

                   # values(1, 'Gizmo',       19.99);
                    if (loopCommands.insertIntoSyntax(subCommand[3], subCommand[-1])):
                        values = valueString[valueString.index('(') + 1 : valueString.index(')')].split(',')
                        i = 0
                        for ele in values:
                             values[i] = ele.strip()
                             i += 1
                        loopCommands.insertInto(curDatabase , subCommand[2], values)

                else:
                    loopCommands.print_buffer.append("%s is not a valid insert command" % subCommand[1])
            elif (subCommand[0].lower() == 'exit'):
                exit()
            else:
                loopCommands.print_buffer.append(subCommand[0] + " is not a valid first command.")
            

        #Print the results        
        loopCommands.printBuffer()

        #Read for more input and restart the loop.
        commandString = input()
        commandArray = commandString.split(";")  
    