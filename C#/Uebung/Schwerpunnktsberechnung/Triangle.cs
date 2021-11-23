using ScottPlot;
using System;
using System.Drawing;
using System.Collections.Generic;
using System.Text;

namespace Schwerpunnktsberechnung
{
    class Triangle : Shape
    {
        private Point p1;
        private Point p2;
        private Point p3;
        public Triangle(Point offP, Point pa, Point pb, Point pc, int h) : base(offP, h)
        {
            p1 = pa;
            p2 = pb;
            p3 = pc;
        }

        public override double Area()
        {
            return 0.5 * ((p2.X_Coord - p1.X_Coord) * (p3.Y_Coord - p1.Y_Coord) - (p3.X_Coord - p1.X_Coord) * (p2.Y_Coord - p1.Y_Coord));            
        }
        public override Point BallancePoint()
        {
            double x_Coord = OffsetP.X_Coord + 0.333333333333333333333 * (p1.X_Coord + p2.X_Coord + p3.X_Coord);
            double y_Coord = OffsetP.Y_Coord + 0.333333333333333333333 * (p1.Y_Coord + p2.Y_Coord + p3.Y_Coord);
            Point ballance_p = new Point("cart", x_Coord, y_Coord);
            return ballance_p;
        }

        protected override double[] CalculateXCoords()
        {
            Point[] points = new Point[3] { p1, p2, p3 };
            double[] values = new double[3];
            for (int i = 0; i < values.Length; i++)
            {            
                    values[i] = OffsetP.X_Coord + points[i].X_Coord;
            }
            return values;
        }

        protected override double[] CalculateYCoords()
        {
            Point[] points = new Point[3] { p1, p2, p3 };
            double[] values = new double[3];
            for (int i = 0; i < values.Length; i++)
            {
                values[i] = OffsetP.Y_Coord + points[i].Y_Coord;
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
        public override string ToString()
        {
            string resultstring = $"Dreieck mitdem Offset X: {OffsetP.X_Coord} Y: {OffsetP.Y_Coord} den Koordinaten: X1: {p1.X_Coord}, Y1: {p1.Y_Coord}, X2: {p2.X_Coord}, Y2: {p2.Y_Coord}, X3: {p3.X_Coord}, Y3: {p3.Y_Coord}";
            return resultstring;
        }
    }
}
