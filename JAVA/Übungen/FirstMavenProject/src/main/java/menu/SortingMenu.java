package menu;


import algorithms.sorting.Sorter;
import arithmetic.operations.Calculator;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

import java.util.Random;
import java.util.Scanner;
import java.util.concurrent.ThreadLocalRandom;

public class SortingMenu {
    // ##### Properties #####
    private final int DEFAULT_SIZE = 10;
    private final Logger LOG = LogManager.getLogger(SortingMenu.class);
    private final Scanner in = new Scanner(System.in);
    int[] arr;


    // ##### Constructor #####
    public SortingMenu() {
        this.run();
    }


    // ##### Functions #####

    /**
     * Calls a bunch of functions initialises the Sorter, calls the function that sorts the array
     * and prints the unsorted and sorted array
     */
    private void run() {
        decideGenORInput();
        boolean desc = decideAscDesc();
        boolean firstPivot = decideFirstPivot();
        Sorter sorter = new Sorter(arr, firstPivot);
        long time = System.currentTimeMillis();
        sorter.sort(desc);
        time = System.currentTimeMillis() - time;
        LOG.info("Sortierdauer: " + time + "ms");
        sorter.writeToFile(time);
        time = System.currentTimeMillis();
        sorter.sort(desc);
        time = System.currentTimeMillis() - time;
        LOG.info("Sortierdauer: " + time + "ms");
    }

    /**
     * Reads the next line from the terminal and calls two functions depending on the input.
     * The user has to decide, if he wants to generate an random array or manually input the
     * numbers.
     */
    private void decideGenORInput() {
        LOG.info("Wollen Sie eine zufällige Liste generieren[g], oder " + "wollen Sie die Zahlen selbst eingeben[i]? ");
        while (true) {
            switch (in.nextLine()) {
                case "i":
                    inputArraySize();
                    manualInput();
                    return;
                case "g":
                    inputArraySize();
                    arrayMaker();
                    return;
                default:
                    LOG.info("Geben Sie [g] um zu generieren und [i] um selbst Zahlen einzufügen! ");
                    break;
            }
        }
    }

    /**
     * Reads the next line from the terminal. Lets the user decide if he wants to sort the Array
     * ascending or descending.
     *
     * @return boolean: True if descending; False if ascending
     */
    private boolean decideAscDesc() {
        LOG.info("Wollen Sie das Array aufsteingend[a] oder absteigend[d] sortieren?");
        while (true) {
            switch (in.nextLine()) {
                case "a":
                    return false;
                case "d":
                    return true;
                default:
                    LOG.info("Geben Sie [a] für aufsteigend und [d] für absteigend ein!");
                    break;
            }
        }
    }

    /**
     * Reads the next line from the terminal. Lets the user decide if he wants that the sorting
     * algorithm uses always the first element as pivot or a random element.
     *
     * @return boolean: True if first; False if random
     */
    private boolean decideFirstPivot() {
        LOG.info("Wollen Sie immer das erste[f] oder ein zufälliges[r]Element als Pivot-Element" + " nehmen?");
        while (true) {
            switch (in.nextLine()) {
                case "r":
                    return false;
                case "f":
                    return true;
                default:
                    LOG.info("Geben Sie [f] für das Erste und [r] für ein Zufälliges ein!");
                    break;
            }
        }
    }

    /**
     * Reads the next line from the Terminal, tries to parse it into integer and initialises the
     * array arr.
     * If an error has occurred, then the array size will be set to DEFAULT_SIZE
     */
    private void inputArraySize() {
        int length = DEFAULT_SIZE;
        LOG.info("Geben Sie die Länge des Arrays in einer Ganzzahl an: ");
        String input = in.nextLine();
        while (Calculator.isNotInt(input)) {
            LOG.info("Geben Sie eine Ganzzahl ein: ");
            input = in.nextLine();
        }
        try {
            length = Integer.parseInt(input);
        } catch (NumberFormatException e) {
            LOG.error("Ein Fehler ist aufgetreten! Array wird auf Standardgröße 10 gesetzt!");
            LOG.error("Error: Eingegebene Zahl für Integer zu groß!");
        }
        arr = new int[length];
    }

    /**
     * Reads the next line from the terminal, parses it into an integer
     * and stores it into the array.
     */
    private void manualInput() {

        LOG.info("Geben Sie nun nacheinander die Zahlen des Arrays ein!");
        for (int i = 0; i < arr.length; i++) {
            System.out.printf("%s > ", i);
            String input = in.nextLine();
            while (Calculator.isNotInt(input)) {
                LOG.info("Geben Sie eine Ganzzahl ein!");
                input = in.nextLine();
            }
            arr[i] = Integer.parseInt(input);
        }
    }

    /**
     * Creates Random int numbers for every index in the array and stores it in the array arr.
     */
    private void arrayMaker() {
        for (int i = 0; i < arr.length; i++) {
            arr[i] = ThreadLocalRandom.current().nextInt(arr.length*-1, arr.length);
        }
    }

    /**
     * Prints every element of the sorted array
     */
    private void printArray() {
        System.out.print("[");
        for (int n : arr) {
            System.out.printf("%s ", n);
        }
        System.out.print("]");
        System.out.println();
    }
}
