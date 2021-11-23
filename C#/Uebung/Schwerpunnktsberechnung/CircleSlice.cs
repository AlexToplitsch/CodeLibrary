using ScottPlot;
using System;
using System.Drawing;
using System.Collections.Generic;
using System.Text;

namespace Schwerpunnktsberechnung
{
    class CircleSlice : Shape
    {
        private double Radius { get; set; }
        private double StartAngle { get; set; }
        private double SegmentAngle { get; set; }
        public CircleSlice(Point offP, double radius, double startAngle, double segmentAngle, int h) : base(offP, h)
        {
            Radius = radius;
            StartAngle = startAngle * (Math.PI/180);
            SegmentAngle = segmentAngle * (Math.PI/180);
        }

        public override double Area()
        {
            double area = 0;
            area = SegmentAngle * Math.Pow(Radius, 2);
            return area;
        }

        public override Point BallancePoint()
        {
            double h = 0.6666666666667 * Radius * (Math.Sin(SegmentAngle / 2) / (SegmentAngle / 2));
            double xCoord = OffsetP.X_Coord + h * Math.Cos(StartAngle + (SegmentAngle / 2));
            double yCoord = OffsetP.Y_Coord + h * Math.Sin(StartAngle + (SegmentAngle / 2));
            Point bP = new Point("cart", xCoord, yCoord);
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

        protected override double[] CalculateYCoords()
        {
            int points = Convert.ToInt32((1000/(Math.PI *2)) * SegmentAngle);
            double[] values = new double[points];
            double angle = StartAngle;
            values[0] = OffsetP.Y_Coord;
            for (int i = 1; i < values.Length - 1; i++)
            {
                values[i] = OffsetP.Y_Coord + Radius * Math.Sin(angle);
                angle += SegmentAngle / points;
            }
            values[points-1] = OffsetP.Y_Coord + Radius * Math.Sin(StartAngle + SegmentAngle);
            return values;
        }

        protected override double[] CalculateXCoords()
        {
            int points = Convert.ToInt32((1000 / (Math.PI * 2)) * SegmentAngle);
            double[] values = new double[points];
            double angle = StartAngle;
            values[0] = OffsetP.X_Coord;
            for (int i = 1; i < values.Length - 1; i++)
            {
                values[i] = OffsetP.X_Coord + Radius * Math.Cos(angle);
                angle += SegmentAngle / points;
            }
            values[points-1] = OffsetP.X_Coord + Radius * Math.Cos(StartAngle + SegmentAngle);
            return values;
        }

        public override string ToString()
        {
            string resultstring = $"Kreisausschnitt mit dem Offset: X:{OffsetP.X_Coord}, Y:{OffsetP.Y_Coord}, Alpha:{StartAngle*180/Math.PI} dem Radius {Radius} und dem Winkel Phi:{SegmentAngle * 180 / Math.PI} ";
            return resultstring;
        }
    }
}
