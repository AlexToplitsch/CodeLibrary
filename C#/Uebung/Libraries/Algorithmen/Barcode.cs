using System;
using System.Collections.Generic;
using System.Text;

namespace Algorithmen
{
    public class Barcode
    {

        public string Code { get; set; }
        private string PZ { get; set; }
        private bool Full { get; set; }
        private int Modulo { get; set; }
        private bool Mod11 { get; set; }

        public Barcode(string code, bool full = false, bool mod11 = false, int mod = 10)
        {
            Mod11 = mod11;
            if (!Mod11){ Modulo = mod; }
            else { Modulo = 11; }
            Full = full;

            if (Full)
            {
                Code = code[0..^1];
                PZ = Convert.ToString(code[^1]);
            }
            else
            {
                Code = code;
                Set_PZ();
            }
            
        }


        private int[] Convert_string_to_intarray()
        {
            int[] arr = new int[Code.Length];

            for (int i = 0; i < Code.Length; i++)
            {
                arr[i] = Convert.ToInt32(Code[i]) - 48;
            }


            return arr;
        }


        private int Calc_quersumme()
        {
            int[] arr = Convert_string_to_intarray();
            int quersumme = 0;
            int factor = 2;

            if (Mod11)
            {
                for (int i = arr.Length - 1; i >= 0; i--)
                {
                    quersumme += arr[i] * factor;
                    factor++;
                    if(factor > 7) { factor = 2; }
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


        private int Calculate_PZ()
        {
            int quersumme = Calc_quersumme();
            return Modulo - (quersumme % Modulo);
        }


        private void Set_PZ()
        {
            string pz = Convert.ToString(Calculate_PZ());
            if (Modulo == 11)
            {
                pz = Replace_PZ(pz);
            }
            PZ = pz;
        }

        private string Replace_PZ(string n)
        {
            if(n == "10")
            {
                return "x";
            }
            else if(n == "11")
            {
                return "0";
            }
            return n;
        }


        public string Get_Full_Barcode()
        {
                return Code + PZ;
        }


        public bool Is_Barcode_Valid()
        {
            string pz = Convert.ToString(Calculate_PZ());
            pz = Replace_PZ(pz); 
            if (pz != PZ || Full == false)
            {
                return false;
            }
            return true;
        }
    }
}
