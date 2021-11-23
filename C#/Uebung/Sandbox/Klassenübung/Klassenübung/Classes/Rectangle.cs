using System;
using System.Collections.Generic;
using System.Text;

namespace Klassenübung.Classes
{
    public class Rectangle : Shape              //erbt von der Klasse Shape
    {
        private double width;
        private double length;


        //constructor ":base(name)" --> der Übergabeparameter "name" wird an die Baseklasse übergeben
        //(constructor von Shape wird ausgrführt)
        public Rectangle(double a, double b, string name) : base(name)
        {
            this.width = a;
            this.length = b;
        }


        protected override double Area()
        {
            return width * length;
        }

        private double Circumference()
        {
            return 2 * (width + length);
        }

        public string Display()
        {
            string text = $"Das Rechteck mit der Breite {width}cm und der Länge {length}cm hat einen Umfang von {Circumference()}cm und eine Fläche von {Area()}cm².";
            return text;

        }
    }
}
