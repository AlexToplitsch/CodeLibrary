using System;
using System.Collections.Generic;
using Algorithmen;

namespace Barcode_Generator
{
    class Program
    {
        static void Main(string[] args)
        {
            //Console.WriteLine(Primfaktorzerlegung.IsPrimenumber(53));
            //foreach (int element in Primfaktorzerlegung.ListOfPrimenumbers(-99999999))
            //{
            //    Console.WriteLine(element);
            //}
            //Console.WriteLine(Primfaktorzerlegung.GetPrimenumbers(99999988));
            //Console.WriteLine(Primfaktorzerlegung.IsPrimenumber(2272727));
            //ulong n = 100;
            //Console.WriteLine(CatalanZahl.CalcCatalanLookUp(n));
            //int n = 3;
            //string a = "A";
            //string b = "B";
            //string c = "C";
            //Stack<int> stack_A = new Stack<int>();
            //Stack<int> stack_B = new Stack<int>();
            //Stack<int> stack_C = new Stack<int>();

            //Init(stack_A, n);
            //DisplayStack(a, b, c, stack_A, stack_B, stack_C);
            //Solve(n, a, b, c, stack_A, stack_B, stack_C);
            //Solve(n, c, a, b, stack_C, stack_A, stack_B);
            double a = -10.0, b = 0.0;
            Console.WriteLine(Nullstellenbestimmung.CalcIntersection(a, b, -9)); 

        }
        public static void Init( Stack<int> stack, int n)
        {
            for (int i = n; i > 0; i--)
            {
                stack.Push(i);
            }
        }
        public static void DisplayStack(string a, string b, string c, Stack<int> stack1, Stack<int> stack2, Stack<int> stack3)
        {
            Console.Write($"{a}:");
            foreach (var item in stack1)
            {
                Console.Write(item);
            }
         
            Console.WriteLine();
            Console.Write($"{b}:");
            foreach (var item in stack2)
            {
                Console.Write(item);
            }
         
            Console.WriteLine();
            Console.Write($"{c}:");
            foreach (var item in stack3)
            {   
                Console.Write(item);
            }
           
            Console.WriteLine();

        }
        public static void Solve(int n, string a, string b, string c, Stack<int> A, Stack<int> B, Stack<int> C)
        {
            if (n == 0)
            {
                return;
            }
            Solve(n - 1, a, c, b, A, C, B);
            Move(a, b, c, n, A, B, C);
            Solve(n - 1, b, a, c, B, A, C);
        }

        public static void Move(string a, string b, string c, int n, Stack<int> stackA, Stack<int> stackB, Stack<int> stackC)
        {
            Console.WriteLine($"Move Ring {n} from Stack {a} to Stack {c}");
            stackC.Push(stackA.Pop());
            DisplayStack(a, b, c, stackA, stackB, stackC);
        }
    }
}
