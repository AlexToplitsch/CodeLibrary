using System;
using System.Numerics;
using System.Runtime.ExceptionServices;

namespace Schachbrett
{
    class Program
    {
        static void Main(string[] args)
        {
            int n = Convert.ToInt32(Console.ReadLine());
            int[,] schachbrett = new int[n, n];
            int[] zeilensummen = new int[n];
            int[] spaltensummen = new int[n];
            int count = 0;

            for (int i = 0; i < n; i++)
            {
                for(int j = 0; j < n; j++)
                {
                    schachbrett[i, j] = 10 * (i + 1) + (j + 1);
                    Console.Write(schachbrett[i, j] + "   ");
                    zeilensummen[i] = zeilensummen[i] + schachbrett[i, j];
                    
                }
                Console.Write("=   " + zeilensummen[i]);
                Console.WriteLine();

            }

            Console.WriteLine();
            Console.WriteLine();

            for (int i = 0; i < n; i++)
            {
                for (int j = 0; j < n; j++)
                {
                    spaltensummen[i] = spaltensummen[i] + schachbrett[j, i];
                }

                Console.Write(spaltensummen[i] + "  ");

            }

            for(int i = 0; i < n; i++)
            {
                for(int j = 0; j < n; j++)
                {
                    if (schachbrett[i,j] % 2 == 0 && schachbrett[i, j] % 3 == 0)
                    {
                        count++;
                    }
                }
            }

            Console.WriteLine();

            Console.WriteLine("Die Anzahl der geraden Zahlen beträgt " + count);

        }
    }
}
