using System;
using System.Collections.Generic;
using System.Text;

namespace Algorithmen
{
    public static class CatalanZahl
    {
        public static int CalcCatalanRek(int n)
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

        public static int CalcCatalan(int n)
        {
            return CalcCatalanRek(n + 1);
        }

    }
}
