using System;
using Algorithmen;

namespace Mainprogram
{
    class Program
    {
        static void Main(string[] args)
        {
            ArrayCreater creater = new ArrayCreater();
            int[] arr = creater.CreateArray(30, 500);
            creater.PrintArray(arr);
            arr = Sortieralgorithmen.BubbleSort(arr);
            creater.PrintArray(arr);
            Console.WriteLine("Nach welcher Nummer soll gesucht werden?");
            int n = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine(Suchalgorithmen.BinarySearch(arr, n));
        }
    }
}
