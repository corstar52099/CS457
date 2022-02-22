from distutils import command
from genericpath import isfile
import os, shutil
from re import sub
def removeOuterParentheses(self):
        stack = []
        res=""
        for s in self:
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

def makeAndFillTable(filename, contents):
    with open(filename, 'w') as f:
        for s in contents:
            s = s.strip()
            f.write(s + "\n")

def alterTable(filename, fun, thingChanging):
    print("gets here")
    if (fun.lower() == 'add'):
        with open(filename, 'a') as f:
            f.write(thingChanging + "\n")
    elif (fun.lower() == 'delete'):
        with open(filename, 'r') as f:
            contents = f.read()
        with open(filename, 'w') as f:
            contents.remove(thingChanging)
            f.write(thingChanging)
#TODO: need to make it so that if the table already exists do not do anything
if __name__ == "__main__":
    print("Welcome to Cory's database tool")
    curDatabase = None
    startingDir = os.getcwd()
    commandString = input()
    commandArray = commandString.split(";")
    print(commandArray)
    while (commandArray != 'exit'):
        for s in commandArray:
            subCommand = s.split(" ")
            while("" in subCommand) :
                subCommand.remove("")
            if (subCommand[0].lower() == 'use'):
                try:
                    os.chdir(startingDir + '/' + subCommand[1])
                    curDatabase = os.getcwd()
                    print("Using database " + subCommand[1])
                except Exception as e:
                    print("Could not create database becasue of %s." % e)
            elif (subCommand[0].lower() == 'create'):
                if (subCommand[1].lower() == 'database'):
                   # print("gets here")
                    try:
                        os.mkdir(subCommand[2])
                        print("Database " + subCommand[2] + " created.")
                    except Exception as e:
                        print ("Failed to create database becasuse %s" % e)
                elif (subCommand[1].lower() == 'table'):
                    if (isfile(curDatabase + "/" + subCommand[2] + ".txt")):
                        print("Failed to create table %s becasue it already exists." % subCommand[2])
                        continue
                    elif (curDatabase == None):
                        print("Failed to create table %s becasue there is no database being used." % subCommand[2])
                        continue
                    x = subCommand[3:len(subCommand)]
                    tableCon = ' '.join(x)
                    #get rid of parenthesis then turn back to an array
                    tableCon  = removeOuterParentheses(tableCon)
                    tableStr = ''.join(tableCon)
                    #tablestr = removeOuterParentheses(tableStr)
                    tableStr = tableStr.split(",")
                    try: 
                        makeAndFillTable(subCommand[2], tableStr)
                        print("Table %s created." % subCommand[2])
                    except Exception as e:
                        print("Failed to create table becasue of %s." % e)
            elif (subCommand[0].lower() == 'drop'):
                if (subCommand[1].lower() == 'table'):
                    try:
                        os.remove(subCommand[2])
                        print("Table %s deleted." % subCommand[2])
                    except Exception as e:
                        print ("Failed to delete table %s becasue of %s" % (subCommand[2], e))
                elif (subCommand[1].lower() == 'database'):
                    try:
                        for filename in os.listdir(startingDir + '/' + subCommand[2]):
                            file_path = os.path.join(startingDir + '/' + subCommand[2], filename)
                            try:
                                if os.path.isfile(file_path) or os.path.islink(file_path):
                                    os.unlink(file_path)
                                elif os.path.isdir(file_path):
                                    shutil.rmtree(file_path)
                                print("Database %s deleted." % subCommand[2])
                            except Exception as e:
                                print('Failed to delete database %s becasue %s' % (subCommand[2], e))
                        os.rmdir(startingDir + '/' + subCommand[2])
                    except Exception as e:
                        print('Failed to delete database %s becasue %s' % (subCommand[2], e))
            elif (subCommand[0].lower() == 'alter'):
                if(subCommand[1].lower() == 'table'):
                    alterTable(subCommand[2], subCommand[3], ' '.join(subCommand[4:6]))
            elif (subCommand[0].lower() == 'select'):
                if (subCommand[1].lower() == '*'):
                    if (subCommand[2].lower() == 'from'):
                        try:
                            with open(subCommand[3], 'r') as f:
                                print(f.read())
                        except Exception as e:
                            print("Failed to select from table becasue of %s" % e)
            elif (subCommand[0].lower() == 'exit'):
                exit()
            else:
                print(subCommand[0] + " is not a valid first command.")
        commandString = input()
        commandArray = commandString.split(";")  
    