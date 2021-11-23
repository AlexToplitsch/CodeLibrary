using ScottPlot;
using System;
using System.Drawing;
using System.Collections.Generic;
using System.Text;

namespace Schwerpunnktsberechnung
{
    class Circle : Shape
    {
        public string Name { get; private set; } = "Kreis";
        private double radius;
        
        public Circle(Point pCircle, double rad, int h ) : base(pCircle, h)
        {
            radius = rad;
        }

        public override double Area()
        {

            return Math.Pow(radius, 2) * Math.PI; 
        }

        public override Point BallancePoint()
        {
            
            double x_Coord = OffsetP.X_Coord + radius;
            double y_Coord = OffsetP.Y_Coord + radius;
            Point ballance_p = new Point("cart", x_Coord, y_Coord);
            return ballance_p;
        }

        public override string ToString()
        {
            string resultstring = $"Kreis mit dem Offset: X:{OffsetP.X_Coord}, Y:{OffsetP.Y_Coord} und dem Radius {radius}";
            return resultstring;
        }

        protected override double[] CalculateXCoords()
        {
            double[] values = new double[1000];
            double angle = 0;
            for (int i = 0; i < 1000; i++)
            {
                values[i] = BallancePoint().X_Coord + radius * Math.Cos(angle);
                angle += 0.00628318530718;
            }
            return values;
           
        }

        protected override double[] CalculateYCoords()
        {
            double[] values = new double[1000];
            double angle = 0;
            for (int i = 0; i < 1000; i++)
            {
                values[i] = BallancePoint().Y_Coord + radius * Math.Sin(angle);
                angle += 0.00628318530718;
            }
            return values;
        }
        public override void Draw(ref Plot plt)
        {
            Color color;
            if (Hole == 1)
            {
                color = Color.Green;
            }
            else
            {
                color = Color.White;
            }
            plt.PlotPolygon(
                CalculateXCoords(),
                CalculateYCoords(),
                label: null, lineWidth: 2, lineColor: System.Drawing.Color.Black,
                true, fillColor: color,
                fillAlpha: 1);
            plt.PlotPoint(BallancePoint().X_Coord, BallancePoint().Y_Coord, markerSize: 5, color: Color.Red);
        }
    }
}
