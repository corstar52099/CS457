package com.starkscory.cs457.assignment1.java;

import java.io.*;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;


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

    public static String createTableWithInput(String workingDirectory, String loadedDatabase, String nameOfTable, Map<String, String> mapOfAttributes) {
        File myObj = new File(workingDirectory + "/" + loadedDatabase + "/" + nameOfTable + ".txt");
        try {
            if (myObj.createNewFile()) {
                BufferedWriter writer = new BufferedWriter(new FileWriter(myObj));

                //Loop through the map printing all the attributes and types of the table
                for (Map.Entry<String, String> entry : mapOfAttributes.entrySet()) {
                    writer.write(entry.getKey() + " | "+ entry.getValue());
                    writer.write("\n");
                }
                writer.close();
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

    //builds a map of a table with assumption that table exists
    public static Map<String, String> parseTable (String workingDirectory, String loadedDatabase, String tableToParse) {
        Map<String, String> returnMap = new HashMap<>();
        try {
            File myObj = new File(workingDirectory + "/" + loadedDatabase + "/" + tableToParse + ".txt");
            Scanner myReader = new Scanner(myObj);
            while (myReader.hasNextLine()) {
                String data = myReader.nextLine();
                String attribute  = data.substring(0, data.indexOf(" "));
                String type = data.substring(data.indexOf("|") + 3);
                returnMap.put(attribute, type);
                System.out.println(data);
            }
            myReader.close();
            return returnMap;
        } catch (FileNotFoundException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }
        return returnMap;
    }

    public static String updateTable(String workingDirectory, String loadedDatabase, String tabletoUpdate, String addAttribute, String addType){
        File myObj = new File(workingDirectory + "/" + loadedDatabase + "/" + tabletoUpdate + ".txt");
        try {
            BufferedWriter writer = new BufferedWriter(new FileWriter(myObj));
            writer.write(addAttribute + " | "+ addType);
            writer.close();
            return addAttribute + addType + " added successfully in " + tabletoUpdate + ".";
        } catch (IOException e) {
            return "Error Updating table";
        }
    }

    public static String overWriteTable(Map<String, String> thingsInTable, String workingDirectory, String loadedDatabase, String tabletoUpdate) {
        File myObj = new File(workingDirectory + "/" + loadedDatabase + "/" + tabletoUpdate + ".txt");
        try {
            BufferedWriter writer = new BufferedWriter(new FileWriter(myObj, false));
            for (Map.Entry<String, String> entry : thingsInTable.entrySet()) {
                writer.write(entry.getKey() + " | "+ entry.getValue());
                writer.write("\n");
            }
            writer.close();
            return "Successfully removed ";
        } catch (IOException e) {
            return "Error Updating table";
        }
    }


}
