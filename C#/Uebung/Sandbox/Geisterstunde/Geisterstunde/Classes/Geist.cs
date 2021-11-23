using System;
using System.Collections.Generic;
using System.Drawing;
using System.Security.Cryptography.X509Certificates;
using System.Text;

namespace Geisterstunde.Classes
{
    public class Geist
    {
        public Geist(string name, int size)
        {
            Name = name;
            this.size = size;
        }
        public string Name { get; private set; }
        protected string buh = "BUH!!!";
        protected string greetings = "Hallo mein Name ist ";
        public int size;
        public virtual string Haunt()
        {
            return buh;
        }

        public string Greetings()
        {
            return greetings + Name + "!";
        }
    }
}