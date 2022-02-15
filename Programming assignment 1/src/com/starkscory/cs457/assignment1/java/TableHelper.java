package com.starkscory.cs457.assignment1.java;

import java.io.File;
import java.io.IOException;


public class TableHelper {
    public static String createDefaultTable(Integer defNum, String workingDirectory, String loadedDatabase) throws IOException {
        File myObj = new File(workingDirectory + "/" + loadedDatabase + "/" + defNum + "_Table.txt");
        try {
            if (myObj.createNewFile()) {
                return "Default table created successfully\n";
            } else {
                return "An Error has occurred.";
            }
        } catch (IOException e) {
            return "An Error has occurred.";
        }

    }

    public static String createTableWithInput (String workingDirectory, String loadedDatabase, String nameOfTable) {
        File myObj = new File(workingDirectory + "/" + loadedDatabase + "/" + nameOfTable + ".txt");
        try {
            if (myObj.createNewFile()) {
                return nameOfTable + " created successfully in " + loadedDatabase + ".";
            } else {
                return "Error Creating table";
            }
        } catch (IOException e) {
            return "Error Creating table";
        }
    }

    public static String deleteTableWithInput (String workingDirectory, String loadedDatabase, String nameOfTable) {
        File myObj = new File(workingDirectory + "/" + loadedDatabase + "/" + nameOfTable + ".txt");
        if (myObj.delete()) {
            return nameOfTable + " deleted successfully in " + loadedDatabase + ".";
        } else {
            return "Error deleting table, probably doesn't exist.";
        }
    }
}
