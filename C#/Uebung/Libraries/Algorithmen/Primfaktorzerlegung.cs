using System;
using System.Collections.Generic;
using System.Text;

namespace Algorithmen
{
    public static class Primfaktorzerlegung
    {
        public static string GetPrimenumbers(int n)
        {
            if (!IsNumberValid(n))
            {
                return "Zahl nicht teilbar!";
            }
            return ConvertListToString(n);

        }

        public static bool IsPrimenumber(int n)
        {
            if (!IsNumberValid(n))
            {
                return false;
            }

            for(int i = 2; i < Math.Sqrt(n) + 1; i++)
            {
                if (n % i == 0 && n != 2) { return false; }
                if(i > 2) { i++; }
            }
            return true;          
        }

        public static List<int> ListOfPrimenumbers(int n)
        {

            List<int> primenumbers = new List<int>();

            if (!IsNumberValid(n))
            {
                return primenumbers;
            }
            if (n < 0)
            {
                n = SwitchSign(n);
            }


            int[] arr = MakeIntArray(n);

            foreach (int number in arr)
            {
                if (IsPrimenumber(number))
                {
                    primenumbers.Add(number);
                }
            }
            return primenumbers;
        }


        private static string ConvertListToString(int n)
        {
            string pf = "";
            if (n < 0)
            {
                n = SwitchSign(n);
                pf += "(-1) * ";
            }
            List<List<int>> liste = CalculatePrimenumbers(n);
            foreach(List<int>prime in liste)
            {
                pf += Convert.ToString(prime[0]) + "^" + Convert.ToString(prime[1])+ " * " ;
            }
            return pf[0..^3]; //gibt einen gewissen Bereich des Strings aus(in dem Fall von index 0 bis -3)
        }

        public static List<List<int>> CalculatePrimenumbers(int n)
        {
            if (!IsNumberValid(n))
            {
                return new List<List<int>> { };
            }

            if (n < 0)
            {
                n = SwitchSign(n);
            }

            List<List<int>> primenumbers= new List<List<int>>();
            int number = n;
            int primenumber = 2;



            while(number > 1)
            {
                int exponent = 0;
                List<int> numberAndExpo = new List<int>();
                while (number % primenumber == 0)
                {
                    number = number / primenumber;
                    exponent++;
                }
                if(exponent != 0)
                {
                    numberAndExpo.Add(primenumber);
                    numberAndExpo.Add(exponent);
                    primenumbers.Add(numberAndExpo);
                }

                if (primenumber > 2)
                {
                    primenumber++;
                }
                primenumber++;

            }
            return primenumbers;
        }

        private static int SwitchSign(int number)
        {
            return number * -1;
        }

        private static bool IsNumberValid(int n){
            if(n == 1 || n == 0)
            {
                return false;
            }


            return true;
        }

        private static int[] MakeIntArray(int n)
        {
            int[] arr = new int[n / 2];
            arr[0] = 2;

            int nubmer = 3;
            
            for(int i = 3; i < arr.Length; i++)
            {
                arr[i] = nubmer;
                nubmer += 2;
            }

            return arr;
        }
    }
}
