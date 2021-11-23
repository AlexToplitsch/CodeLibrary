using System;
using System.ComponentModel;
using System.Security.Cryptography;

namespace MatrixMalVector
{
    class Program
    {
        static void Main(string[] args)
        {
            Random rand = new Random();
            int matrixlength = Convert.ToInt32(Console.ReadLine());
            int matrixheight = Convert.ToInt32(Console.ReadLine());
            int[] vector = new int[matrixlength];
            int[] resultVector = new int[matrixheight];
            int[,] matrix = new int[matrixheight, matrixlength];

            Console.WriteLine();

            // Erstellung der Matrix und des Vectors
            for (int i = 0; i < matrixheight; i++)
            {
                for(int j = 0; j < matrixlength; j++)
                {
                    matrix[i, j] = rand.Next(1, 10);
                    Console.Write(matrix[i, j] + " ");
                    vector[i] = rand.Next(1, 10);
                }
                Console.WriteLine();
                
            }

            Console.WriteLine('x');

            foreach (int point in vector)
            {
                Console.Write(point + " ");
            }

            Console.WriteLine('=');

            // Multiplikation der Matrix mit dem Vector
            for(int i = 0; i < matrixheight; i++)
            {
                for(int j = 0; j < matrixlength; j++)
                {
                    resultVector[i] = resultVector[i] + matrix[i, j] * vector[j];
                    
                }
                Console.Write(resultVector[i] + " ");


            }
        }
        
    }
}
