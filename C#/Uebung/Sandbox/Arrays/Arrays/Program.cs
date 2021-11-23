using System;

namespace Arrays
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Geben Sie die Länge der Zeile ein:");
            int n = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine("Geben Sie den Bereich in der Zahlen  ein:");
            int m = Convert.ToInt32(Console.ReadLine());
            Random rand = new Random();

            int[] arr = new int[n];

            for (int i = 0; i < n; i++)
            {
                arr[i] = rand.Next(0, m);
                Console.Write(arr[i]+ " ");

            }
        }
    }
}
