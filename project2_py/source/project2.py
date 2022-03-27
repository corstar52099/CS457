from genericpath import isfile
import os, shutil
from re import L, sub
from source import databaseHelper as db

# AUTHOR: Cory Starks
# Date: 03/26/2022
# Class: CS457
# Assignment: Project 2
def project2Script(inp = None):
    try:
            #print("Welcome to Cory's database tool")
            curDatabase = None
        
            #make note of the starting directory
            startingDir = os.getcwd()
    
            #get the command input from user
            if (inp == None):
                print("Welcome to Cory's database tool")
                commandString = input()
                commandArray = commandString.split(";")

            #Input from run script
            else:

                #Input from run script
                commandArray = inp
                i = 0

                for ele in commandArray:

                    #replace all new lines in command with spaces
                    if (i + 1 == len(commandArray)):
                        commandArray[i] = ele.replace("\n", "")
                        commandArray[i] = ele.replace(";", "")
                        break
                    commandArray[i] = ele.replace("\n", "")

                    #Remove the '#' if you would like to see the list of commands passed and how they are parsed
                    #print("COMMAND: %s" % commandArray[i])
                    i += 1
    
            #Split up each individual command
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
                if (len(subCommand) < 2):
                    continue
                #print(subCommand[0].lower())
                if (subCommand[0].lower() == 'use'):
                    #Use database with subCommand[1] being the database to use
                    #and startingDir being the current working directory
                    #function will return false if it failed to create database
                    if(loopCommands.useDatabase(startingDir, subCommand[1])):
                        #update the current database
                        curDatabase = os.getcwd()
                    else:
                        loopCommands.print_buffer.append("Failed to useDatabase because of a command issue")

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
                    
                    #Select from a table
                    loopCommands.selectFromMetaData(curDatabase, subCommand[1 : len(subCommand)])
                        
                elif (subCommand[0].lower() == 'insert'):
                    if (subCommand[1].lower() == 'into'):

                        #insert into table with valueString being the combintation of commands given
                        #and values being all of the data that is planned to be inserted.
                        #subCommand[2] is the table name and curDatabase is current database
                        valueString = ' '.join([str(elem) for elem in subCommand])
                        if (loopCommands.insertIntoSyntax(subCommand[3], subCommand[-1])):
                            values = valueString[valueString.index('(') + 1 : valueString.index(')')].split(',')
                            i = 0
                            for ele in values:
                                 values[i] = ele.strip()
                                 i += 1
                            loopCommands.insertInto(curDatabase , subCommand[2], values)
                    else:
                        loopCommands.print_buffer.append("%s is not a valid insert command" % subCommand[1])

                elif (subCommand[0].lower() == 'update'):
                    if (subCommand[2].lower() == 'set'):

                        #update table by changing the value of some element
                        #subCommand[1] is the table name
                        #subCommand[2 : len(subCommand)] is the command that follows the table name
                        loopCommands.updateTable(curDatabase, subCommand[1], subCommand[2 : len(subCommand)])

                elif (subCommand[0].lower() == 'delete'):
                    if (subCommand[1].lower() == 'from'):

                        #Delete a specified element from a table 
                        #subCommand[2] is the table name to delete from
                        #subCommand[3: len(subCommand)] is the rest of the command after table name
                        loopCommands.deleteFromTable(curDatabase, subCommand[2], subCommand[3: len(subCommand)])

                    else:
                        loopCommands.print_buffer.append(subCommand[1] + " is not a valid delete command")
                elif (subCommand[0].lower() == '.exit'):
                    exit()
                else:
                    loopCommands.print_buffer.append(subCommand[0] + " is not a valid first command.")
        
            #Print the results        
            loopCommands.printBuffer()
    except Exception as e:
        print('.exit %s' % e)