using System;
using System.Collections.Generic;
using System.Text;

namespace Geisterstunde.Classes
{
    class SchleimGeist : Geist
    {
        public SchleimGeist(string name, int size) : base(name, size)
        {

        }
        private string schleimspur = "~~~~~";

        public string Slime()
        {
            return schleimspur;
        }

        public override string Haunt()
        {
            return base.Haunt() + this.Slime();
        }

    }
}
