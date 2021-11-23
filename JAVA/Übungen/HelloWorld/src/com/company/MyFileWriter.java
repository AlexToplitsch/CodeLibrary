package com.company;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;

public class MyFileWriter {
    private String path;
    private String filename;
    File file = new File("");

    // ##### Constructor #####
    public MyFileWriter() {

    }


    // ##### Getter / Setter #####
    public String getPath() {
        return path;
    }

    /**
     * Stores the valid path in the property path,
     * Returns true if the path is valid and false if the path is not valid.
     * If the last char is not a backslash, one will be appended
     *
     * @param path String, that represents the path of the file
     * @return boolean
     */
    public boolean setPath(String path) {
        if(path.charAt(path.length() -1) != '\\'){
            path = path + "\\";
        }
        if (pathIsValid(path)) {
            this.path = path;
            return true;
        } else {
            return false;
        }
    }

    /**
     * Stores the valid filename in the property filename
     * Returns true if the filename is valid and false if the filename is not valid
     *
     * @param name String, that represents the filename
     * @return boolean
     */
    public boolean setFilename(String name){
        if (fileIsValid(name)) {
            this.filename = name;
            return true;
        } else {
            return false;
        }
    }

    public String getFilename(){
        return filename;
    }


    // ##### Functions #####
    public void save(String str) throws IOException {
        if(createDirectory()){
           FileWriter writer = new FileWriter(path+ filename);
           writer.append("________________________________________________________________\n")
                 .append(str)
                 .append("\n________________________________________________________________\n");
            writer.close();
        }
    }

    private boolean createDirectory(){
        file = new File(path);
        if (!file.exists()){
            return file.mkdirs();
        }
        else return file.exists();
    }
    /**
     * Checks if the str is a valid windows file path eg.: D:\path\directory\
     * @param str String, that represents the windows path
     * @return boolean
     * */
    private boolean pathIsValid(String str){
        return str.matches("([a-zA-Z]:\\\\)([^*?:/\\\\\"<>|]+\\\\)*");

    }

    /**
     * Checks if the str is a valid windows filename
     * @param str String, that represents the filename
     * @return boolean
     * */
    private boolean fileIsValid(String str){
        return str.matches("[^*?:/\\\\\"<>|]+\\.txt");
    }
}
