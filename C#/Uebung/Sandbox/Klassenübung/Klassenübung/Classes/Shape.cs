using System;
using System.Collections.Generic;
using System.Text;
//Übung für Klassenvererbung
namespace Klassenübung.Classes
{
    public class Shape
    {
        public Shape(string name)
        {
            Name = name;
        }
        public string Name { get; set; }        //das ist ein Property

        protected virtual double Area()
        {
            return 10.0;
        }
    }
}
