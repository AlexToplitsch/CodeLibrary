package com.company;


public class Calculator {

    private static int MAX_DECIMAL_POINTS;

    public Calculator(int maxDecimalPoints) {
        MAX_DECIMAL_POINTS = maxDecimalPoints;
    }

    /**
     * Takes two float numbers, operates an arithmetical operation  depending on the
     * operand, that was given in the commandline and  calls the method that writes it in the terminal
     *
     * @param a left number of the operand
     * @param b right number of the operand
     */
    public Float calculate(ArithmeticOperations op, float a, float b) {
        try {
            return round(op.calc(a, b));
        } catch (ArithmeticException throwable) {
            System.out.println(throwable.getMessage());
            return null;
        }
    }


    /**
     * Checks if the String str is can be converted into float
     *
     * @param str String that is gonna be checked
     * @return boolean
     */
    public static boolean isNotNumeric(String str) {
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
     *
     * @param i float that has to be rounded
     */
    private float round(float i) {
        float d = (float) Math.pow(10, MAX_DECIMAL_POINTS);
        return Math.round(i * d) / d;
    }

    /**
     * Checks if the String str is can be converted into int
     *
     * @param str String that is gonna be checked
     * @return boolean
     */
    public static boolean isNotInt(String str) {
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
