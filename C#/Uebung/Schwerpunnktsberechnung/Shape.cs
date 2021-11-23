using System;
using System.Collections.Generic;
using System.Text;
using ScottPlot;

namespace Schwerpunnktsberechnung
{
    public abstract class Shape
    {   
        public Point OffsetP { get; set; }
        public int Hole { get; set; }
        public Shape(Point p, int hole = 1)
        {
            OffsetP = p;
            if (hole == 0||hole == 1)
            {
                Hole = hole;
            }
            else
            {
                throw new NotImplementedException("Der letze Parameter muss 0 oder 1 sein");
            }
            
        }

        public abstract double Area();

        public abstract Point BallancePoint();
        protected abstract double[] CalculateXCoords();
        protected abstract double[] CalculateYCoords();
        public abstract void Draw(ref Plot plt);
    }
}
