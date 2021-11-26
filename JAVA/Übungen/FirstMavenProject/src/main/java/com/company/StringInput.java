package com.company;

import java.util.Scanner;

public class StringInput {
    Scanner in;
    private String input;

    // constructor
    public StringInput(Scanner in) {
        this.in = in;
    }

    // functions

    /**
     * Concatenates the input string with "Hello"  and returns it
     * if input equals exit, than it returns only the input String
     *
     * @return String
     */
    public String getString() {
        if (input.equalsIgnoreCase("exit")) {
            return input;
        }
        return "Hello " + input;
    }

    /**
     * Reads one line from the console and puts it into input
     * variable
     */
    public void setString() {
        input = in.nextLine();
    }

}
