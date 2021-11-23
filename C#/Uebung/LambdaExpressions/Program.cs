using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;

namespace LambdaExpressions
{
    class Program
    {
        static void Main(string[] args)
        {
            var list = Helper.Create_dataset();

            var apprentices = list
                                  .FirstOrDefault(x => x.Apprentice);
            Console.WriteLine(apprentices.Name);
           // Helper.Display_enum(apprentices);
        }

        private static void run()
        {
            var list = new List<int>() { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19 };
            var new_list = EvenNumbers(list, x => x % 2 == 1);
            Display<int>(new_list);

            Console.WriteLine();

            var res = Calculate<int, double>(5, 6, (x, y) => x * x + y * y);
            Console.WriteLine(res);
            Func<int, int> fib = Fib;

            Console.WriteLine("\nFibbonaci");
            Benchmarking(75, fib);
        }

        private static int Fib(int x)
        {
            if (x == 1)
            {
                return 1;
            }
            if (x == 0)
            {
                return 0;
            }
            return Fib(x - 1) + Fib(x - 2);
        }

        private static void Display<T>(IEnumerable<T> list)
        {
            foreach (var item in list)
            {
                Console.WriteLine(item);
            }
        }

        private static IEnumerable<T> EvenNumbers<T>(IEnumerable<T> numbers, FilterOp<T>f)
        {
            
            foreach(T number in numbers)
            {
                if (f(number))
                {
                    yield return number;
                }
            }
            
        }

        private delegate bool FilterOp<T>(T x);

        private delegate TResponse Calc<in T, out TResponse>(T x, T y);

        private static TResponse Calculate< T, TResponse>(T x, T y, Calc<T, TResponse> f)
        {
            return f(x, y);
        }

        private static void Benchmarking(int x,  Func<int, int> f)
        {
            Stopwatch watch = new Stopwatch();
            watch.Start();
            Console.WriteLine(f(x));
            watch.Stop();
            long res = watch.ElapsedMilliseconds;
            Console.WriteLine(res);
        }

    }
}
