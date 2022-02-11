package com.starkscory.cs457.assignment1.java;

import javax.xml.crypto.Data;

public class commandHandler {
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
