using System;
using Geisterstunde.Classes;

namespace Geisterstunde
{
    class Program
    {
        static void Main(string[] args)
        {
            Geist spooky = new Geist("Spooky", 5);
            SchleimGeist slimey = new SchleimGeist("Slimey", 6);
            Geist smeagol = new Geist("Smeagol", 1);
            Kannibalgeist hungry = new Kannibalgeist("Hungry", 4);
            Console.WriteLine(smeagol.Greetings());
            hungry.Eat(ref smeagol);
            Console.Write(hungry.size);



        }
    }
}
