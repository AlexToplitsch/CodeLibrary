package com.company;

import java.io.*;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;


public class MyFileWriter {
    private String path;
    private String filename;
    private static final Logger logger = LogManager.getLogger(Menu.class);
    File file = new File("");

    // ##### Constructor #####
    public MyFileWriter() {

    }


    // ##### Getter / Setter #####
    public String getPath() {
        return path;
    }
    public String getFilename() {
        return filename;
    }

    /**
     * Stores the valid path in the property path,
     * Returns true and if the path is valid and false if the path is not valid.
     * If the last char is not a backslash, one will be appended
     *
     * @param path String, that represents the path of the file
     * @return boolean
     */
    private boolean setPath(String path) {
        if (path.charAt(path.length() - 1) != '\\') {
            path = path + "\\";
        }
        if (pathIsValid(path)) {
            this.path = path;
            file = new File(path);
            logger.info("Success: Path setting was successfull!");
            return true;
        } else {
            logger.info("Error: Failure at path setting!");
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
    private boolean setFilename(String name) {
        if (fileIsValid(name)) {
            this.filename = name;
            logger.info("Success: Filename setting was successful!");
            return true;
        } else {
            logger.info("Error: Failure at filename setting!");
            return false;
        }
    }

    /**
     * Sets the fileName and the path properties.
     * @param filePath The absolute path
     * @return boolean. True if everything is valid, False if fileName or path is invalid
     */
    public boolean setFilePath(String filePath){
        return setFilename(separateFilename(filePath)) && setPath(separatePath(filePath));
    }


    // ##### Functions #####

    /**
     * Writes the String str in the file which is saved in path+filename
     *
     * @param str file path where the file is saved
     * @throws IOException if the named file exists but is a directory rather than a regular file,
     *                     does not exist but cannot be created, or cannot be opened for any other reason
     *                     External annotations:
     */
    public void writeToFile(String str, Logger logger) throws IOException {
        if (this.pathExists()) {
            logger.warn(
                    "New Operation:\n" + "________________________________________________________________\n" + str +
                            "\n________________________________________________________________\n");
            logger.info("Success: Successfully written in logfile!");
            copyToDestination();
        }
    }

    /**
     * Creates all necessary directories of the path, if it doesn't exist.
     */
    public void createDirectories() {
        if (!file.exists()) {
            if(file.mkdirs()) {
                logger.info("Success: Path creation successful!");
            }
            else{
                logger.info("Error: Path creation failed!");
            }
        }
    }

    /**
     * Checks if the str is a valid windows file path eg.: D:\path\directory\
     *
     * @param str String, that represents the windows path
     * @return boolean
     */
    private boolean pathIsValid(String str) {
        return str.matches("([a-zA-Z]:\\\\)([^*?:/\\\\\"<>|]+\\\\)*");
    }

    /**
     * Checks if the str is a valid windows filename
     *
     * @param str String, that represents the filename
     * @return boolean
     */
    private boolean fileIsValid(String str) {
        return str.matches("[^*?:/\\\\\"<>|]+\\.txt");
    }

    /**
     * Checks if the path exists.
     *
     * @return boolean true if the path exists, false if the path doesn't exists
     */
    public boolean pathExists() {
        return file.exists();
    }

    /**
     * Copies the operation.txt file from c:\temp to the file which is represented by the fields
     * filename and path of this class.
     */
    private void copyToDestination() {
        try {
            BufferedReader br = new BufferedReader(new FileReader(
                    "C:\\temp\\operation.log"));
            BufferedWriter fw = new BufferedWriter(new FileWriter(path + filename));
            fw.write(""); // clear the text file
            String st;
            while((st=br.readLine()) != null){
                fw.append(st).append("\n");
            }
            fw.close();
            br.close();
        } catch(IOException throwable){
            System.out.println(throwable.getMessage());
        }
    }

    /**
     * Separates the filename from the path and returns the path.
     *
     * @param filePath file path
     * @return path without the filename
     */
    private String separatePath(String filePath) {
        return filePath.split("[^*?:/\\\\\"<>|]+\\.txt")[0];
    }

    /**
     * Separates the filename from the path and returns the filename.
     *
     * @param filePath path of the file
     * @return filename without the path
     */
    private String separateFilename(String filePath) {
        return filePath.split("([a-zA-Z]:\\\\)([^*?:/\\\\\"<>|]+\\\\)*")[1];
    }
}
