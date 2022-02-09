package com.starkscory.cs457.assignment1.java;

import java.io.File;
import java.io.IOException;


public class TableHelper {
    public static void createDefaultTable(int defNum, String workingDirectory, String loadedDatabase) throws IOException {
        File myObj = new File(workingDirectory + "/" + loadedDatabase + "/" + defNum + "_Table.txt");
        try {
            if (myObj.createNewFile()) {
                System.out.println("Default table created successfully\n");
            } else {

            }
        } catch (IOException e) {
            System.out.println("An Error has occurred.");
        }

    }
}
