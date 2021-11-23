using System;
using System.Collections.Generic;
using System.Text;

namespace Klassenübung.Classes
{
     class Circle
    {
        private double radius;

        public Circle(double r)
        {
            this.radius = r;
        }

        private double Area()
        {
            return Math.Pow(radius, 2) * Math.PI;
        }
        private double Circumference()
        {
            return 2 * radius * Math.PI;
        }

        public string Info()
        {
            string str = $"Der Kreis mit dem Radius {radius}cm hat einen Umfang von {Circumference()}cm und eine Fläche von {Area()}cm².";
            return str;
        }

    }
}
