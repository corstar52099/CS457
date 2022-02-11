package com.starkscory.cs457.assignment1.java;

import java.io.IOException;

public class DatabaseInitializer{
    private DirectoryScan init =  new DirectoryScan();
    private commandHandler commands = new commandHandler();
    //Database intiializer is going to initialize a database that has some information.
    //Information that is stored in a parent class
    public String init () {
         init.addNewDirectory();
         return "Database Successfully created!";
    }

    public void tableInit () throws IOException {
        init.createTable();
    }

    public void printLoadOptions() {
        //for (String  init.getSetOfDirectoryNames()) {
          //  System.out.println(i + init.getSetOfDirectoryNames().);
        //}
    }

    public void handleLoadMenuOption () {

    }
    public boolean decideCommand (String commandString) {
        //do a fancy algorithm that decides the command
        int indexOfFirstSpace = commandString.indexOf(" ");
        final String firstWord = commandString.substring(0, indexOfFirstSpace);
        final String secondWord = commandString.substring(indexOfFirstSpace + 1, commandString.length());
        int indexOfFirstSemicolon = commandString.indexOf(";");
        if (!(indexOfFirstSpace > indexOfFirstSemicolon)) {
            return false;
        }
        else if (firstWord.equals("CREATE")) {
            create(secondWord);
        }
        else if (firstWord.equals("DELETE")) {
            delete(secondWord);
        }
        else if (firstWord.equals("UPDATE")) {
            update(secondWord);
        }
        else {return false;}
        return true;
    }

    private void create(String command){
        int indexOfFirstSpace = command.indexOf(" ");
        int indexOfFirstSemicolon = command.indexOf(";");
        if (!(indexOfFirstSpace > indexOfFirstSemicolon)) {
            return;
        }
        if (command.equals("DATABASE")) {
            //create a database
        }
        else if (command.equals("TABLE")) {
            //create a table
        }
    }
    private void delete(String command){
        int indexOfFirstSpace = command.indexOf(" ");
        int indexOfFirstSemicolon = command.indexOf(";");
        if (!(indexOfFirstSpace > indexOfFirstSemicolon)) {
            return;
        }
        if (command.equals("DATABASE")) {
            //create a database
        }
        else if (command.equals("TABLE")) {
            //create a table
        }
    }
    private void update(String command){
        int indexOfFirstSpace = command.indexOf(" ");
        int indexOfFirstSemicolon = command.indexOf(";");
        if (command.equals("TABLE")) {
            //create a table
        }
    }
    private void query(String command){}
}
//TODO: Step 1: Create Database Folder if one does not exist
//get current directory

//TODO: Step 2: inside of the Database Folder, Create a table folder whether thats default table or specified one

//TODO: Step 3: POSSIBLY create a config file if there is time.