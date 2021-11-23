using System;
using System.Collections.Generic;
using System.Text;

namespace Algorithmen
{
    public static class Suchalgorithmen
    {
        private static bool CheckZero(int n)
        {
            if (n == 0)
            {
                return true;
            }
            return false;
        }

        public static int LinearSearch(int[] arr, int number, bool sorted = true)
        /*Sucht in dem übergebenen Integer Array nach der übergebenen Nummer*/
        {
            for (int i = 0; i < arr.Length; i++)
            {
                if(arr[i] == number)
                {
                    return i + 1;
                }
            }

            return -1;
        }

        public static int BinarySearch(int[] arr, int number)
        {
            return BinarySearch_Rekursiv(arr, number, 0, arr.Length - 1);
        }
        private static int BinarySearch_Rekursiv(int[] arr, int number, int start, int end)
        /*Sucht in dem übergebenen Integer Array nach der übergebenen Nummer*/
        {

            int middle = (start + end) / 2;
            
            if(arr[middle] == number)
            {
                return middle + 1;
            }

            else if (arr[middle] < number)
            {
                return BinarySearch_Rekursiv(arr, number, middle + 1, end);
            }
            else
            {
                return BinarySearch_Rekursiv(arr, number, start, middle - 1);
            }
            
        }

        public static int JumpSearch(int[] arr, int number)
        /*Sucht in dem übergebenen Integer Array nach der übergebenen Nummer*/
        {
            int jump = Convert.ToInt32(Math.Sqrt(arr.Length));

            for(int i = 0; i < arr.Length; i += jump)
            {
                try
                {
                    if (arr[i] > number)
                    {
                        for (int j = i; j >= i -  jump; j--)
                        {
                            if(arr[j] == number)
                            {
                                return j + 1;
                            }
                            if(j == i - jump)
                            {
                                return -1;
                            }
                        }
                    }
                }

                catch (Exception)
                {
                    if (arr[arr.Length - 1] > number)
                    {
                        for (int j = arr.Length - 1; j >= arr.Length - 1 - jump; j--)
                        {
                            if (arr[j] == number)
                            {
                                return j + 1;
                            }
                            else
                            {
                                return -1;
                            }
                        }
                    }
                } 
            }

            return -1;
        }

        private static int BinaryStartNumbr(int length)
        {
            if (length % 2 == 0)
            {
               return length / 2;
            }

            else
            {
                return length / 2 + 1;
            }
        }
    }
}
