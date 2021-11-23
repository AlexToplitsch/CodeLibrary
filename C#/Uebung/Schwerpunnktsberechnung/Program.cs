using System;
using System.Collections.Generic;

namespace Schwerpunnktsberechnung
{
    class Program
    {
        //static string Input()
        //{
        //    Console.WriteLine(@"Fügen Sie die Datei in diesen Ordner ein: D:\IT-Unterricht\Programme\C#\Schwerpunnktsberechnung\Shapedata\");
        //    Console.WriteLine("Geben Sie die eingfügte Datei hier ein: ");
        //    string path = "Parameter.txt"; //Console.ReadLine();
        //    return path;
        //}
        static void Output()
        {
            CombinedShape combined = CombinedShape.GetShape("Parameter.txt");
            Point bp = combined.BallancePoint();
            string output = $"X:{bp.X_Coord}      Y:{bp.Y_Coord}";
            Console.WriteLine(output);
            combined.Display();
            combined.ShowImage();
        }
        static void Main(string[] args)
        {
            Output();
        }
    }
}