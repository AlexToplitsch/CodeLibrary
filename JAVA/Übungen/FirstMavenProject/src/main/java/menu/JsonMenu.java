package menu;

import com.fasterxml.jackson.databind.JsonNode;
import json.JSONReader;
import json.JsonComparatorASC;
import json.JsonComparatorDESC;
import json.objects.ValueCountObject;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

import javax.swing.*;
import javax.swing.filechooser.FileNameExtensionFilter;
import java.io.File;
import java.io.IOException;
import java.util.Arrays;
import java.util.Scanner;

public class JsonMenu {
    // ##### Properties #####
    private static final Logger LOG = LogManager.getLogger(JsonMenu.class);
    private static ValueCountObject obj;
    private static final Scanner in = new Scanner(System.in);
    private static final JSONReader reader = new JSONReader();

    // ##### Functions #####
    public static void main() {
        if (selectPath()) {
            sortJSONArray();
            printSortedObjects();
        }
    }

    /**
     * Prints the sorted JSON Object
     */
    private static void printSortedObjects() {
        JsonNode node = reader.objectToJson(obj.getValue());
        LOG.info(node.toPrettyString());
    }

    /**
     * Opens the JFileChooser with selection mode files only and file filter set on only .txt and
     * .json files. If the file chooser was closed with the approve option, then the function
     * createJSONObject will be called, otherwise nothing happens.
     */
    private static boolean selectPath() {
        JFileChooser chooser = new JFileChooser("D:\\");
        // Window settings
        chooser.setFileSelectionMode(JFileChooser.FILES_ONLY);
        chooser.setFileFilter(new FileNameExtensionFilter("Text files", "txt"));
        chooser.setFileFilter(new FileNameExtensionFilter("JSON", "json"));
        chooser.setAcceptAllFileFilterUsed(false);

        int option = chooser.showOpenDialog(null); // how the FileChooser was closed
        // if the open button is clicked
        if (option == JFileChooser.APPROVE_OPTION) {
            File f = chooser.getSelectedFile();
            return createJSONObject(f.getAbsolutePath());
        }
        // if the cancel button was clicked
        else if (option == JFileChooser.CANCEL_OPTION) {
            LOG.info("See ya later!");
        } else {
            LOG.error("Error: Error at file choosing!");
        }
        return false;
    }

    /**
     * Reads the next line from the terminal and tries to parse it into an integer. If the line is
     * not parsable the decision is set to -1
     * @return int
     */
    private static int decideASCorDESC() {
        int decision;
        try {
            decision = Integer.parseInt(in.nextLine());
        } catch (NumberFormatException e) {
            decision = -1;
        }
        return decision;
    }

    /**
     * Creates an ValueCountObject from a text file or json file
     * @param path Abstract path where the file is stored
     * @return boolean: True if creation was successful; False if it was not successful;
     */
    private static boolean createJSONObject(String path) {
        try {
            obj = reader.makeObjects(path, ValueCountObject.class);
            return true;
        } catch (UnsupportedOperationException | IOException uOE) {
            LOG.error("Es ist folgender Fehler aufgetreten: " + uOE.getMessage());
            LOG.error("Error: " + uOE.getMessage());
        }
        return false;
    }

    /**
     * Calls the decide function as long as the return value of the function is not 1 or 2.
     * If the decision is 1 then the JSON array is sorted ascending if 2, then the JSON array
     * is sorted descending
     */
    private static void sortJSONArray(){
        int decision;
        do {
            LOG.info("Wollen Sie die Objekte alphabetisch aufsteigend[1] oder absteigend[2] " + "sortieren: ");
            decision = decideASCorDESC();
        } while (decision != 1 && decision != 2);
        if (decision == 1) {
            Arrays.sort(obj.getValue(), new JsonComparatorASC());
        } else {
            Arrays.sort(obj.getValue(), new JsonComparatorDESC());
        }
    }
}
