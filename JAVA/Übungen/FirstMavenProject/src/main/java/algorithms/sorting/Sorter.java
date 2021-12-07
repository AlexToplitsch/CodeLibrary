package algorithms.sorting;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.Random;

public class Sorter {
    //######################### Properties ###################################
    private static final Logger log = LogManager.getLogger(Sorter.class);


    //######################### Constructor ###################################
    public Sorter() {

    }


    //######################### Functions ###################################

    /**
     * Calls the recursive sort function
     *
     * @param a   The array that will be sorted
     * @param c   The comparator, that compares two values
     * @param <T> Type of the array and the Comparator functions
     */
    public static <T> void sort(T[] a, Comparator<? super T> c) {
        try {
            recSort(a, c, 0, a.length - 1);
        } catch (StackOverflowError e) {
            log.error("Error: " + e.getMessage());
            log.error(e.getMessage());
        }
    }

    /**
     * Recursive function
     *
     * @param a   The array that will be sorted
     * @param c   The comparator, that compares two values
     * @param l   The index of the first element of the partition
     * @param r   The index of the last element of the partition
     * @param <T> Type of the array and the Comparator functions
     */
    private static <T> void recSort(T[] a, Comparator<? super T> c, int l, int r) {
        int q;
        if (l < r) {
            q = partition(a, c, l, r);
            recSort(a, c, l, q);
            recSort(a, c, q + 1, r);
        }
    }

    /**
     * Sorts the array by using the passed comparator
     *
     * @param a   The array that will be sorted
     * @param c   The comparator, that compares two values
     * @param l   The index of the first element of the partition
     * @param r   The index of the last element of the partition
     * @param <T> Type of the ArrayList and the Comparator functions
     * @return The index of the pivot element
     * @throws StackOverflowError if the stack overflows
     */
    private static <T> int partition(T[] a, Comparator<? super T> c, int l, int r) throws
            StackOverflowError {
        int i, j;
        T x;
        x = getPivot(a, l, r - l);
        i = l - 1;
        j = r + 1;
        while (true) {
            do {
                i++;
            } while (i < a.length && c.compare(x, a[i]) > 0);
            do {
                j--;
            } while (j > -1 && c.compare(x, a[j]) < 0);

            if (i < j) {
                T k = a[i];
                a[i] = a[j];
                a[j] = k;
            } else {
                return j;
            }
        }
    }

    /**
     * @param a             The array to get the pivot from
     * @param startIndex    Start index of the partition
     * @param partitionSize Size of the partition
     * @param <T>           Type of the ArrayList and the Comparator functions
     * @return The pivot element
     */
    private static <T> T getPivot(T[] a, int startIndex, int partitionSize) {
        return a[startIndex + new Random().nextInt(partitionSize)];
        //return a.get(startIndex);
    }


    /**
     * Calls the recursive sort function
     *
     * @param a   The ArrayList that will be sorted
     * @param c   The comparator, that compares two values
     * @param <T> Type of the ArrayList and the Comparator functions
     */
    public static <T> void sort(ArrayList<T> a, Comparator<? super T> c) {
        try {
            recSort(a, c, 0, a.size() - 1);
        } catch (StackOverflowError e) {
            log.error("Error: " + e.getMessage());
            log.error(e.getMessage());
        }
    }

    /**
     * Recursive function
     *
     * @param a   The ArrayList that will be sorted
     * @param c   The comparator, that compares two values
     * @param l   The index of the first element of the partition
     * @param r   The index of the last element of the partition
     * @param <T> Type of the ArrayList and the Comparator functions
     */
    private static <T> void recSort(ArrayList<T> a, Comparator<? super T> c, int l, int r) throws StackOverflowError {
        int q;
        if (l < r) {
            q = partition(a, c, l, r);
            recSort(a, c, l, q);
            recSort(a, c, q + 1, r);
        }
    }

    /**
     * Sorts the ArrayList by using the passed comparator
     *
     * @param a   The ArrayList that will be sorted
     * @param c   The comparator, that compares two values
     * @param l   The index of the first element of the partition
     * @param r   The index of the last element of the partition
     * @param <T> Type of the ArrayList and the Comparator functions
     * @return The index of the pivot element
     * @throws StackOverflowError if the stack overflows
     */
    private static <T> int partition(ArrayList<T> a, Comparator<? super T> c, int l, int r) throws
            StackOverflowError {
        int i, j;
        T x;
        x = getPivot(a, l, r - l);
        i = l - 1;
        j = r + 1;
        while (true) {
            do {
                i++;
            } while (i < a.size() && c.compare(x, a.get(i)) > 0);
            do {
                j--;
            } while (j > -1 && c.compare(x, a.get(j)) < 0);

            if (i < j) {
                T k = a.get(i);
                a.set(i, a.get(j));
                a.set(j, k);
            } else {
                return j;
            }
        }
    }

    /**
     * @param a             The ArrayList to get the pivot from
     * @param startIndex    Start index of the partition
     * @param partitionSize Size of the partition
     * @param <T>           Type of the ArrayList and the Comparator functions
     * @return The pivot element
     */
    private static <T> T getPivot(ArrayList<T> a, int startIndex, int partitionSize) {
        return a.get(startIndex + new Random().nextInt(partitionSize));
        //return a.get(startIndex);
    }
}
