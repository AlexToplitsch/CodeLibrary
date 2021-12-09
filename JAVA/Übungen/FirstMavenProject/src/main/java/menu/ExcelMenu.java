package menu;

import algorithms.sorting.Sorter;
import excel.beans.row.ExcelRowBeans;
import excel.comparator.ExcelComparator;
import excel.reader.ExcelReader;
import menu.filechooser.MyFileChooser;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

import javax.swing.*;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Locale;
import java.util.Scanner;

public class ExcelMenu {
    //######################### Properties ###########################
    private String filePath;
    private ArrayList<ExcelRowBeans> rows;
    Logger logger = LogManager.getLogger(ExcelMenu.class);
    Scanner in = new Scanner(System.in);


    //######################### Constructor #########################
    public ExcelMenu() {
        run();
    }


    //######################### Functions ###########################
    public ArrayList<ExcelRowBeans> getRows() {
        return rows;
    }

    private void run() {
        if (choseFile()) {
            createRowObjects();
            if (sort()) {
                int cellIndex = Integer.parseInt(chooseCellIndex());
                boolean desc = chooseDesc();
                long time = System.currentTimeMillis();
                Sorter.sort(rows, new ExcelComparator(cellIndex, desc));
                time = System.currentTimeMillis() - time;
                System.out.println("Sortierdauer: " + time);
            }
        }
    }


    /**
     * Opens the JFileChooser and lets the user choose xls files to read
     *
     * @return True if chooser was closed with approve_option; False if something else happened
     */
    private boolean choseFile() {
        MyFileChooser mychooser = new MyFileChooser("C:\\", false);
        mychooser.setFileFilter("Excel", "xls");
        JFileChooser chooser = mychooser.getChooser();
        int closeOption = chooser.showOpenDialog(null);
        if (closeOption == JFileChooser.APPROVE_OPTION) {
            filePath = chooser.getSelectedFile().getAbsolutePath();
        } else {
            filePath = "C:\\Users\\toplitsc\\7000_MPM_Milestones_Eng_Dev.xls";
        }
        return true;
    }

    /**
     * Creates an instance of the ExcelReader class and creates an ArrayList of ExcelRowBeans objects
     */
    private void createRowObjects() {
        ExcelReader reader = new ExcelReader(filePath, true);
        try {
            reader.init(0, 0, 0);
        } catch (IOException e) {
            logger.error("Error: " + e.getMessage());
        }
        reader.createRowList();
        rows = reader.getRows();
    }

    /**
     * Reads the next line from the terminal as long as the input is not a number between 0 an 7
     *
     * @return The input from the terminal
     */
    private String chooseCellIndex() {
        System.out.println("Nach welcher Spalte wollen Sie sortieren?");
        System.out.println("ID Zeile: [0], $Projektbezeichnung: [1], Zeilenbezeichnung: [2], Start: [3], Prozent Fretigstellung: [4]," + " Datum Endfixierung: [5], Abteilung: [6], Bemerkung:  [7]");
        String decision;
        while (true) {
            switch (decision = in.nextLine()) {
                case "0":
                case "1":
                case "2":
                case "3":
                case "4":
                case "5":
                case "6":
                case "7":
                    return decision;
                default:
                    System.out.println("Geben Sie eine Zahl zwischen 0 und 7 ein!");
            }
        }
    }

    /**
     * Reads the next line from the terminal as long as the input is not "a" or "d" for ascending/descending order
     *
     * @return true if the input is "d", false, if the input is "a"
     */
    private boolean chooseDesc() {
        System.out.println("In welcher Reihenfolge wollen Sie sortieren?");
        System.out.print("Aufsteigend [a], Absteigend [d]: ");
        while (true) {
            switch (in.nextLine().toLowerCase(Locale.ROOT)) {
                case "a":
                    return false;
                case "d":
                    return true;
                default:
                    System.out.println("Geben Sie [a] für Aufsteigend und [d] für Absteigend ein!");
            }
        }
    }

    /**
     * Reads the next line from the terminal as long as the input is not "j" or "n". It is choosing if the List should be sorted or
     * not.
     *
     * @return true if the input is "j", false, if the input is "n"
     */
    private boolean sort() {
        System.out.println("Wollen Sie sortieren?");
        System.out.print("Ja [j], Nein [n]: ");
        while (true) {
            switch (in.nextLine().toLowerCase(Locale.ROOT)) {
                case "n":
                    return false;
                case "j":
                    return true;
                default:
                    System.out.println("Geben Sie [j] für ja und [n] für nein ein!");
            }
        }
    }
}
