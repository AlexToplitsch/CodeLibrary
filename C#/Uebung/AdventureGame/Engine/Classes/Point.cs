using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Engine.Classes
{
    public class Point
    {

        public int X_Coord { get; set; }
        public int Y_Coord { get; set; }
        public Point(int x, int y)
        {
            X_Coord = x;
            Y_Coord = y;
        }


    }
}
