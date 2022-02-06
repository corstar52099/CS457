import java.io.File;
import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class DirectoryScan{
    private String workingDirectory;
    private Scanner scan;
    private Integer folderNumberIterator;
    public DirectoryScan(){
        this.scan = new Scanner(System.in);
        this.workingDirectory = System.getProperty("user.dir");
        this.folderNumberIterator = 0;
    }

    public String scanDirectory(){ return this.scan.next(); }

    public boolean addNewDirectory(String directoryName) {
        File file = new File(workingDirectory + directoryName);
        return file.mkdir();
    }

    public boolean doesThisDirectoryExist(String thisDirectory){
        Set<String> setOfDirectoryNames = new HashSet<>();
        Set<String> setOfFileNames = new HashSet<>();
        Integer tmpInteger = folderNumberIterator;
        File folder = new File(workingDirectory);

        //iterate over directory names
        File[] listOfFiles = folder.listFiles();
        for (int i = 0; i < listOfFiles.length; i++) {
            if (listOfFiles[i].isFile()) {
                //System.out.println("File " + listOfFiles[i].getName());
            } else if (listOfFiles[i].isDirectory()) {
                setOfDirectoryNames.add(listOfFiles[i].getName());
            }
        }
        for (String d : setOfDirectoryNames) {
            if (thisDirectory.equals(d)) {
                return false;
            }
        }
        return true;
    }
}