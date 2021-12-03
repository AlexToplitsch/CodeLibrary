package menu;
//TODO: Menu gestalten für einlesen von indizes für Sheet, Row und Zelle
//todo: Sortieren mit comparator
import excel.beans.row.ExcelRowBeans;
import excel.reader.ExcelReader;
import menu.filechooser.MyFileChooser;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

import javax.swing.*;
import java.io.IOException;
import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Scanner;

public class ExcelMenu {
    //######################### Properties ###########################
   private  String filePath;
    private ExcelReader reader;
    private ArrayList<ExcelRowBeans> rows;
    Logger logger = LogManager.getLogger(ExcelMenu.class);
    Scanner in = new Scanner(System.in);

    //######################### Constructor #########################
    public ExcelMenu() {
        run();
    }

    //######################### Functions ###########################

    /**
     *
     */
    private void run() {
        choseFile();
        createRowObjects();
    }

    /**
     *
     */
    private void choseFile(){
        MyFileChooser mychooser = new MyFileChooser("C:\\", false);
        mychooser.setFileFilter("Excel", "xls");
        JFileChooser chooser = mychooser.getChooser();
        int closeOption = chooser.showOpenDialog(null);
        if(closeOption == JFileChooser.APPROVE_OPTION){
            filePath = chooser.getSelectedFile().getAbsolutePath();
        }
    }

    private void createRowObjects(){
        reader = new ExcelReader(filePath);
        try {
            reader.init(0,0,0);
        } catch (IOException e) {
            logger.error("Error: " + e.getMessage());
        }
        reader.createRowList();
         rows = reader.getRows();
    }

    private void chooseSortIndex(){
        logger.info("Nach welcher Spalte wollen Sie sortieren?");
        logger.info("ID Zeile: [0], $Projektbezeichnung: [1], Zeilenbezeichnung: [2], Start: [3], Prozent Fretigstellung: [4]," +
                " Datum Endfixierung: [5], Abteilung: [6], Bemerkung:  [7]");
        while(true){
            switch (in.nextLine()){
                case "0":
                    return;
                case "1":
                    return;
                case "2":
                    return;
                case "3":
                    return;
                case "4":
                    return;
                case "5":
                    return;
                case "6":
                    return;
                case "7":
                    return;
                default:
                    logger.info("Geben Sie eine Zahl zwischen 0 und 7 ein!");
            }
        }
    }
}
