import java.io.File;
import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class DirectoryScan{
    private String workingDirectory;
    private Scanner scan;
    private Integer folderNumberIterator;
    private Integer fileNumberIterator;
    private static File folder;
    private static File[] listOfFiles;
    private static Set<String> setOfDirectoryNames;
    private static Set<String> setOfFileNames;

    public DirectoryScan(){
        this.scan = new Scanner(System.in);
        this.workingDirectory = System.getProperty("user.dir");
        setOfDirectoryNames =  new HashSet<>();
        setOfFileNames = new HashSet<>();
        folder = new File(workingDirectory);
        listOfFiles = folder.listFiles();
        for (File itFile : listOfFiles) {
            for (int i = 0; i < listOfFiles.length; i++) {
                if (listOfFiles[i].isFile()) {
                    if (listOfFiles[i].getName().contains("_Table")){
                        fileNumberIterator++;
                    }
                    setOfFileNames.add(listOfFiles[i].getName());
                } else if (listOfFiles[i].isDirectory()) {
                    if (listOfFiles[i].getName().contains("_Database")){
                        folderNumberIterator++;
                    }
                    setOfDirectoryNames.add(listOfFiles[i].getName());
                }
            }
        }
        //TODO: error catching
    }

    public String scanDirectory(){ return this.scan.next(); }

    public boolean addNewDirectory() {
        //TODO:add a default directory
        return false;
    }

    public boolean doesThisDirectoryExist(String thisDirectory){
        //TODO: error catching
        for (String d : setOfDirectoryNames) {
            if (thisDirectory.equals(d)) {
                return false;
            }
        }
        return true;
    }
}