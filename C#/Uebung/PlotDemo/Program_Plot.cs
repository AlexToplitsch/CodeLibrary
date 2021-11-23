using System;
using OpenCvSharp;
using ScottPlot;
namespace PlotDemo
{
    class Program
    {
        static void Main(string[] args)
        {
            var plt = new ScottPlot.Plot(600, 400);

            int pointCount = 51;
            double[] x = DataGen.Consecutive(pointCount);
            double[] sin = DataGen.Sin(pointCount);
            double[] cos = DataGen.Cos(pointCount);

            plt.PlotScatter(x, sin);
            plt.PlotScatter(x, cos);

            plt.AxisAuto(horizontalMargin: 0.5, verticalMargin: 0.5);


            plt.SaveFig(@"D:\IT-Unterricht\Programme\C#\PlotDemo\PlotTypes_Polygon_Quickstart.png");

            plt.SaveFig("Customize_AxisLimits_Manual.png");
            using var src = new Mat(@"D:\IT-Unterricht\Programme\C#\PlotDemo\PlotTypes_Polygon_Quickstart.png", ImreadModes.Color);
            using (new Window("ImageView", src))
            {
                Cv2.WaitKey();
            }
        }
    }
}
