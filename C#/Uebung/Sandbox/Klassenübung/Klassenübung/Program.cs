using Klassenübung.Classes;
using System;

namespace Klassenübung
{
    class Program
    {
        static void Main(string[] args)
        {
            Rectangle rect1 = new Rectangle(4,5, "Alex");
            Console.WriteLine(rect1.Display());
            Console.WriteLine();

            Triangle tri1 = new Triangle(5,7);
            Console.WriteLine(tri1.Display());
            Console.WriteLine();


            Circle circ1 = new Circle(5);
            Console.WriteLine(circ1.Info());
            Console.WriteLine();

        }
    }
}
