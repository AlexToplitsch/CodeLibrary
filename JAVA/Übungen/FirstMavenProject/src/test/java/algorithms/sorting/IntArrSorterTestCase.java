package algorithms.sorting;

import org.junit.Test;

import static junit.framework.TestCase.assertEquals;

public class IntArrSorterTestCase {
    private final int[] case1 = new int[]{7,8,4,2,5,9,4,6,7,4,5,4,9,19,20,15,16,71,15};
    private final int[] resAsc1 = new int[] {2,4,4,4,4,5,5,6,7,7,8,9,9,15,15,16,19,20,71};
    private final int[] resDesc1 = new int[] {71,20,19,16,15,15,9,9,8,7,7,6,5,5,4,4,4,4,2};
    private final int[] case2 = new int[]{456,-9,-10,1025,789,15,12,15,13,12,5,-5,7,9,10,
            -9,-12,10123,1024,-9,-9,8,123,10111,1023};
    private final int[] resAsc2 = new int[]{-12,-10,-9,-9,-9,-9,-5,5,7,8,9,10,12,12,13,15,15,123,
            456,789,1023,1024,1025,10111,10123};
    private final int [] resDesc2 = new int[] {10123,10111,1025,1024,1023,789,456,123,15,
            15,13,12,12,10,9,8,7,5,-5,-9,-9,-9,-9,-10,-12};
    IntArrSorter intArrSorter = new IntArrSorter(case1.clone(), true);

    /**
     * Testcase with firstPivot true and ascending order of an integer array
     */
    @Test
    public void ascSortFirstPivot1(){
        intArrSorter.setIntArr(case1.clone());
        int[] res = intArrSorter.sort(false);
        assertEquals(arrayToString(resAsc1), arrayToString(res));
    }

    /**
     * Testcase with firstPivot true and descending order of an integer array
     */
    @Test
    public void descSortFirstPivot1(){
        intArrSorter.setIntArr(case1.clone());
        int[] res = intArrSorter.sort(true);
        assertEquals(arrayToString(resDesc1), arrayToString(res));
    }

    /**
     * Testcase with firstPivot false and ascending order of an integer array
     */
    @Test
    public void ascSortRandomPivot1(){
        intArrSorter.setIntArr(case1.clone());
        intArrSorter.setFirstPivot(false);
        int[] res = intArrSorter.sort(false);
        assertEquals(arrayToString(resAsc1), arrayToString(res));
    }

    /**
     * Testcase with firstPivot false and descending order of an integer array
     */
    @Test
    public void descSortRandomPivot1(){
        intArrSorter.setIntArr(case1.clone());
        intArrSorter.setFirstPivot(false);
        int[] res = intArrSorter.sort(true);
        assertEquals(arrayToString(resDesc1), arrayToString(res));
    }

    @Test
    public void ascSortFirstPivot2(){
        intArrSorter.setIntArr(case2.clone());
        int[] res = intArrSorter.sort(false);
        assertEquals(arrayToString(resAsc2), arrayToString(res));
    }

    /**
     * Testcase with firstPivot true and descending order of an integer array
     */
    @Test
    public void descSortFirstPivot2(){
        intArrSorter.setIntArr(case2.clone());
        int[] res = intArrSorter.sort(true);
        assertEquals(arrayToString(resDesc2), arrayToString(res));
    }

    /**
     * Testcase with firstPivot false and ascending order of an integer array
     */
    @Test
    public void ascSortRandomPivot2(){
        intArrSorter.setIntArr(case2.clone());
        intArrSorter.setFirstPivot(false);
        int[] res = intArrSorter.sort(false);
        assertEquals(arrayToString(resAsc2), arrayToString(res));
    }

    /**
     * Testcase with firstPivot false and descending order of an integer array
     */
    @Test
    public void descSortRandomPivot2(){
        intArrSorter.setIntArr(case2.clone());
        intArrSorter.setFirstPivot(false);
        int[] res = intArrSorter.sort(true);
        assertEquals(arrayToString(resDesc2), arrayToString(res));
    }



    /**
     * Converts the passed array to a String.
     * @param arr The array the that will be formatted as String
     * @return String: Every index of the passed array with the pattern as follows [1,2,4,5,...]
     */
    public String arrayToString(int[] arr){
        StringBuilder str = new StringBuilder();
        str.append("[");
        for(int n : arr){
            str.append(n).append(",");
        }
        str.append("]");
        return str.toString();
    }
}
