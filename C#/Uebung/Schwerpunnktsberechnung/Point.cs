using System;
using System.Collections.Generic;
using System.Text;

namespace Schwerpunnktsberechnung
{
    public class Point
    {
        public double X_Coord { get; private set; }
        public double Y_Coord { get; private set; }
        public double Z_Coord { get; private set; }
        public double DimensionXY { get; private set; }
        public double DimensionXZ { get; private set; }
        public double Length { get; private set; }
        public Point(string id = "cart", double x = 0, double y = 0, double z = 0)
        {
            if(id == "cart")
            {
                CartesianCoord(x, y, z);
            }
            else if(id == "pol")
            {
                PolarCoord(x, y, z);
            }
            else
            {
                Console.WriteLine("Nicht definiertes Koordinatensystem!");
            }
        }

        private void CartesianCoord(double xCoord, double yCoord, double zCoord)
        {
            X_Coord = xCoord;
            Y_Coord = yCoord;
            Z_Coord = zCoord;
        }

        private void PolarCoord(double angleXY, double angleXZ, double length)
        {
            DimensionXY = angleXY;
            DimensionXZ = angleXZ;
            Length = length;

        }


    }
}
