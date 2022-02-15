package com.starkscory.cs457.assignment1.java;

import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

public class DatabaseInitializer{
    private DirectoryScan init =  new DirectoryScan();
    private commandHandler commands = new commandHandler();
    //Database intiializer is going to initialize a database that has some information.
    //Information that is stored in a parent class
    public String init () {
         init.addNewDirectory();
         return "Database Successfully created!";
    }

    public void printLoadOptions() {
        //for (String  init.getSetOfDirectoryNames()) {
          //  System.out.println(i + init.getSetOfDirectoryNames().);
        //}
    }

    public String startCommandReading () throws IOException {
        return init.decideCommand();
    }
}
//TODO: Step 1: Create Database Folder if one does not exist
//get current directory

//TODO: Step 2: inside of the Database Folder, Create a table folder whether thats default table or specified one

//TODO: Step 3: POSSIBLY create a config file if there is time.