package com.company;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Calculator.main();
    }

    public static void runStringInput() {
        Scanner in = new Scanner(System.in);
        StringInput comReader = new StringInput(in);

        System.out.println("Geben Sie einen Text ein, " + "'exit' ein um die Schleife abzubrechen!");
        // Input loop
        while (true) {
            comReader.setString();

            // breaks the loop if  the user input equals "exit"
            if (comReader.getString().equalsIgnoreCase("exit")) {
                break;
            }
            System.out.println(comReader.getString() + "\n");

        }
    }
}
