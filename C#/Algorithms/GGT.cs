using System;
using System.Collections.Generic;
using System.Text;

namespace Algorithmen
{
    public static class GGT
    {
        public static int CalcggT(int[] arr)
        {   if(arr.Length == 1)
            {
                return arr[0];
            }
            return CalcggTRek(arr, arr[0], arr[1], 1);
        }

        private static int CalcggTRek(int[] arr, int a, int b, int index)
        {
            
            if (a < b) 
            {
                int temp = a;
                a = b;
                b = temp;
            }

            b = Calc(a, b);

            if (arr[^1] == arr[index]) 
            {   
                if(b < 0)
                {
                    b *= (-1);
                }
                return b;
            }
            index++;
            return CalcggTRek(arr, arr[index], b, index);
        }

        //public static int CalcKgV(int[] arr)
        //{
        //    List<List<List<int>>> liste = new List<List<List<int>>>();

        //    for(int i = 0; i < arr.Length; i++)
        //    {
        //        liste.Add(Primfaktorzerlegung.CalculatePrimenumbers(arr[i]));
        //    }

        //}

        //private static int CalcKgVRek()
        //{

        //}

        private static int Calc(int a, int b)
        {

            while (a % b != 0)
            {
                int rest = a % b;
                a = b;
                b = rest;
            }
            return b;
        }


    }
}
