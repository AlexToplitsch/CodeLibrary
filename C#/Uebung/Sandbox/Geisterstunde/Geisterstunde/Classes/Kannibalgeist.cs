using System;
using System.Collections.Generic;
using System.Text;

namespace Geisterstunde.Classes
{
    class Kannibalgeist : Geist
    {
        public Kannibalgeist(string name, int size) : base(name, size)
        {
       
        }

        public int Eat()
        {
            this.size += 1;
            return size;
        }

        public void Eat(ref SchleimGeist g)
        {
            this.size = this.size + g.size;
            g = null;
        }
        public void Eat(ref Geist g)
        {
            this.size = this.size + g.size;
            g = null;
        }
        public void Eat(ref Kannibalgeist g)
        {
            this.size = this.size + g.size;
            g = null;
        }
    }
}
