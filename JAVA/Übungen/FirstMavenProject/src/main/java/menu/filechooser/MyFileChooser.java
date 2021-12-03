package menu.filechooser;

import javax.swing.*;
import javax.swing.filechooser.FileNameExtensionFilter;

public class MyFileChooser {
    //########################### Properties ####################################
    private JFileChooser chooser;
    private String currentDirectoryPath;
    private boolean allFilesFilter;

    //########################### Constructor ####################################
    public MyFileChooser(String currentDirectoryPath, boolean allFilesFilter){
        this.currentDirectoryPath = currentDirectoryPath;
        this.allFilesFilter = allFilesFilter;
    }

    //########################### Getter/Setter ####################################

    public String getCurrentDirectoryPath() {
        return currentDirectoryPath;
    }

    public void setCurrentDirectoryPath(String currentDirectoryPath) {
        this.currentDirectoryPath = currentDirectoryPath;
    }

    public boolean isAllFilesFilter() {
        return allFilesFilter;
    }

    public void setAllFilesFilter(boolean allFilesFilter) {
        this.allFilesFilter = allFilesFilter;
    }

    public JFileChooser getChooser(){
        if(chooser == null){
            initChooser();
        }
        return chooser;
    }

    //########################### Functions ####################################
    public void initChooser(){
        chooser = new JFileChooser(currentDirectoryPath);
        chooser.setFileSelectionMode(JFileChooser.FILES_ONLY);
        chooser.setAcceptAllFileFilterUsed(allFilesFilter);
    }

    public void setFileFilter(String description, String extension){
        if(chooser == null){
            initChooser();
        }
        chooser.setFileFilter(new FileNameExtensionFilter(description, extension));
    }
}
