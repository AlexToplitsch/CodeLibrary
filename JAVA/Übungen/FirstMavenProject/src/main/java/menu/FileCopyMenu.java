package menu;

import file.operations.FileCopier;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

import javax.swing.*;
import java.io.File;
import java.io.FileNotFoundException;

public class FileCopyMenu {

    private static final Logger LOGGER = LogManager.getLogger(FileCopyMenu.class);
    private static FileCopier fC;

    public static void main(){
        if(selectStartFile()) {
            if(startCopying()){
                LOGGER.info("Successfully copied the file at " + fC.getStartPath() +
                        " to " + fC.getDestinationPath());
            }
        }
    }

    /**
     * Opens the JFileChooser to select any file. If the open button was clicked it calls the
     * selectDestinationPath function an passes the filename and the start path. If the cancel
     * button was clicked or any error has occurred the function will get canceled.
     *
     * @return boolean: True if the path setting of start and destination path successful; False
     * if something else happens;
     */
    private static boolean selectStartFile() {
        JFileChooser chooser = new JFileChooser("D:\\");
        // Window settings
        chooser.setFileSelectionMode(JFileChooser.FILES_ONLY);

        int option = chooser.showOpenDialog(null); // how the FileChooser was closed
        // if the open button is clicked
        if (option == JFileChooser.APPROVE_OPTION) {
            File f = chooser.getSelectedFile();
            return selectDestinationPath(FileCopier.separateFilename(f.getAbsolutePath()),
                                         f.getAbsolutePath());
        }
        // if the cancel button was clicked
        else if (option == JFileChooser.CANCEL_OPTION) {
            LOGGER.info("See ya later!");
        }
        else{
            LOGGER.info("Error: Error at file choosing!");
        }
        return false;
    }

    /**
     * Opens the JFileChooser and calls a function to create the file in its new destination.
     * If the creation was successful the data of the original file will be copied to the copy file.
     * @param fileName Filename that will be appended to the destination path
     * @param startPath Start path where the original file is stored
     * @return boolean: True if the copy process was successful; False if  it wasn't successful
     * or anything else happened;
     */
    private static boolean selectDestinationPath(String fileName, String startPath) {
        JFileChooser chooser = new JFileChooser("D:\\");
        // Window settings
        chooser.setFileSelectionMode(JFileChooser.DIRECTORIES_ONLY);

        int option = chooser.showOpenDialog(null); // how the FileChooser was closed
        // if the open button is clicked
        if (option == JFileChooser.APPROVE_OPTION) {
            try {
                File f = chooser.getSelectedFile();
                String destinationPath = f.getAbsolutePath() + "\\" + fileName;
                if(FileCopier.createFile(destinationPath)) {
                    fC = new FileCopier(startPath, destinationPath);
                    return true;
                }
            }catch(FileNotFoundException e){
                LOGGER.info("Error: " + e.getMessage());
            }
        }
        //if the cancel button is clicked
        else if (option == JFileChooser.CANCEL_OPTION) {
            LOGGER.info("See ya later!");
        }
        else{
            LOGGER.info("Error: Error at file choosing!");
        }
        return false;
    }

    /**
     * Starts the copy process
     * @return boolean: True if the process was successful; False if the process was not
     * successful;
     */
    private static boolean startCopying(){
        return fC.copyFile();
    }

}
