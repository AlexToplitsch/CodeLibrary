package com.company;

import java.util.Locale;
import java.util.Scanner;

public class Calculator {
    private static final Scanner in = new Scanner(System.in);
    private static int MAX_DECIMAL_POINTS;


    public static void main() {
        setMaxDecimalPoints();
        while (true) {
            System.out.println("###################### Rechner #######################");
            System.out.print("Abbrechen? [J/N]: ");
            switch (in.nextLine().toLowerCase(Locale.ROOT)) {
                case "j":
                    return;
                case "n":
                    float[] values = valuesInput();
                    calculate(values[0], values[1]);
                    break;
                default:
                    System.out.println("Geben Sie 'J' für ja oder 'N' für Nein ein! \n");
            }
        }
    }

    /**
     * Sets the maximum decimal points of the result
     **/
    private static void setMaxDecimalPoints() {
        System.out.print("Geben Sie die maximalen Nachkommastellen ein:");
        String value = in.nextLine();
        while (isNotInt(value) || value.length() > 1 || Integer.parseInt(value) > 8 && Integer.parseInt(value) < 0) {
            System.out.print("Geben Sie nur eine Ziffer (1-8) ein!");
            value = in.nextLine();
        }
        MAX_DECIMAL_POINTS = Integer.parseInt(value);
    }

    /**
     * Takes two float numbers, operates an arithmetical operation  depending on the
     * operand, that was given in the commandline and  calls the method that writes it in the terminal
     *
     * @param a left number of the operand
     * @param b right number of the operand
     */
    private static void calculate(float a, float b) {
        float result = 0;
        boolean calculated;
        System.out.print("Geben Sie einen Operator ein: ");
        String op;
        do {
            calculated = true;
            op = in.nextLine();
            switch (op) {
                case "+": {
                    result = ArithmeticOperations.ADD.calc(a, b);
                    break;
                }
                case "-": {
                    result = ArithmeticOperations.SUB.calc(a, b);
                    break;
                }
                case "*": {
                    result = ArithmeticOperations.MULTI.calc(a, b);
                    break;
                }
                case "/": {
                    try {
                        result = ArithmeticOperations.DIV.calc(a, b);
                    } catch (ArithmeticException e) {
                        System.out.println(e.getMessage());
                    }
                    break;
                }
                default:
                    System.out.println("Kein Gültiger Operator!");
                    calculated = false;
            }
        } while (!calculated);

        printResult(a, b, result, op);
    }

    /**
     * Writes the result of the operation in the terminal
     *
     * @param a left number of operand
     * @param b right number of operand
     * @param result  result of the operation
     * @param operand operand of the operation
     *
     */
    private static void printResult(float a, float b, float result, String operand) {
        System.out.println(a + operand + b + " = " + round(result));
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
        while (isNotNumeric(value)) {
            System.out.print("Bitte geben Sie nur eine Zahl ein: ");
            value = in.nextLine();
        }
        values[0] = Float.parseFloat(value);

        // second value
        System.out.print("Geben Sie die zweite Zahl ein: ");
        value = in.nextLine();
        while (isNotNumeric(value)) {
            System.out.print("Bitte geben Sie nur eine Zahl ein: ");
            value = in.nextLine();
        }
        values[1] = Float.parseFloat(value);


        return values;
    }

    /**
     * Checks if the String str is can be converted into float
     *
     * @param str String that is gonna be checked
     * @return boolean
     */
    private static boolean isNotNumeric(String str) {
        if (str == null) {
            return true;
        }
        try {
            Float.parseFloat(str);
            return false;
        } catch (NumberFormatException throwable) {
            return true;
        }
    }

    /**
     * Rounds the float i with max decimal points
     * @param i float that has to be rounded
     */
    private static float round(float i) {
        float d = (float) Math.pow(10, MAX_DECIMAL_POINTS);
        return Math.round(i * d) / d;
    }

    /**
     * Checks if the String str is can be converted into int
     *
     * @param str String that is gonna be checked
     * @return boolean
     */
    private static boolean isNotInt(String str) {
        if (str == null) {
            return true;
        }
        try {
            Integer.parseInt(str);
            return false;
        } catch (NumberFormatException throwable) {
            return true;
        }
    }
}
