from mailbox import linesep
import os, shutil
from genericpath import isfile

#alter a table
# @param filename: the name of the file to open
# @param fun: the type of function (add or delete)
# @param thingChanging: the individual metadata changing
class databaseHelper:

    print_buffer = []

    def __init__(self) -> None:

        self.print_buffer = []

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

    def useDatabase(self, startingDir, databaseToUse):
        try:
            os.chdir(startingDir + '/' + databaseToUse)
            self.print_buffer.append("Using database " + databaseToUse)
            return True
        except Exception as e:
            self.print_buffer.append("Could not use database %s becasue of %s." % (databaseToUse, e))
            return False

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

    def createDatabase(self, startingDir, databaseName):
        try:
            os.mkdir(startingDir + "/" +databaseName)
            self.print_buffer.append("Database " + databaseName + " created.")
        except Exception as e:
            self.print_buffer.append("Failed to create database %s becasuse %s" % (databaseName, e))

    def dropTable(self, curDatabase, tableToDrop):
        try:
            os.remove(curDatabase + "/" + tableToDrop + ".txt")
            self.print_buffer.append("Table %s deleted." % tableToDrop)
        except Exception as e:
            self.print_buffer.append("Failed to delete table %s becasue of %s" % (tableToDrop, e))

    def dropDatabase(self, startingDir, databaseToDrop):
        try:
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

    def selectFrom(self, curDatabase, table):
        try:
            with open(curDatabase + "/" + table + ".txt", 'r') as f:
                self.print_buffer.append(f.read())
        except Exception as e:
            self.print_buffer.append("Failed to select from table becasue of %s" % e)
    
    def printBuffer(self):
        for s in self.print_buffer:
            print(s)

    def insertInto(self, curDatabase, table, data):
        if (self.checkValidData(curDatabase, table, data)):
            with open(curDatabase + "/%s.txt" % table, 'a') as f:
                f.write('\n' + ' | '.join(data))
                self.print_buffer.append("1 new record inserted.")
        else:
            self.print_buffer.append("Falied to insert table %s becasue data is invalid." % table)

    def insertIntoSyntax(self, stringToCheck, lastString):
        substring = "values("
        if( stringToCheck != None and substring in stringToCheck):
            for c in lastString:
                if (c == ')'):
                    return True
        else:
            return False
    
    def checkValidData(self, curDatabase, table, data):
        try:
            with open("%s/%s.txt" % (curDatabase, table), 'r') as f:
                tmp = f.read()

                line = tmp[ 0 : tmp.index('\n') ].split(' | ')
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
            
