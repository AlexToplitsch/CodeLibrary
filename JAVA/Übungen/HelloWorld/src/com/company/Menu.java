package com.company;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

import javax.swing.*;
import javax.swing.filechooser.FileNameExtensionFilter;
import java.io.File;
import java.util.Locale;
import java.util.Scanner;


public class Menu {
    private static final Logger logger = LogManager.getLogger(Menu.class);
    private static final MyFileWriter writer = new MyFileWriter();
    private static final Scanner in = new Scanner(System.in);
    private static Calculator calc;

    public static void main() {
        if(!selectFile()) {
            return;
        }
        initCalculator();

        while (true) {

            logger.info("###################### Rechner #######################");
            logger.info("Abbrechen? [J/N]: ");
            switch (in.nextLine()
                      .toLowerCase(Locale.ROOT)) {
                case "j":
                    return;
                case "n":
                    float[] values = valuesInput();
                    operandInput(values[0], values[1]);
                    break;
                default:
                    logger.info("Geben Sie 'J' für Ja oder 'N' für Nein ein! \n");
            }
        }
    }

    /**
     * Opens the JFileChooser and sets the path and the filename in writer Object
     * If the path or the file is not valid it reopens the file chooser. If the FileChooser option equals
     * CANCEL_OPTION
     */
    private static boolean selectFile() {
        JFileChooser chooser = new JFileChooser("D:\\");
        // Window settings
        chooser.setFileSelectionMode(JFileChooser.FILES_ONLY);
        chooser.setFileFilter(new FileNameExtensionFilter("Text files", "txt"));
        chooser.setAcceptAllFileFilterUsed(false);

        int option = chooser.showOpenDialog(null); // how the FileChooser was closed
        // if the open button is clicked
        if (option == JFileChooser.APPROVE_OPTION) {
            File f = chooser.getSelectedFile();
            if(!writer.setFilePath(f.getAbsolutePath())){
                selectFile();
            }
            return true;
        }
        else if (option == JFileChooser.CANCEL_OPTION) {
            logger.info("See ya later!");
        }
        else{
            logger.info("Error: Error at file choosing!");
        }
        return false;

    }

    /**
     * Sets the maximum decimal points of the result
     **/
    private static void initCalculator() {
        logger.info("Geben Sie die maximalen Nachkommastellen ein: ");
        String value = in.nextLine();
        while (Calculator.isNotInt(value) || value.length() > 1 || Integer.parseInt(value) > 8 && Integer.parseInt(value) < 0) {
            logger.info("Geben Sie nur eine Ziffer (1-8) ein!");
            value = in.nextLine();
        }

        calc = new Calculator(Integer.parseInt(value));
    }

    /**
     * Reads two values from the terminal, converts these into float types and returns them in
     * an array with two fields.
     *
     * @return float[]
     */
    private static float[] valuesInput() {
        float[] values = new float[2];
        String value;

        // first value
        logger.info("Geben Sie die erste Zahl ein: ");
        value = in.nextLine();
        while (Calculator.isNotNumeric(value)) {
            logger.info("Bitte geben Sie nur eine Zahl ein: ");
            value = in.nextLine();
        }
        values[0] = Float.parseFloat(value);

        // second value
        logger.info("Geben Sie die zweite Zahl ein: ");
        value = in.nextLine();
        while (Calculator.isNotNumeric(value)) {
            logger.info("Bitte geben Sie nur eine Zahl ein: ");
            value = in.nextLine();
        }
        values[1] = Float.parseFloat(value);
        return values;
    }

    /**
     * Takes two float numbers, operates an arithmetical operation  depending on the
     * operand, that was given in the commandline and  calls the method that writes it in the terminal
     *
     * @param a left number of the operand
     * @param b right number of the operand
     */
    private static void operandInput(float a, float b) {
        boolean calculated;
        logger.info("Geben Sie einen Operator ein: ");
        String op;
        ArithmeticOperations operation = ArithmeticOperations.ADD;

        do {
            calculated = true;
            op = in.nextLine();
            switch (op) {
                case "+": {
                    operation = ArithmeticOperations.ADD;
                    break;
                }
                case "-": {
                    operation = ArithmeticOperations.SUB;
                    break;
                }
                case "*": {
                    operation = ArithmeticOperations.MULTI;
                    break;
                }
                case "/": {
                    operation = ArithmeticOperations.DIV;
                    break;
                }
                default:
                    logger.info("Kein Gültiger Operator!");
                    calculated = false;
            }
        } while (!calculated);
        try {
            printResult(a, b, calc.calculate(operation, a, b), op);
        } catch (NullPointerException throwable) {
            logger.info("\n");
        }

    }

    /**
     * Writes the result of the operation in the terminal
     *
     * @param a       left number of operand
     * @param b       right number of operand
     * @param result  result of the operation
     * @param operand operand of the operation
     */
    private static void printResult(float a, float b, float result, String operand) {
        String equation = a + " " + operand + " " + b + " = " + result;
        logger.info(equation);
        saveInFile(equation);
    }

    /**
     * Calls the Function of the FileWriter class that saves the equation in a txt file.
     *
     * @param str The equation as String that will be saved
     */
    private static void saveInFile(String str) {
        logger.info("Wollen Sie die Gleichung in der Datei " + writer.getPath() + writer.getFilename() + " speichern? [J/N] ");
        boolean notSaved = true;
        while (notSaved) {
            notSaved = false;
            switch (in.nextLine()
                      .toLowerCase(Locale.ROOT)) {
                case "j":
                    try {
                        writer.writeToFile(str, logger);
                    } catch (java.io.IOException throwable) {
                        logger.error("Gleichung  konnte nicht gespeichert werden!\n" + "Fehler: " + throwable.getMessage());
                    }
                    break;
                case "n":
                    return;
                default:
                    logger.info("Geben Sie 'J' für Ja oder 'N' für Nein ein! \n");
                    notSaved = true;
            }
        }
    }
}
