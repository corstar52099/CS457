package com.starkscory.cs457.assignment1.java;

import com.starkscory.cs457.assignment1.java.DatabaseInitializer;

//Database tool will store necessary information for the database
//Will handle necessary functionality of the database
public class DatabaseTool {
    //Directory that will contain a specific database.

    private String DatabaseUUID;
    // Other files will be contained in /{DatabaseDirectory}
    private String DatabaseDirectory;



    public DatabaseTool(){
        DatabaseUUID = "";
        DatabaseDirectory = "";
    }

    public DatabaseTool(DatabaseInitializer init){

    }

}

