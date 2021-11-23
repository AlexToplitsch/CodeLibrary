using ScottPlot;
using System;
using System.Drawing;
using System.Collections.Generic;
using System.Text;

namespace Schwerpunnktsberechnung
{
    class Circlesection : Shape
    {

        private double Radius { get; set; }
        private double Length { get; set; }
        private double StartAngle { get; set; }
        private double SegmentAngle { get; set; }
        private Point Centralpoint { get; set; }
        public Circlesection(Point p, double radius, double length, double startangle, int h) : base(p, h)
        {
            Radius = radius;
            Length = length;
            StartAngle = (startangle * (Math.PI/180)) - Math.Sinh((length / 2) / radius);
            SegmentAngle = 2 * Math.Sinh((length / 2) / radius);
            CalculateCentralpoint();
        }

        public override double Area()
        {
            double area = 0.5 * Math.Pow(Radius, 2) * (2 * (SegmentAngle/2) - Math.Sin(SegmentAngle));
            return area;
        }

        public override Point BallancePoint()
        {
            Point bP;
            double h = Math.Pow(Length, 3) / (12 * Area());
            double xCoord = Centralpoint.X_Coord + h * Math.Cos(StartAngle + (SegmentAngle / 2));
            double yCoord = Centralpoint.Y_Coord + h * Math.Sin(StartAngle + (SegmentAngle / 2));
            bP = new Point("cart", xCoord, yCoord);
            return bP;
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

        protected override double[] CalculateXCoords()
        {
            int points = Convert.ToInt32((1000 / (Math.PI * 2)) * SegmentAngle);
            double angle = StartAngle;
            double[] x = new double[points];
            x[0] = Centralpoint.X_Coord + Radius * Math.Cos(StartAngle);
            for(int i = 1; i < x.Length - 1; i++)
            {
                x[i] = Centralpoint.X_Coord + Radius * Math.Cos(angle);
                angle += SegmentAngle / points;
            }
            x[points-1] = Centralpoint.X_Coord + Radius * Math.Cos(StartAngle + SegmentAngle);
            return x;
        }

        protected override double[] CalculateYCoords()
        {
            int points = Convert.ToInt32((1000 / (Math.PI * 2)) * SegmentAngle);
            double angle = StartAngle;
            double[] y = new double[points];
            y[0] = Centralpoint.Y_Coord + Radius * Math.Sin(StartAngle);
            for (int i = 1; i < y.Length - 1; i++)
            {
                y[i] = Centralpoint.Y_Coord + Radius * Math.Sin(angle);
                angle += SegmentAngle / points;
            }
            y[points-1] = Centralpoint.Y_Coord + Radius * Math.Sin(StartAngle + SegmentAngle);
            return y;
        }

        private void CalculateCentralpoint()
        {
            double x = OffsetP.X_Coord - Radius * Math.Cos(StartAngle);
            double y = OffsetP.Y_Coord - Radius * Math.Sin(StartAngle);
            Centralpoint = new Point("cart", x, y);
        }
    }
}
