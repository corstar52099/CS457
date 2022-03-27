from mailbox import linesep
from operator import mod, ne, truediv
import os, shutil
from genericpath import isfile

# AUTHOR: Cory Starks
# Date: 03/26/2022
# Class: CS457
# Assignment: Project 2

#CLASS: databaseHelper
#This class functions as a helper for project2.py.
#The class contains functions that are meant to run in a singular instance
class databaseHelper:

    print_buffer = []

    def __init__(self) -> None:

        self.print_buffer = []

    #alter a table
    # @param filename: the name of the file to open
    # @param fun: the type of function (add or delete)
    # @param thingChanging: the individual metadata changing
    def alterTable(self, table, fun, thingChanging):
        contents = []
        try:
            if (fun.lower() == 'add'):
                with open(table + ".txt", 'a') as f:
                    f.write("|" + thingChanging)
                self.print_buffer.append("Table %s modified." % table)
            elif (fun.lower() == 'delete'):
                with open(table + ".txt", 'r') as f:
                    oldContents = f.read()
                    contents = oldContents.split("|")
                contents.remove(thingChanging)
                with open(table + ".txt", 'w') as f:
                    i = 0
                    for s in (contents):
                        if (i + 1 == len(contents)):
                            f.write(s)
                            break
                        f.write(s + '|')
                        i += 1
                self.print_buffer.append("Table %s modified." % table)
        except Exception as e:
            self.print_buffer.append("Failed to alter table becasue of %s." % e)

    #make a table and fill it with content
    # @param filename: the name of the file to open
    # @param contents: the list of metadata to insert into the table
    def makeAndFillTable(self, filename, contents):
        with open(filename + ".txt", 'w') as f:
            i = 0
            for s in contents:
                s = s.strip()
                if (i + 1 == len(contents)):
                    f.write(s)
                    break
                f.write(s + " | ")
                i += 1

    #remove outter parenthesis from a metadata
    # @param metaData: metaData that requires parenthesis to be removed
    # e.g. "(varchar(20))" -> "varchar(20)"
    def removeOuterParentheses(self, metaData):
            stack = []
            res=""
            for s in metaData:
                if (s == '('):
                    stack.append(s)
                    if (len(stack) > 1):
                        res+=s
                    continue
                elif (s == ')'):
                    stack.pop()
                    if (len(stack) == 0):
                        break
                    res+=s
                else:
                    res+=s
            return res

    #Change the current database to specified database
    # @param startingDir: the starting directory to look for the database in
    # @param databaseToUse: the database to use
    def useDatabase(self, startingDir, databaseToUse):
        try:
            os.chdir(startingDir + '/' + databaseToUse)
            self.print_buffer.append("Using database " + databaseToUse)
            return True
        except Exception as e:
            self.print_buffer.append("Could not use database %s becasue of %s." % (databaseToUse, e))
            return False

    #create a table in a specefied database
    # @param curDatabase: the name of the file to open
    # @param tableName the list of metadata to insert into the table
    def createTable(self, curDatabase, tableName, metaData):
        if(curDatabase == None):
            self.print_buffer.append("Failed to create table %s becasue there is no database being used." % tableName)
            return
        elif (isfile(curDatabase + "/" + tableName + ".txt")):
            self.print_buffer.append("Failed to create table %s becasue it already exists." % tableName)
            return
        tableCon = ' '.join(metaData)
        tableCon  = self.removeOuterParentheses(tableCon)
        tableStr = ''.join(tableCon)
        tableStr = tableStr.split(",")
        try: 
            self.makeAndFillTable(tableName, tableStr)
            self.print_buffer.append("Table %s created." % tableName)
        except Exception as e:
            self.print_buffer.append("Failed to create table %s becasue of %s." % (tableName, e))

    #create a database in the current working directory
    # @param startingDir: The name of the starting directory 
    # @param databaseName: The name of the database to create
    def createDatabase(self, startingDir, databaseName):
        try:
            os.mkdir(startingDir + "/" +databaseName)
            self.print_buffer.append("Database " + databaseName + " created.")
        except Exception as e:
            self.print_buffer.append("Failed to create database %s becasuse %s" % (databaseName, e))

    #delete a table in the current database
    # @param startingDir: The name of the starting directory 
    # @param tableToDrop: The name of the table to delete
    def dropTable(self, curDatabase, tableToDrop):
        try:
            os.remove(curDatabase + "/" + tableToDrop + ".txt")
            self.print_buffer.append("Table %s deleted." % tableToDrop)
        except Exception as e:
            self.print_buffer.append("Failed to delete table %s becasue of %s" % (tableToDrop, e))

    #delete a database in from the current working directory
    # @param startingDir: The name of the starting directory 
    # @param databaseToDrop: The name of the database being deleted
    def dropDatabase(self, startingDir, databaseToDrop):
        try:
            #we must delete all of the files within the database first
            #because os doesnt allow us to delete a folder that contains files
            for filename in os.listdir(startingDir + '/' + databaseToDrop):
                file_path = os.path.join(startingDir + '/' + databaseToDrop, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                self.print_buffer.append('Failed to delete database %s becasue %s' % (databaseToDrop, e))
                os.rmdir(startingDir + '/' + databaseToDrop)
                self.print_buffer.append("Database %s deleted." % databaseToDrop)
        except Exception as e:
            self.print_buffer.append('Failed to delete database %s becasue %s' % (databaseToDrop, e))

    #select specific criteria from the database
    # @param  curDatabase: The name of the current database
    # @param command: A string containing contents of the command that 
    #                   will use this function. The function will parse
    #                   this command and determine what to do with it
    def selectFromMetaData(self, curDatabase, command):

        attributeArr = []
        tableName = ""

        i = 0

        #Select all condition
        if command[0] == '*':
            try:
                with open(curDatabase + "/" + command[2] + ".txt", 'r') as f:
                    self.print_buffer.append(f.read())
                return
            except Exception as e:
                self.print_buffer.append("Failed to select from table becasue of %s" % e)

        #Select criteria condition
        for s in command:
            if (s.lower() == "from"):
                tableName = command[i + 1]
                i += 2
                break
            s = s.strip(',')
            attributeArr.append(s)
            i += 1
        if (command[i] == "where"):
            attribute = command[i + 1]
            comparison = command[i + 2]
            attValue = command[i + 3]
            with open ("%s/%s.txt" % (curDatabase, tableName)) as f:
                temp = f.read()
            metaData = temp[0 : temp.index("\n")].split(" | ")

            #create array of acceptable metadata and indecies
            acceptMetadata = []
            Indecies = []
            attIndex = 0
            k = 0
            for ele in metaData:
                meta = ele.split(" ")
                if (meta[0] == attribute):
                    attIndex = k
                    attType = meta[1]
                if (meta[0] in attributeArr):
                    acceptMetadata.append(ele)
                    Indecies.append(k)
                k += 1

            #create the output table and add the acceptable metadata to the top
            outputArr = []
            j = 0
            for line in temp.split("\n"):
                if (j == 0):
                    outputArr.append(' | '.join(acceptMetadata))
                    j += 1
                    continue
                data = line.split(' | ')
                stringBuilder = []

                #convert the types before making comparisons
                if (attType == 'float'):
                            data[attIndex] = float(data[attIndex])
                            attValue = float(attValue)
                elif (attType == 'int'):
                    data[attIndex] = int(data[attIndex]) 
                    attValue = int(attValue)

                #Generate output based on the type of comparison being made
                if (comparison == '!='):
                    if (data[attIndex] != attValue):
                        for index in Indecies:
                            stringBuilder.append(data[index])
                        outputArr.append(' | '.join(stringBuilder))
                        continue
                elif (comparison == '='):
                    if (data[attIndex] == attValue):
                        for index in Indecies:
                            stringBuilder.append(data[index])
                        outputArr.append(' | '.join(stringBuilder))
                        continue
                elif (comparison == '<'):
                    if (data[attIndex] < attValue):
                        for index in Indecies:
                            stringBuilder.append(data[index])
                        outputArr.append(' | '.join(stringBuilder))
                        continue
                elif (comparison == '>'):
                    if (data[attIndex] > attValue):
                        for index in Indecies:
                            stringBuilder.append(data[index])
                        outputArr.append(' | '.join(stringBuilder))
                        continue
                elif (comparison == '<='):
                    if (data[attIndex] <= attValue):
                        for index in Indecies:
                            stringBuilder.append(data[index])
                        outputArr.append(' | '.join(stringBuilder))
                        continue
                elif (comparison == '>='):
                    if (data[attIndex] >= attValue):
                        for index in Indecies:
                            stringBuilder.append(data[index])
                        outputArr.append(' | '.join(stringBuilder))
                        continue
                j += 1
            for ele in outputArr:
                self.print_buffer.append(ele)

    #print the current print buffer which will contain contents
    #that are collected from the commands executed in this object
    def printBuffer(self):
        for s in self.print_buffer:
            print(s)

    #insert specific data into a table
    # @param curDatabase: The name of the current database.
    # @param table: The name of the table to insert into
    # @param data: The specific data that will be inserted into the table
    def insertInto(self, curDatabase, table, data):
        if (self.checkValidDataEntry(curDatabase, table, data)):
            with open(curDatabase + "/%s.txt" % table, 'a') as f:
                f.write('\n' + ' | '.join(data))
                self.print_buffer.append("1 new record inserted.")
        else:
            self.print_buffer.append("Falied to insert table %s becasue data is invalid." % table)

    #A boolean type function that checks for valid syntax of inserting
    # @param stringToCheck: The string that needs to be validated.
    # @param lastString: The final string of the insert command.
    def insertIntoSyntax(self, stringToCheck, lastString):
        substring = "values("
        if( stringToCheck != None and substring in stringToCheck):
            for c in lastString:
                if (c == ')'):
                    return True
        else:
            return False
    
    #A boolean type function that checks if data is valid and can be inserted into table
    # @param curDatabase: The name of the current database.
    # @param table: The name of the table that is used for validation of data
    # @param data: The data that is attepting to be inserted
    def checkValidDataEntry(self, curDatabase, table, data):
        try:
            with open("%s/%s.txt" % (curDatabase, table), 'r') as f:
                tmp = f.read()
                try:
                    line = tmp[ 0 : tmp.index('\n') ].split(' | ')
                except:
                    line = tmp.split(' | ')
                i = 0
                for ele in line:
                    temp = ele.split(' ')
                    if (temp[1].lower() == "int" and data[i].isnumeric()):    
                        i += 1                  
                        continue
                    elif ("varchar(" in temp[1].lower()):
                        i += 1
                        continue
                    elif (temp[1].lower() == "float" and float(data[i]) and '.' in data[i]):
                        i += 1
                        continue
                    else:
                        return False                   
                return True
        except Exception as e:
            self.print_buffer.append("An error has occured becasue of %s" % e)

    #Check if attribute and the corresponding data is valid
    # @param curDatabase: the current working database
    # @param table: the table in question
    # @param attributeName: a list contianing the attribute name and data
    def containsData(self, curDatabase, table, attributeData):
        try:
            with open("%s/%s.txt" % (curDatabase, table)) as f:
                temp = f.read()
            metaData = temp[0 : temp.index("\n")].split(" | ")
            index = 0
            for ele in metaData:
                splitData = ele.split(" ")
                if (splitData[0] == attributeData[0]):
                    break
                index += 1
            with open("%s/%s.txt" % (curDatabase, table)) as f:
                j = 0
                temp2 = f.read()
                for line in temp2.split("\n"):
                    if (j == 0):
                        j += 1
                        continue
                    data = line.split(" | ")
                    if (data[index] == attributeData[1]):
                        return True
            return False
        except:
            return False

    #update table with specific criteria
    # @param curDatabase: The name of the current database
    # @param table: The table being updated
    # @param command: The string of the command that will be parsed by
    #                   this function to determine what sort of update to make
    def updateTable(self, curDatabase, table, command):
        try:
            if (self.checkValidUpdate(curDatabase, table, command)):
                modifications = 0
                setVal = command[3]
                whereVal = command[7]
                newTableContents = []

                with open("%s/%s.txt" %(curDatabase, table), "r") as f:
                    i = 0
                    setIndex = 0
                    whereIndex = 0
                    for line in f.read().split("\n"):
                        if (i == 0):
                            lineArr = line.split(" | ")

                            #get the index of the set Attribute
                            for ele in lineArr:
                                temp = ele.split(" ")
                                if (temp[0]  == command[1]):
                                    break
                                setIndex += 1

                            #get the index of the where Attribute
                            for ele in lineArr:
                                temp = ele.split(" ")
                                if (temp[0]  == command[5]):
                                    break
                                whereIndex += 1

                            newTableContents.append(line)
                            i += 1
                            continue
                        lineArr = line.split(" | ")
                        if (lineArr[whereIndex] == whereVal):
                            modifications += 1
                            lineArr[setIndex] = setVal
                            newLine = ' | '.join(lineArr)
                            newTableContents.append(newLine)
                            continue
                        newTableContents.append(line)
                self.writeTable(curDatabase, table, newTableContents)
                if (modifications == 1):
                    self.print_buffer.append("1 record modified.")
                else:
                    self.print_buffer.append("%s record modified." % modifications)
        except:
            self.print_buffer.append("Failed to update %s becasue of invalid update." % table)

    #Overwrite a table with the information given in lineArr
    #NOTE: this function should always work because lineArr
    #           is expected to be valid
    # @param curDatabase: The name of the current database
    # @param table: The name of the table being overwriten
    # @param lineArr: Data being written into the table
    def writeTable(self, curDatabase, table, lineArr):
        with open("%s/%s.txt" % (curDatabase, table), "w") as f:
            i = 0
            for ele in lineArr:
                if (i + 1 == len(lineArr)): 
                    f.write(ele)
                    break
                f.write(ele + "\n")
                i += 1

    #Delete certain data from table with given criteria
    # @param curDatabase: The name of the current database
    # @param table: The name of the table being updated
    # @param command: The string of content given by the command
    #                       that will determine what happens.
    def deleteFromTable(self, curDatabase, table, command):
        try:
            if (self.checkValidDelete(curDatabase, table, command)):

                #Assign and get variables from command
                modifications = 0
                comparison = command[2]
                whereAttribute = command[1]
                whereVal = command[3]
                newTableContents = []
                whereType = ""       
                with open("%s/%s.txt" %(curDatabase, table), "r") as f:
                    i = 0
                    whereIndex = 0
                    for line in f.read().split("\n"):
                        if (i == 0):
                            lineArr = line.split(" | ")     
                            #get the index of the where Attribute
                            for ele in lineArr:
                                temp = ele.split(" ")
                                if (temp[0]  == whereAttribute):
                                    whereType = temp[1]
                                    break
                                whereIndex += 1     
                            newTableContents.append(line)
                            i += 1
                            continue
                        lineArr = line.split(" | ")

                        #convert the typed based on the type being sought
                        if (whereType == 'float'):
                            lineArr[whereIndex] = float(lineArr[whereIndex])
                            whereVal = float(whereVal)
                        elif (whereType == 'int'):
                            lineArr[whereIndex] = int(lineArr[whereIndex]) 
                            whereVal = int(whereVal)

                        #make the modification basxed on the given comparison
                        if(comparison == "="):
                            if (lineArr[whereIndex] == whereVal):
                                modifications += 1
                                continue
                        if(comparison == "<"):
                            if (lineArr[whereIndex] < whereVal):
                                modifications += 1
                                continue
                        if(comparison == ">"):
                            if (lineArr[whereIndex] > whereVal):
                                modifications += 1
                                continue
                        if(comparison == ">="):
                            if (lineArr[whereIndex] >= whereVal):
                                modifications += 1
                                continue
                        if(comparison == "<="):
                            if (lineArr[whereIndex] <= whereVal):
                                modifications += 1
                                continue
                        if(comparison == "!="):
                            if (lineArr[whereIndex] != whereVal):
                                modifications += 1
                                continue
                        newTableContents.append(line)
                self.writeTable(curDatabase, table, newTableContents)
                if (modifications == 1):
                    self.print_buffer.append("1 record deleted.")
                else:
                    self.print_buffer.append("%s records deleted" % modifications)
            else:
                self.print_buffer.append("Failed to delete from %s because of invalid data input" % table)
        except Exception as e:
            self.print_buffer.append("Failed to delete from table because of %s" % e)

    #Check that the delete command being attempted is valid
    # @param curDatabase: The name of the current database
    # @param command: The string of command that needs to be validated for deleting
    def checkValidDelete(self, curDatabase, table, command):
        try:
            if (command[0].lower() == "where"):
                with open("%s/%s.txt" % (curDatabase, table)) as f:
                    temp = f.read()
                metaData = temp [0 : temp.index("\n")].split(" | ")
                for ele in metaData:
                    tmp  = ele.split(" ")
                    if (tmp[0] == command[1]):
                        return True
                return False
            else:
                return False
        except:
            return False

    #Check if the update bieng attempted is valid
    # @param curDatabase: The name of the current database
    # @param table: The name of the table attempting to be updated
    # @param command: The string of command that needs to be validated for updating
    def checkValidUpdate(self, curDatabase, table, command):
        try:
            if (command[0].lower() == "set"):
                updateAttributeName = []
                updateAttributeName.append(command[1])
                updateAttributeName.append(command[3])
                if(self.checkValidAttribute(curDatabase, table, updateAttributeName)):
                    attributeName = []
                    attributeName.append(command[5])
                    attributeName.append(command[7])
                    if(command[2] == "=" and command[4].lower() == "where" and self.checkValidAttribute(curDatabase, table, attributeName)):
                        if (self.containsData(curDatabase, table, attributeName)):
                            return True
            return False
        except:
            return False

    #Check if attribute and the corresponding data is valid
    # @param curDatabase: the current working database
    # @param table: the table in question
    # @param attributeName: a list contianing the attribute name and data
    def checkValidAttribute(self, curDatabase, table, attributeData):
        try:
            with open("%s/%s.txt" % (curDatabase, table)) as f:
                temp = f.read()
            metaData = temp [0 : temp.index("\n")].split(" | ")
            for ele in metaData:
                attributes = ele.split(" ")
                if (attributes[0] == attributeData[0]):
                    if (attributes[1].lower() == "int" and attributeData[1].isnumeric()):            
                        return True
                    elif ("varchar(" in attributes[1].lower()):
                        return True
                    elif (attributes[1].lower() == "float" and float(attributeData[1]) and '.' in attributeData[1]):
                        return True
                    else:
                        return False   
        except:
            return False
