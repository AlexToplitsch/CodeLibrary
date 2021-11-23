package com.company;

public class FileWriter {
    private String path;

    // Constructor
    public FileWriter() {

    }

    // Getter / Setter
    public String getPath() {
        return path;
    }

    /**
     * Stores the the valid path in the property path
     * Returns true if the path is valid and false if the path is not valid
     *
     * @param path String, that represents the path of the file
     * @return boolean
     */
    public boolean setPath(String path) {
        if (isValid(path)) {
            this.path = path;
            return true;
        } else {
            return false;
        }
    }

    /**
     * Checks if the str is a valid windows file path
     * @param str String, that represents the windows path
     * @return boolean
     * */
    private boolean isValid(String str){

    }
}
