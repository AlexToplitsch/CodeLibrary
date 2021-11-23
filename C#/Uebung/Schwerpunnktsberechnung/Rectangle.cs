using ScottPlot;
using System;
using System.Drawing;

namespace Schwerpunnktsberechnung
{
    class Rectangle : Shape
    {
        public string Name { get; private set; } = "Rechteck";
        private double lengthX;
        private double lengthY;
        public Rectangle(Point pRect, double lenX, double lenY, int h) : base(pRect, h)
        {
            lengthX = lenX;
            lengthY = lenY;
        }

        public override double Area()
        {
            return lengthX * lengthY;
        }

        public override Point BallancePoint()
        {

            double x_Coord = OffsetP.X_Coord + (lengthX / 2);
            double y_Coord = OffsetP.Y_Coord + (lengthY / 2);
            Point ballance_p = new Point("cart", x_Coord, y_Coord);
            return ballance_p;
        }

        public override string ToString()
        {
            string resultstring = $"Rechteck mit dem Offset: X:{OffsetP.X_Coord}, Y:{OffsetP.Y_Coord} und der Länge in X:{lengthX} und in Y:{lengthY}";
            return resultstring;
        }

        protected override double[] CalculateXCoords()
        {
            double[] values = new double[4];
            for (int i = 0; i < values.Length; i++)
            {
                if (i <= 1)
                {
                    values[i] = OffsetP.X_Coord;
                }
                else
                {
                    values[i] = OffsetP.X_Coord + lengthX;
                }
            }
            return values;
        }

        protected override double[] CalculateYCoords()
        {
            double[] values = new double[4];
            for (int i = 0; i < values.Length; i++)
            {
                if (i == 0 || i == 3)
                {
                    values[i] = OffsetP.Y_Coord;
                }
                else
                {
                    values[i] = OffsetP.Y_Coord + lengthY;
                }
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
