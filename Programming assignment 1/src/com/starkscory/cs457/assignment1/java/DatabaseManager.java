package com.starkscory.cs457.assignment1.java;

import java.io.IOException;
import java.util.Scanner;

//TODO: A new Database should be created in correct place
//TODO: A new Table should be created in the correct place

public class DatabaseManager {
    public static void main(String[] args) throws IOException {

        DatabaseInitializer Init= new DatabaseInitializer();
        System.out.println("Welcome to Cory's Database management tool\n");
        boolean menuFlag = false;
        //eventually add option to create new database or load a different database again.
        printStartMenu();
        Scanner mainScan = new Scanner(System.in);
        int option = 0;
        while (!menuFlag) {
            option = mainScan.nextInt();
            if (option == 1) {
                //create new database option
                System.out.println(Init.init());
                menuFlag = true;
            } else if (option == 2) {
                //TODO: Implement Load existing database option
                System.out.println("Which database would you like to load?: ");
                Init.printLoadOptions();
                menuFlag = true;
            } else {
                System.out.println("Please enter a valid option!");
            }
        }

        while (menuFlag) {
            printLoopMenu();
            option = mainScan.nextInt();
            switch (option) {
                case 1:
                    Init.tableInit();
                case 2:
                case 3:
                case 4:
                case 5:
            }
            //print()
        }
        //start the database

        //TODO: Implement Multiple commands such as: CREATE_DATABASE,
        // DELETE_DATABASE, CREATE TABLE, DELETE TABLE, UPDATE, QUERY
    }

    //TODO: possibly implement cusomizable menu with config
    static public void printStartMenu() {
        System.out.println("Cory's Database Management Tool:\n" +
                "--------------------------------\n" +
                "1: Create New Database\n" +
                "2: Load Existing Database\n" +
                "Which would you like to do?: ");
    }

    static public void printLoopMenu() {
        System.out.println("Cory's Database Management Tool:\n" +
                "--------------------------------\n" +
                "1: Create Table\n" +
                "2: Delete Table\n" +
                "3: Update Table\n" +
                "4: Query Table\n" +
                "5: Exit\n" +
                "Which would you like to do?: ");
    }
}