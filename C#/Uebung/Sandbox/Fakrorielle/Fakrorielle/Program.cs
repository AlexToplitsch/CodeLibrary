using System;

namespace Fakrorielle
{
    class Program
    {
        static decimal Factorielle(ulong number1, ulong number2)
        {
            ulong n = 1;
            ulong k = 1;
            ulong nk = 1;
            decimal result = 0;
           
            for (uint i = 1; i <= number1; i++)
            {
                n = n * i;
            }

            for (uint i = 1; i <= number2; i++)
            {
                k = k * i;
            }

            for (uint i = 1; i <= (number1 - number2); i++) 
            {
                nk = nk * i;
                
            }
            result = (n / (k * nk));
            return result;

        }
        static void Main(string[] args)
        {
            uint n = Convert.ToUInt32(Console.ReadLine());
            uint k = Convert.ToUInt32(Console.ReadLine());
            decimal res = Factorielle(n, k);
            Console.Write(res.ToString());
        }
    }
}
