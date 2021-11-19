using System;

namespace Algorithmen
{
    public class ArrayCreater
    {
        private bool CheckZero(int n)
        {
            if (n == 0)
            {
                return true;
            }
            return false;
        }

        public int[] CreateArray(int length, int range)
        {
            if (CheckZero(length) == true || CheckZero(range) == true)
            {
                return new int[1] { -1 };
            }
            Random rnd = new Random();
            int n = length;
            int[] arr = new int[n];
            for (int i = 0; i < n; i++)
            {
                arr[i] = rnd.Next(1, range);
            }

            return arr;
        }

        public void PrintArray(int[] arr)
        {
            Console.Write("[");
            for (int i = 0; i < arr.Length; i++)
            {
                if (i == arr.Length - 1)
                {
                    Console.Write(arr[i]);
                    break;
                }
                Console.Write(arr[i] + ", ");
            }
            Console.Write("]");
            Console.WriteLine();
            Console.WriteLine();
            Console.WriteLine();
            Console.WriteLine();
        }

    }
}
