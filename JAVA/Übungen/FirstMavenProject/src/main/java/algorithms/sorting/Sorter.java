package algorithms.sorting;

import java.util.Random;

import org.apache.logging.log4j.Logger;
import org.apache.logging.log4j.LogManager;

public class Sorter {
    // ##### Properties #####
    Logger LOG = LogManager.getLogger(Sorter.class);
    private int[] intArr;
    private int[] sortedIntArr;
    private boolean firstPivot;
    private boolean desc = false;


    // ##### Constructor #####
    public Sorter(int[] intArr, boolean firstPivot) {
        this.intArr = intArr;
        this.firstPivot = firstPivot;
        this.sortedIntArr = intArr.clone();
    }


    // ##### Getter/Setter #####
    public void setFirstPivot(boolean firstPivot) {
        this.firstPivot = firstPivot;
    }

    public void setIntArr(int[] arr) {
        this.intArr = arr;
        this.sortedIntArr = this.intArr;
    }

    public void setDesc(boolean desc) {
        this.desc = desc;
    }


    // ##### Functions #####

    /**
     * Sets the property desc and calls the recursive function for asc or desc quick sorting.
     *
     * @param desc If true, array will be sorted in descending order; if false, array will be
     *             sorted in ascending order;
     * @return int[]: The sorted int array;
     */
    public int[] sort(boolean desc) {
        int[] arr = intArr;
        try {
            this.desc = desc;
            arr = recSort(0, sortedIntArr.length - 1);
        } catch (StackOverflowError e) {
            LOG.error("Error: Stack overflow | " + e.getMessage());
            LOG.error("Zu viele Rekursionsaufrufe. Teilsortierte Liste wird zurückgegeben!");
        }
        return arr;
    }

    /**
     * Calls itself as long as the left index is smaller than the right index of the array
     *
     * @param l Left index of the array
     * @param r Right index of the array
     * @return The sorted Array
     */
    private int[] recSort(int l, int r) throws StackOverflowError {
        int q;
        if (l < r) {
            if (desc) {
                q = descPartition(l, r);
            } else {
                q = partition(l, r);
            }
            recSort(l, q);
            recSort(q + 1, r);
        }
        return sortedIntArr;
    }

    /**
     * Sorts the partition of an array in ascending order defined by the left and right indices and if the partition
     * is sorted it returns the right index on the updated position
     *
     * @param l left index that defines the size of the partition
     * @param r right index that defines the size of the partition
     * @return int: right index on its updated position after sorting the partition
     */
    private int partition(int l, int r) {
        int i, j, x;
        x = getPivot(l, r - l);
        i = l - 1;
        j = r + 1;
        while (true) {
            do {
                i++;
            } while (sortedIntArr[i] < x);
            do {
                j--;
            } while (sortedIntArr[j] > x);
            if (i < j) {
                int k = sortedIntArr[i];
                sortedIntArr[i] = sortedIntArr[j];
                sortedIntArr[j] = k;
            } else {
                return j;
            }
        }
    }

    /**
     * Sorts the partition of an array in descending order defined by the left and right indices and if the partition
     * is sorted it returns the right index on the updated position
     *
     * @param l left index that defines the size of the partition
     * @param r right index that defines the size of the partition
     * @return int: right index on its updated position after sorting the partition
     */
    private int descPartition(int l, int r) {
        int i, j, x;
        x = getPivot(l, r - l);
        i = l - 1;
        j = r + 1;
        while (true) {
            do {
                i++;
            } while (sortedIntArr[i] > x);
            do {
                j--;
            } while (sortedIntArr[j] < x);
            if (i < j) {
                int k = sortedIntArr[i];
                sortedIntArr[i] = sortedIntArr[j];
                sortedIntArr[j] = k;
            } else {
                return j;
            }
        }
    }

    /**
     * @param index the very left index of the partition
     * @param range the size of the partition
     * @return If firstPivot is true it returns the first element of the partition, else it returns a random
     * element of the partition
     */
    private int getPivot(int index, int range) {
        int x;
        if (firstPivot) {
            x = sortedIntArr[index];
        } else {
            x = sortedIntArr[index + new Random().nextInt(range)];
        }
        return x;
    }

    /**
     * Converts the passed integer array into a String.
     *
     * @param arr The array that will be converted
     * @return String: The array as String with pattern as follows [1,2,3,4,...]
     */
    public static String toString(int[] arr) {
        StringBuilder str = new StringBuilder();
        str.append("[");
        for (int n : arr) {
            str.append(n)
               .append(",");
        }
        str.append("]");
        return str.toString();
    }

    /**
     * Writes the sorted and unsorted array into a log file at D:\Development
     *
     * @param duration Duration of the sorting process
     */
    public void writeToFile(long duration) {
        String order = "Ascending";
        String pivot = "Random Pivot";
        if (desc) {
            order = "Descending";
        }
        if (firstPivot) {
            pivot = "First Pivot";
        }
        LOG.info("New Sorting Operation | Dauer: " + duration + "ms | " + "Reihenfolge: " + order + " | Stelle des Pivot-Elements: " + pivot + "\n" + toString(
                this.intArr) + "\n" + toString(this.sortedIntArr) + "\n\n");
    }
}
