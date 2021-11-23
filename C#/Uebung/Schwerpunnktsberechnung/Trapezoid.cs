//using ScottPlot;
//using System;
//using System.Collections.Generic;
//using System.Text;

//namespace Schwerpunnktsberechnung
//{
//    class Trapezoid : Shape
//    {
//        private double A { get; set; }
//        private double B { get; set; }
//        private double H { get; set; }

//        public Trapezoid(Point p, double xLong, double xShort, double height) : base(p)
//        {
//            A = xLong;
//            B = xShort;
//            H = height;
//        }

//        public override double Area()
//        {
//            double area = (H / 2) * (A + B);
//            return area;
//        }

//        public override Point BallancePoint()
//        {
//            Point bP;
//            double r = (Math.Pow(A,2) - Math.Pow(B, 2) +
//            double xCoord = 
//            double yCoord = OffsetP.Y_Coord + (H / 3) * ((A + 2 * B) / (A + B)) + ;
//        }

//        public override void Draw(ref Plot plt)
//        {
//            throw new NotImplementedException();
//        }

//        protected override double[] CalculateXCoords()
//        {
//            throw new NotImplementedException();
//        }

//        protected override double[] CalculateYCoords()
//        {
//            throw new NotImplementedException();
//        }
//    }
//}
