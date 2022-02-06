import java.io.File;
import java.util.Scanner;

public class DatabaseInitializer extends DatabaseTool{
    //Database intiializer is going to initialize a database that has some information.
    //Information that is stored in a parent class
    public void DatabaseInitializer () {
         DirectoryScan init =  new DirectoryScan();

         init.addNewDirectory("Directory" + 1);
        //TODO: Step 1: Create Database Folder if one does not exist
        //get current directory

        //TODO: Step 2: inside of the Database Folder, Create a table folder

        //TODO: Step 3: POSSIBLY create a config file if there is time.
    }
}
