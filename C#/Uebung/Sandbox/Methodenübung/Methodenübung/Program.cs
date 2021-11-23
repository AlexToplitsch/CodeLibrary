using System;

namespace Methodenübung
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Geben Sie die zu berechnende Geometrie ein:");
            string geometry = Console.ReadLine();
            if (geometry == "Rechteck")
            {
                Console.WriteLine("Wollen Sie die Fläche oder den Umfang berechnen?");
                string formula = Console.ReadLine();
                Console.WriteLine("Geben Sie nun die zwei Seiten ein in cm ein:");
                double length = Convert.ToDouble(Console.ReadLine());
                double width = Convert.ToDouble(Console.ReadLine());
                double res = GeometryRectangle(formula, length, width);
                Console.WriteLine("Der berechnete Wert beträgt " + res);
            }

            else if (geometry == "Dreieck")
            {
                Console.WriteLine("Wollen Sie die Fläche oder den Umfang berechnen?");
                string formula = Console.ReadLine();
                Console.WriteLine("Ist es ein rechtwinkeliges oder ein gleichschenkliges Dreieck?");
                string shape = Console.ReadLine();
                Console.WriteLine("Geben Sie nun die drei Längen ein: (Die längsten Seite zuerst!)");
                double a = Convert.ToDouble(Console.ReadLine());
                double b = Convert.ToDouble(Console.ReadLine());
                double c = Convert.ToDouble(Console.ReadLine());
                double res = GeometryTriangle(formula, shape, a, b, c);
                Console.WriteLine("Der berechnete Wert beträgt " + res);
            }

            else if (geometry == "Kreis")
            {
                Console.WriteLine("Wollen Sie die Fläche oder den Umfang berechnen?");
                string formula = Console.ReadLine();
                Console.WriteLine("Geben Sie nun den Radius in cm ein:");
                double radius = Convert.ToDouble(Console.ReadLine());
                double res = GeometryCircle(formula, radius);
                Console.WriteLine("Der berechnete Wert beträgt " + res);
            }

            else
            {
                Console.WriteLine("Eingabe ist ungültig!");
            } 
        }

        public static double GeometryRectangle(string formula, double length, double width)
        {
            if (formula == "Fläche")
            {
                double resArea = length * width;
                return resArea;
            }
            else
            {
                double resScope = 2* (width + length);
                return resScope;
            }   
        }

        public static double GeometryTriangle(string shape, string formula, double firstLength, double secondLength, double thirdLength)
        {
            double resScope = 0;
            double resArea = 0;
            if (formula == "Umfang")
            {
                resScope = firstLength + secondLength + thirdLength;
                return resScope;
            }

            else
            {
                switch (shape)
                {
                    case "rechtwinkelig":
                        resArea = (firstLength * secondLength) / 2;
                        return resArea;
                        
                    default:
                        double height = 0;

                        if (firstLength == secondLength)
                        {
                            height = Math.Sqrt(Math.Pow(firstLength, 2) - Math.Pow(thirdLength / 2, 2));
                            resArea = (height * thirdLength) / 2;
                        }

                        else if (firstLength == thirdLength)
                        {
                            height = Math.Sqrt(Math.Pow(firstLength, 2) - Math.Pow(secondLength / 2, 2));
                            resArea = (height * secondLength) / 2;
                        }

                        else
                        {
                            height = Math.Sqrt(Math.Pow(secondLength, 2) - Math.Pow(firstLength / 2, 2));
                            resArea = (height * secondLength) / 2;
                        }

                        return resArea;
                }
            }  
        }
        public static double GeometryCircle(string formula, double radius)
        {
            if (formula == "Fläche")
            {
                double resArea = Math.Pow(radius, 2) * Math.PI;
                return resArea;
            }
            else
            {
                double resScope = radius * 2 * Math.PI;
                return resScope;
            }
        }
    }
}
