using System;
using System.Collections.Generic;
using System.Text;

namespace Algorithmen
{
    public class CatalanZahl
    {
        static  ulong[] lookup = new ulong[1000];

        private static void Init()
        {
            lookup[0] = 1;

            for (int i = 1; i < lookup.Length; i++)
            {
                lookup[i] = 0;
            }

        }

        private static ulong CalcCatalanRekLookUp(ulong n)
        {
            
            if (lookup[n] == 0)
            {
                ulong c = 0;
                for (ulong i = 0; i <= n - 1; i++)
                {
                    c += CalcCatalanRekLookUp(i) * CalcCatalanRekLookUp(n - 1 - i);
                }
                lookup[n] = c;
            }

            return lookup[n];

        }

        public static ulong CalcCatalanLookUp(ulong n)
        {
            Console.WriteLine("Hallo!");
            Init();
            return CalcCatalanRekLookUp(n + 1);
        }

        public static int CalcCatalan(int n)
        {
            return CalcCatalanRek(n + 1);
        }

        private static int CalcCatalanRek(int n)
        {
            if (n <= 1)
            {
                return 1;
            }
            int c = 0;
            for (int i = 0; i <= n - 1; i++)
            {
                c += CalcCatalanRek(i) * CalcCatalanRek(n - 1 - i);
            }
            return c;

        }

    }
}
