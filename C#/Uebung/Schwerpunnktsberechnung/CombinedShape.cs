using System;
using System.Collections.Generic;
using System.Drawing;
using System.Text;
using ScottPlot;
using OpenCvSharp;

namespace Schwerpunnktsberechnung
{
    class CombinedShape : Shape
    {
        private static CombinedShape Combined_Shape = null;
        private static List<Shape> Shapes { get; set; }
        public static int Dimension { get; set; }
        private double CombinedArea { get; set; }
        private Point CombinedBP { get; set; }
        private static string CoordSystem { get; set; }


        private CombinedShape(List<Shape> shapes, Point p, int h) : base(p, h)
        {
            Shapes = shapes;
        }

        public static CombinedShape GetShape(string file)
        {
            if(Combined_Shape == null)
            {
                Point p = new Point("cart");
                int h = 0;
                Combined_Shape = new CombinedShape(CreateShape(file), p, h);
            }

            return Combined_Shape;
        }
        public override double Area()
        {
            foreach(Shape shape in Shapes)
            {
                if(shape.Hole == 1)
                {
                    CombinedArea += shape.Area();

                }
                else
                {
                    CombinedArea -= shape.Area();
                }
            }

            return CombinedArea;
        }

        public override Point BallancePoint()
        {
            CombinedArea = Area();
            double x_s = 0;
            double y_s = 0;
            foreach (Shape shape in Shapes)
            {
                double area;
                if (shape.Hole == 1)
                {
                    area = shape.Area();
                }
                else
                {
                    area = shape.Area() * -1;
                }
                double xcoord = shape.BallancePoint().X_Coord;
                double ycoord = shape.BallancePoint().Y_Coord;
                x_s += (xcoord * area);
                y_s += (ycoord * area);
            }
            CombinedBP = new Point("cart", x_s / CombinedArea, y_s / CombinedArea);
            return CombinedBP;
        }

        private static List<Shape> CreateShape(string file)
        {
            
            string[] datalines = System.IO.File.ReadAllLines(@"D:\IT-Unterricht\Programme\C#\Schwerpunnktsberechnung\Shapedata\" + file);
            List<Shape> shapes = new List<Shape>();

            for (int i = 0; i < datalines.Length; i++)
            {
                string[] parameters = datalines[i].Split(' ');
                Point offset_p;
                if (i == 0)
                {
                    try
                    {
                        Dimension = Convert.ToInt32(parameters[0]);
                        continue;
                    }
                    catch (FormatException)
                    {
                        Console.WriteLine("Dimesnion fehlt in der ersten Zeile!");
                        break;
                    }
                }
                if(i == 1)
                {
                    if(parameters[0] == "cart" || parameters[0] == "pol")
                    {
                        CoordSystem = parameters[0];
                        continue;
                    }
                    else
                    {
                        Console.WriteLine("Geben Sie in die zweite Zeile das Koordinatensystem ein!");
                        break;
                    }
                    
                }
               
                if (parameters[0] == "cir")
                {
                    offset_p = new Point(CoordSystem, Convert.ToDouble(parameters[1]), Convert.ToDouble(parameters[2]));
                    double radius = Convert.ToDouble(parameters[3]);
                    int h = Convert.ToInt32(parameters[4]);
                    shapes.Add(new Circle(offset_p, radius, h));
                }

                else if (parameters[0] == "tri")
                {
                    Point offsetP = new Point(CoordSystem, Convert.ToDouble(parameters[1]), Convert.ToDouble(parameters[2]));
                    Point p1 = new Point(CoordSystem, Convert.ToDouble(parameters[3]), Convert.ToDouble(parameters[4]));
                    Point p2 = new Point(CoordSystem, Convert.ToDouble(parameters[5]), Convert.ToDouble(parameters[6]));
                    Point p3 = new Point(CoordSystem, Convert.ToDouble(parameters[7]), Convert.ToDouble(parameters[8]));
                    int h = Convert.ToInt32(parameters[9]);
                    shapes.Add(new Triangle(offsetP, p1, p2, p3, h));

                }

                else if (parameters[0] == "rect")
                {
                    offset_p = new Point(CoordSystem, Convert.ToDouble(parameters[1]), Convert.ToDouble(parameters[2]));
                    double lengthX = Convert.ToDouble(parameters[3]);
                    double lengthY = Convert.ToDouble(parameters[4]);
                    int h = Convert.ToInt32(parameters[5]);
                    shapes.Add(new Rectangle(offset_p, lengthX, lengthY, h)); ;
                }
                else if (parameters[0] == "cirslice")
                {
                    offset_p = new Point(CoordSystem, Convert.ToDouble(parameters[1]), Convert.ToDouble(parameters[2]));
                    double radius = Convert.ToDouble(parameters[3]);
                    double startAngle = Convert.ToDouble(parameters[4]);
                    double segmentAngle = Convert.ToDouble(parameters[5]);
                    int h = Convert.ToInt32(parameters[6]);
                    shapes.Add(new CircleSlice(offset_p, radius, startAngle, segmentAngle, h));
                }
                else if (parameters[0] == "cirsect")
                {
                    offset_p = new Point(CoordSystem, Convert.ToDouble(parameters[1]), Convert.ToDouble(parameters[2]));
                    double radius = Convert.ToDouble(parameters[3]);
                    double length = Convert.ToDouble(parameters[4]);
                    double startAngle = Convert.ToDouble(parameters[5]);
                    int h = Convert.ToInt32(parameters[6]);
                    shapes.Add(new Circlesection(offset_p, radius, length, startAngle, h));
                }
                else
                {
                    Console.WriteLine($"Ersten Parameter in Zeile {i} überprüfen!: {parameters[0]}");
                }
            }
            return shapes;
        }
        public void Display()
        {

            string info = $"Die Form besteht aus {Shapes.Count} Teilflächen: ";
            Console.WriteLine(info);
            foreach(Shape shape in Shapes)
            {
                Console.WriteLine(shape.ToString());
            }
            
        }

        public override void  Draw(ref Plot plt)
        {
            plt.PlotArrow(CombinedBP.X_Coord + 0.5, CombinedBP.Y_Coord + 0.5, 
                          CombinedBP.X_Coord + 5, CombinedBP.Y_Coord + 5,
                          label: "Ballancepoint", color: Color.Magenta);
            plt.PlotPoint(CombinedBP.X_Coord, CombinedBP.Y_Coord, Color.Magenta, markerSize: 7);
            plt.PlotText("BP", CombinedBP.X_Coord - 2, CombinedBP.Y_Coord + 1,color: Color.Magenta, fontSize: 22);
        }
        public void ShowImage()
        {
            var plt = new Plot(600, 600);
            plt.Axis(0, 40, 0, 40);
            foreach(Shape shape in Shapes)
            {
               shape.Draw(ref plt);
            }
            Draw(ref plt);
            
            plt.Title($"Ballancepoint");
            plt.Legend();

            plt.SaveFig(@"D:\IT-Unterricht\Programme\C#\Schwerpunnktsberechnung\Picture\CombinedShape.png");

            using var src = new Mat(@"D:\IT-Unterricht\Programme\C#\Schwerpunnktsberechnung\Picture\CombinedShape.png", ImreadModes.Color);
            using (new Window("ImageView", src))
            {
                Cv2.WaitKey();
            }
        }

        protected override double[] CalculateXCoords()
        {
            double[] x = new double[0];
            return x;
        }

        protected override double[] CalculateYCoords()
        {
            double[] x = new double[0];
            return x;
        }
    }
}

