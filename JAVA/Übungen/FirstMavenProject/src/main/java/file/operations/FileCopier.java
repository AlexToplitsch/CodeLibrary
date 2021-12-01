package file.operations;

import java.io.*;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

public class FileCopier {
    // ##### Properties #####
    private String startPath;
    private String destinationPath;
    private static final Logger LOGGER = LogManager.getLogger(FileCopier.class);


    // ##### Constructor #####
    public FileCopier(String startPath, String destinationPath) throws FileNotFoundException {
        if (fileNotExists(startPath)) {
            throw new FileNotFoundException("Start file not found at: " + startPath);
        } else if (fileNotExists(destinationPath)) {
            throw new FileNotFoundException("Destination file not found at: " + destinationPath);
        } else {
            this.startPath = startPath;
            this.destinationPath = destinationPath;
        }
    }


    // ##### Getter/Setter #####
    public void setStartPath(String startPath) {
        this.startPath = startPath;
    }

    public String getStartPath() {
        return startPath;
    }

    public void setDestinationPath(String destinationPath) {
        this.destinationPath = destinationPath;
    }

    public String getDestinationPath() {
        return destinationPath;
    }


    // ##### Functions #####
    /**
     * Copies the file from the start path to the  destination path.
     *
     * @return boolean: True if the copy process was successful; False if an error has
     * occurred
     */
    public boolean copyFile() {
        try {
            FileInputStream input = new FileInputStream(startPath);
            FileOutputStream output = new FileOutputStream(destinationPath);
            int data;
            do {
                data = input.read();
                output.write(data);
            } while (data != -1);
            LOGGER.info("Success: Copying file was successful!");
            return true;
        } catch (IOException e) {
            LOGGER.info("Error: " + e.getMessage());
        }
        return false;
    }

    /**
     * Checks if the Path exists
     *
     * @param filePath abstract pathname, where a file should exists
     * @return boolean - True if the file does not exist, False if the file exists
     */
    private boolean fileNotExists(String filePath) {
        return !new File(filePath).exists();
    }

    /**
     * Creates a File by this abstract path, if it not already exists
     *
     * @param filePath Abstract path where the file will be created
     * @return boolean: True if  the file does not exists and was created successfully;
     * False if the already exists or an error has occurred;
     */
    public static boolean createFile(String filePath) {
        File f = new File(filePath);
        if (!f.exists()) {
            try {
                if (f.createNewFile()) {
                    LOGGER.info("Success: File creation successful!");
                    return true;
                } else {
                    LOGGER.info("Error: File already exists!");
                }
            } catch (IOException e) {
                LOGGER.error("Error: " + e.getMessage());
            }
        }
        return false;
    }

    /**
     * Separates the filename from the path and returns the filename.
     *
     * @param filePath path of the file
     * @return filename without the path
     */
    public static String separateFilename(String filePath) {
        return filePath.split("([a-zA-Z]:\\\\)([^*?:/\\\\\"<>|]+\\\\)*")[1];
    }
}
