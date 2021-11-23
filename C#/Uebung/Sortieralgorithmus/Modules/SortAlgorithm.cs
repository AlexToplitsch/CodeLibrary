using System;
using System.Collections.Generic;
using System.Text;

namespace Sortieralgorithmus.Modules
{
    public static class  SortAlgorithm
    {

        public static int[] BubbleSort(int[] arr, bool increase = true)
        {
            
            if (increase == true)
            {
                int unsortedLength = arr.Length;
                for (int i = 0; i < arr.Length; i++)
                {
                    for (int j = 0; j < unsortedLength - 1; j++)
                    {
                        if (arr[j] > arr[j + 1])
                        {
                            int temp = arr[j + 1];
                            arr[j + 1] = arr[j];
                            arr[j] = temp;
                        }
                    }
                    unsortedLength = unsortedLength - 1;
                    if (unsortedLength == 0)
                    {
                        break;
                    }
                }
            }

            else
            {
                int unsortedLength = 0;
                for (int i = arr.Length - 1; i > 0; i--)
                {
                    for (int j = arr.Length - 1; j > unsortedLength; j--)
                    {
                        if (arr[j] > arr[j - 1])
                        {
                            int temp = arr[j - 1];
                            arr[j - 1] = arr[j];
                            arr[j] = temp;
                        }
                    }
                    unsortedLength = unsortedLength + 1;
                    if (unsortedLength == arr.Length)
                    {
                        break;
                    }
                }
            }

            return arr;
        }

        public static int[] InsertionSort(int[] arr, bool increase = true)
        {
            if(increase == true)
            {
                for (int i = 1; i < arr.Length; i++)
                {
                    int temp = arr[i];
                    for (int j = i; j >= 0; j--)
                    {
                        if (j == 0)
                        {
                            arr[j] = temp;
                            break;
                        }
                        else if (temp > arr[j - 1])
                        {
                            arr[j] = temp;
                            break;
                        }
                        else
                        {
                            arr[j] = arr[j - 1];
                        }
                    }
                }
            }
            else
            {
                for (int i = 1; i < arr.Length; i++)
                {
                    int temp = arr[i];
                    for (int j = i; j >= 0; j--)
                    {
                        if (j == 0)
                        {
                            arr[j] = temp;
                            break;
                        }
                        else if (temp < arr[j - 1])
                        {
                            arr[j] = temp;
                            break;
                        }
                        else
                        {
                            arr[j] = arr[j - 1];
                        }
                    }
                }
            }

            return arr;
        }

        public static int[] SelectionSort(int[] arr, bool increase = true)
        {
            int lowestIndex; //the index of the lowest value in the array

            if (increase == true)
            {
                for(int i = 0; i < arr.Length; i++)
                {
                    lowestIndex = i;
                    for (int j = i; j < arr.Length; j++)
                    {
                        if(arr[lowestIndex] > arr[j])
                        {
                            lowestIndex = j;
                        }
                    }
                    int temp = arr[i];
                    arr[i] = arr[lowestIndex];
                    arr[lowestIndex] = temp;
                }
            }

            else
            {
                for (int i = arr.Length - 1; i >= 0; i--)
                {
                    lowestIndex = i;
                    for (int j = i; j >= 0; j--)
                    {
                        if (arr[lowestIndex] > arr[j])
                        {
                            lowestIndex = j;
                        }
                    }
                    int temp = arr[i];
                    arr[i] = arr[lowestIndex];
                    arr[lowestIndex] = temp;
                }
            }

            return arr;
        }
    }
}
