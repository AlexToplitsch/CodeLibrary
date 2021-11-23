using System;
using System.Collections.Generic;
using System.Text;

namespace Algorithmen
{
    public static class StaticBarcode
    {

        private static int[] Convert_string_to_intarray(string barcode, int modulo)
        {
            int[] arr = new int[barcode.Length];

            for (int i = 0; i < barcode.Length; i++)
            {
                arr[i] = Convert.ToInt32(barcode[i]) - 48;
            }


            return arr;
        }


        private static int Calc_quersumme(string barcode, int modulo)
        {
            int[] arr = Convert_string_to_intarray(barcode, modulo);
            int quersumme = 0;
            int factor = 2;

            if (modulo == 11)
            {
                for (int i = arr.Length - 1; i >= 0; i--)
                {
                    quersumme += arr[i] * factor;
                    factor++;
                    if (factor > 7) { factor = 2; }
                }
            }
            else
            {
                for (int i = 0; i < arr.Length; i++)
                {
                    quersumme += arr[i];
                }
            }

            return quersumme;
        }


        private static int Calculate_PZ(string barcode, int modulo)
        {
            int quersumme = Calc_quersumme(barcode, modulo);
            return modulo - (quersumme % modulo);
        }


        private static string Set_PZ(string barcode, int modulo)
        {
            string pz = Convert.ToString(Calculate_PZ(barcode, modulo));
            if (modulo == 11)
            {
                pz = Replace_PZ(pz);
            }
            return pz;
        }

        private static string Replace_PZ(string n)
        {
            if (n == "10")
            {
                return "x";
            }
            else if (n == "11")
            {
                return "0";
            }
            return n;
        }
        public static string Get_Full_Barcode(string barcode, int modulo)
        {
            return barcode + Set_PZ(barcode, modulo);
        }

        //public static int Is_Barcode_Valid(string barcode, int modulo)
        //{
        //    if(barcode[^1] == 'x')
        //    {

        //    }
        //}
    }
}
