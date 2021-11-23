using System;

namespace Quadratische_Gleichungen
{
    class Program
    {

        static double[] Input()
        {
            double[] values = new double[3];
            Console.WriteLine("Geben Sie die drei Werte der quadratischen Gleichung ein:");

            for(int i = 0; i < values.Length; i++){
                Console.Write($"{i}: ");
                values[i] = Convert.ToDouble(Console.ReadLine());
            }

            return values;

        }

        static bool CheckEquation(double partResult)
        {

            if(partResult < 0)
            {
                Console.WriteLine("Gleichung ist nicht lösbar!");
                return false;
            }
            else
            {
                Console.WriteLine("Gleichung ist lösbar!");
                return true;
            }
        }

        static double[] Calculation(double[] values)
        {
            double result1;
            double result2;
            if (CheckEquation(Math.Sqrt(values[1] - 4 * values[0] * values[2])) == true)
            {
                double[] a = new double[2];
                result1 = (-values[1] + (Math.Sqrt(Math.Pow(values[1], 2) - 4 * values[0] * values[2]))) / (2 * values[0]);
                result2 = (-values[1] - (Math.Sqrt(Math.Pow(values[1], 2) - 4 * values[0] * values[2]))) / (2 * values[0]);
                
                a[0] = result1;
                a[1] = result2;

                return a;
            }
            else
            {
                double[] a = new double[0];
                return a;
            }

        }

        static void Output(double[] results)
        {
            for( int i = 0; i < results.Length; i++)
            {
                Console.WriteLine($"x{i}: {results[i]}");
            }
            
        }

        static void Main(string[] args)
        {
            Output(Calculation(Input()));
        }
    }
}
