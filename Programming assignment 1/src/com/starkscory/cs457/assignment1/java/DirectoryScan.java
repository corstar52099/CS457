package com.starkscory.cs457.assignment1.java;

import java.io.File;
import java.io.IOException;
import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

//TODO: file number interator does not work with current implementation of loaded database;

public class DirectoryScan{
    private String workingDirectory;
    private String loadedDatabaseName;
    private Scanner scan;
    private Integer folderNumberIterator = 1;
    private Integer fileNumberIterator = 1;
    private static File folder;
    private static File[] listOfFiles;
    private static Set<String> setOfDirectoryNames;
    private static Set<String> setOfFileNames;
    //TODO: Handle loaded database errors
    public DirectoryScan(){
        scan = new Scanner(System.in);
        workingDirectory = new File("").getAbsolutePath();
        loadedDatabaseName = null;
        setOfDirectoryNames =  new HashSet<>();
        setOfFileNames = new HashSet<>();
        folder = new File(workingDirectory);
        listOfFiles = folder.listFiles();
        for (int i = 0; i < listOfFiles.length; i++) {
            if (listOfFiles[i].isFile()) {
                if (listOfFiles[i].getName().contains("_Table")){
                    fileNumberIterator++;
                }
                setOfFileNames.add(listOfFiles[i].getName());
            } else if (listOfFiles[i].isDirectory()) {
                if (listOfFiles[i].getName().contains("_Database")){
                    folderNumberIterator++;
                }
                setOfDirectoryNames.add(listOfFiles[i].getName());
            }
        }
        //TODO: error catching
    }

    public String scanDirectory(){ return this.scan.next(); }
    public String scanDirectoryLine(){ return this.scan.nextLine(); }

    public String addNewDirectory() {
        File newDirectory = new File(this.workingDirectory + "/" + this.folderNumberIterator + "_Database");
        this.loadedDatabaseName = this.folderNumberIterator + "_Database";
        this.folderNumberIterator++;
        Boolean returnVal = newDirectory.mkdir();
        this.listOfFiles = this.folder.listFiles();
        if (newDirectory.mkdir()) {
            this.listOfFiles = folder.listFiles();
            return this.folderNumberIterator + "_Database" + " has been created successfully.";
        }
        return "Failed to make database.";
    }
    public String addNewDirectory(String addedDirectory) {
        int duplicateIterator = 0;
        if (doesThisDirectoryExist(addedDirectory)) {
            while (doesThisDirectoryExist(addedDirectory + duplicateIterator)) {
                duplicateIterator++;
            }
            File newDirectory = new File(this.workingDirectory + "/" + addedDirectory + duplicateIterator);
            if (newDirectory.mkdir()) {
                this.listOfFiles = folder.listFiles();
                this.loadedDatabaseName = addedDirectory + duplicateIterator;
                setOfDirectoryNames.add(addedDirectory + duplicateIterator);
                return addedDirectory + duplicateIterator + " has been created successfully.";
            }
            return "Failed to make database.";
        }
        File newDirectory = new File(this.workingDirectory + "/" + addedDirectory);
        if (newDirectory.mkdir()) {
            this.listOfFiles = folder.listFiles();
            this.loadedDatabaseName = addedDirectory;
            setOfDirectoryNames.add(addedDirectory);
            return addedDirectory + " has been created successfully.";
        }
        return "Failed to make database.";
    }
    public static String deleteDirectory(File file)
    {
        // store all the paths of files and folders present
        // inside directory
        for (File subfile : file.listFiles()) {

            // if it is a subfolder,e.g Rohan and Ritik,
            // recursiley call function to empty subfolder
            if (subfile.isDirectory()) {
                deleteDirectory(subfile);
            }

            // delete files and empty subfolders
            subfile.delete();
        }
        return "Deleted database and tables within";
    }
    public boolean doesThisDirectoryExist(String thisDirectory){
        //TODO: error catching
        for (String d : setOfDirectoryNames) {
            if (thisDirectory.equals(d)) {
                return true;
            }
        }
        return false;
    }

    public void loadDatabase (String databaseToLoad) {
        this.loadedDatabaseName = databaseToLoad;
    }

    public String createTable() throws IOException {
        if (this.workingDirectory.equals(null)) {
            return "You have not loaded a DATABASE. USE {DATABASE_NAME} <--- Usage to load a database to use";
        }
        this.fileNumberIterator++;
        return TableHelper.createDefaultTable(this.fileNumberIterator, this.workingDirectory, this.loadedDatabaseName);
    }

    public String createTable(String tableToCreate) {
        if (this.workingDirectory.equals(null)) {
            return "You have not loaded a DATABASE. USE {DATABASE_NAME} <--- Usage to load a database to use";
        }
        this.fileNumberIterator++;
        return TableHelper.createTableWithInput( this.workingDirectory, this.loadedDatabaseName, tableToCreate);
    }

    //TODO: fix the file number interator bug that will enter the negatives
    public String deleteTable(String tableToDelete) {
        this.fileNumberIterator--;
        return TableHelper.deleteTableWithInput( this.workingDirectory, this.loadedDatabaseName, tableToDelete);
    }

    public Set<String> getSetOfDirectoryNames () {
        return this.setOfDirectoryNames;
    }

    public String decideCommand () throws IOException {
        //do a fancy algorithm that decides the command
        String firstWord  = this.scanDirectory();
        if (firstWord.equalsIgnoreCase("EXIT")) {
            return "exit";
        }
        String secondWord = this.scanDirectory();
        Boolean semiColonFlag = false;
        if (secondWord.contains(";")) {
            secondWord = secondWord.substring(0, secondWord.indexOf(";"));
            semiColonFlag = true;
        }
        if (firstWord.equalsIgnoreCase("CREATE")) {
            return create(secondWord, semiColonFlag);
        }
        else if (firstWord.equalsIgnoreCase("DELETE")) {
            return delete(secondWord, semiColonFlag);
        }
        else if (firstWord.equalsIgnoreCase("UPDATE")) {
            update(secondWord);
        }
        else if (firstWord.equalsIgnoreCase("QUERY")) {
            query(secondWord);
        }
        else if (firstWord.equalsIgnoreCase("USE")) {
           return use(secondWord);
        }
        else {return "ERROR! " + firstWord + " is not a valid first command";}
        return "";
    }

    private String use(String command) {
        if (!doesThisDirectoryExist(command)) {
            return command + " is not an existing database.";
        }
        this.loadedDatabaseName = command;
        return command + " loaded successfully.";
    }

    private String create(String command, Boolean semiColonFlag) throws IOException {
        if (command.equalsIgnoreCase("DATABASE")) {
            //create a database
            if (semiColonFlag) {
               return addNewDirectory();
            }
            String databaseToCreate = this.scanDirectory();
            if (databaseToCreate.contains(";")) {
                return addNewDirectory(databaseToCreate.substring(0, databaseToCreate.indexOf(";")));
            }
            return addNewDirectory(databaseToCreate);
        }
        else if (command.equalsIgnoreCase("TABLE")) {
            //create a table
            if (semiColonFlag) {
                return this.createTable();
            }
            String tableToCreate = this.scanDirectory();
            if (tableToCreate.contains(";")) {
                //TODO: Big fat todo here, need to implement creating a table with parameters
                return this.createTable(tableToCreate.substring(0, tableToCreate.indexOf(";")));
            }
            return this.createTable(tableToCreate);
        }
        return command + " is not a valid CREATE command.";
    }
    private String delete(String command, Boolean semiColonFlag){
        if (semiColonFlag) {
            return "Must specify database to delete";
        }
        if (command.equalsIgnoreCase("TABLE")) {
            //delete a database
            String tableToDelete = this.scanDirectory();
            if (tableToDelete.contains(";")) {
                return deleteTable(tableToDelete.substring(0, tableToDelete.indexOf(";")));
            }
            return deleteTable(tableToDelete);
        }
        else if (command.equalsIgnoreCase("DATABASE")) {
            //delete a table
            String databaseToDelete = this.scanDirectory();
            if (databaseToDelete.contains(";")) {
                return deleteDirectory(new File(workingDirectory + "/" + databaseToDelete.substring(0,databaseToDelete.indexOf(";"))));
            }
            return deleteDirectory(new File(workingDirectory + "/" + databaseToDelete));
        }
        return command + " is not a valid DELETE command";
    }
    private boolean update(String command){
        int indexOfFirstSpace = command.indexOf(" ");
        int indexOfFirstSemicolon = command.indexOf(";");
        if (!(indexOfFirstSpace > indexOfFirstSemicolon)) {
            return false;
        }
        if (command.equals("TABLE")) {
            //create a table
            return true;
        }
        return false;
    }
    private void query(String command){

    }
}