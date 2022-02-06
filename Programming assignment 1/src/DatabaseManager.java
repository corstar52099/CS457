public class DatabaseManager {
    public static void main(String[] args){
        System.out.println("Welcome to Cory's Database management tool\n");
        boolean menuFlag = true;

        printStartMenu();

        while (menuFlag) {
            //print()
        }
        //start the database

        //TODO: Implement Multiple commands such as: CREATE_DATABASE,
        // DELETE_DATABASE, CREATE TABLE, DELETE TABLE, UPDATE, QUERY
    }

    //TODO: possibly implement cusomizable menu with config
    static public void printStartMenu() {
        System.out.println("Cory's Database Management Tool:" +
                           "--------------------------------" +
                           "1: Create New Database" +
                           "2: Load Existing Database");
    }
}
