using System;
using System.Collections.Generic;
using System.Text;

namespace Algorithmen
{
    public class Nullstellenbestimmung
    {
        private static double Function(double x)
        {
            return 2.0 * x + 8.0;
        }

        public static double CalcIntersection(double a, double b, int epsilon)
        {
            if (!((Function(a) < 0 && 0 < Function(b)) || (Function(a) > 0 && 0 > Function(b))))
            {
                throw new NoIntersectionFound($"Keine oder eine gerade Anzahl an Nullstellen in dem Bereich von {a} bis {b} gefunden!");
            }
            return CalcIntersectionRek(a, b, epsilon);
        }

        public static double CalcIntersectionRek(double a, double b, int epsilon)
        { 
            if (Math.Abs(Function(a)) <= Math.Pow(10, epsilon))
            {
                return a;
            }
            if(Function(b) == 0)
            {
                return b;
            }

            double m = a + (b - a) / 2;

            if((Function(a) < 0 && 0 < Function(m)) || (Function(a) > 0 && 0 > Function(m)))
            {
                return CalcIntersectionRek(a, m, epsilon);
            }
            else
            {
                return CalcIntersectionRek(m, b, epsilon);
            }
        }
    }

    public class NoIntersectionFound : Exception
    {
        public NoIntersectionFound()
        {

        }
        public NoIntersectionFound(string message):base(message)
        {

        }
    }
}
