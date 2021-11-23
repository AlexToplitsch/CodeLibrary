using System;
using System.Collections.Generic;
using System.Text;

namespace Klassenübung.Classes
{
    class Triangle
    {
        private double firstLength;
        private double secondLength;
        private double thirdLength;

        public Triangle(double a, double b, double c = 0)
        {
            this.firstLength = a;
            this.secondLength = b;
            if (c == 0)
            {
                this.thirdLength = Math.Sqrt(Math.Pow(firstLength, 2) + Math.Pow(secondLength, 2)); 
            }
        } 

        private double Area()
        {
            if (firstLength == secondLength && thirdLength != Math.Sqrt(Math.Pow(firstLength, 2) + Math.Pow(secondLength, 2)))
            {
                double height = Math.Sqrt(Math.Pow(firstLength, 2) - Math.Pow(thirdLength / 2, 2));
                double resArea = (height * (thirdLength / 2)) / 2;
                return resArea;
            }

            else if (firstLength == thirdLength && firstLength < secondLength)
            {
                double height = Math.Sqrt(Math.Pow(firstLength, 2) - Math.Pow(secondLength / 2, 2));
                double resArea = (height * (secondLength / 2)) / 2;
                return resArea;
            }

            else if (secondLength == thirdLength && secondLength < firstLength)
            {
                double height = Math.Sqrt(Math.Pow(secondLength, 2) - Math.Pow(firstLength / 2, 2));
                double resArea = (height * (firstLength / 2)) / 2;
                return resArea;
            }

            else
            {
                return (firstLength * secondLength) / 2;
            }
        }

        private double Circumference()
        {
                return firstLength + secondLength + thirdLength;
           
        }

        public string Display()
        {
            string text = $"Das Dreieck mit den Seiten {firstLength}cm, {secondLength}cm, {thirdLength}cm, hat einen Umfang von {Circumference()}cm und eine Fläche von {Area()}cm².";
            return text;

        }
    }
}
