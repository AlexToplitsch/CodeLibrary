package com.company;

import java.util.Locale;
import java.util.Scanner;

public class Menu {
    private static final MyFileWriter writer = new MyFileWriter();
    private static final Scanner in = new Scanner(System.in);
    private static Calculator calc;

    public static void main() {
        selectPath();
        selectFilename();
        initCalculator();

        while (true) {
            System.out.println("###################### Rechner #######################");
            System.out.print("Abbrechen? [J/N]: ");
            switch (in.nextLine()
                      .toLowerCase(Locale.ROOT)) {
                case "j":
                    return;
                case "n":
                    float[] values = valuesInput();
                    operandInput(values[0], values[1]);
                    break;
                default:
                    System.out.println("Geben Sie 'J' für Ja oder 'N' für Nein ein! \n");
            }
        }
    }

    /**
     * Reads the path from the command line and hands it to the FileWriter class. Will be
     * repeated as long as the path is not valid!
     **/
    private static void selectPath() {
        System.out.print("Geben Sie den Dateipfad ohne Datei ein: ");

        while (!writer.setPath(in.nextLine())) {
            System.out.println("Der Pfad ist nicht gültig. Ein gültiger String sieht " + "folgendermaßen aus: 'D:\\path\\directory\\'");
        }
        if (!writer.pathExists()) {
            createPath();
        }
    }

    /**
     * Decision if the path should be created. If not selectPath is called again!
     */
    private static void createPath() {
        System.out.println("Pfad existiert nicht! Wollen Sie diesen erstellen? [J/N] ");
        while (true) {
            switch (in.nextLine()
                      .toLowerCase(Locale.ROOT)) {
                case "j":
                    writer.createDirectories();
                    return;
                case "n":
                    selectPath();
                    return;
                default:
                    System.out.println("Geben Sie 'J' für Ja oder 'N' für Nein ein! ");
            }
        }
    }

    /**
     * Reads the filename from the command line and hands it to the FileWriter class. Will be
     * repeated as long as the filename is not valid!
     **/
    private static void selectFilename() {
        System.out.print("Geben Sie nun den Dateinamen mit der Endung 'txt' ein: ");

        while (!writer.setFilename(in.nextLine())) {
            System.out.println("Der Dateiname ist ungültig! Folgende Zeichen" + " dürfen nicht enthalten sein: " + "\n?, *, |, <, >, \\, /, : ");
        }
    }

    /**
     * Sets the maximum decimal points of the result
     **/
    private static void initCalculator() {
        System.out.print("Geben Sie die maximalen Nachkommastellen ein: ");
        String value = in.nextLine();
        while (Calculator.isNotInt(value) || value.length() > 1 || Integer.parseInt(value) > 8 && Integer.parseInt(value) < 0) {
            System.out.print("Geben Sie nur eine Ziffer (1-8) ein!");
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
        System.out.print("Geben Sie die erste Zahl ein: ");
        value = in.nextLine();
        while (Calculator.isNotNumeric(value)) {
            System.out.print("Bitte geben Sie nur eine Zahl ein: ");
            value = in.nextLine();
        }
        values[0] = Float.parseFloat(value);

        // second value
        System.out.print("Geben Sie die zweite Zahl ein: ");
        value = in.nextLine();
        while (Calculator.isNotNumeric(value)) {
            System.out.print("Bitte geben Sie nur eine Zahl ein: ");
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
        System.out.print("Geben Sie einen Operator ein: ");
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
                    System.out.println("Kein Gültiger Operator!");
                    calculated = false;
            }
        } while (!calculated);
        try {
            printResult(a, b, calc.calculate(operation, a, b), op);
        } catch (NullPointerException throwable) {
            System.out.println("\n");
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
        System.out.println(equation);
        saveInFile(equation);
    }

    /**
     * Calls the Function of the FileWriter class that saves the equation in a txt file.
     *
     * @param str The equation as String that will be saved
     */
    private static void saveInFile(String str) {
        System.out.print("Wollen Sie die Gleichung in der Datei " + writer.getPath() + writer.getFilename() + " speichern? [J/N] ");
        boolean notSaved = true;
        while (notSaved) {
            notSaved = false;
            switch (in.nextLine()
                      .toLowerCase(Locale.ROOT)) {
                case "j":
                    try {
                        writer.writeToFile(str);
                    } catch (java.io.IOException throwable) {
                        System.out.println("Gleichung  konnte nicht gespeichert werden!\n" + "Fehler: " + throwable.getMessage());
                    }
                    break;
                case "n":
                    return;
                default:
                    System.out.println("Geben Sie 'J' für Ja oder 'N' für Nein ein! \n");
                    notSaved = true;
            }
        }
    }
}
