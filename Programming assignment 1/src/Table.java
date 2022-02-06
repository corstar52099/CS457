import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;
import javax.swing.*;


public class Table {
    private Integer rows = 0;
    private Integer cols = 0;
    private Set<String> keys;
    private Map<Integer, String> superKey;

    //Default Constructor
    public Table() {
        keys = new HashSet<>();
        keys.add("ID");
        superKey = new HashMap<>();
        rows = 10;
        cols = 1;
    }
    //Parametrised constructor
    public Table (Integer rows, Integer cols, Set<String> keys) {
        if (!keys.contains("ID")) {
            keys.add("ID");
        }
        this.rows = rows;
        this.cols = cols;
        this.keys = keys;
    }
    //Copy constructor
    public Table(Table tableToCopy) {
        this.rows = tableToCopy.rows;
        this.cols = tableToCopy.cols;
        this.keys = tableToCopy.keys;
    }

    public void addRows(int n) {
        rows += n;
    }

    public void addEntry(Object o) {
        if (this.keys.contains(o.toString())) {
            throw new RuntimeException(o.toString() + " already exists in this table.");
        }
        cols++;
        this.keys.add(o.toString());
    }
}
