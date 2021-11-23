using System;
using System.Collections.Generic;
using System.Text;
using ScottPlot;
using OpenCvSharp;
using ScottPlot.Drawing;
using System.Linq;

namespace Algorithmen
{
    public class DiagramPlotter
    {
        private double[] XData { get; set;}
        private double[] YData { get; set; }
        private Plot Screen { get; set; }
        private bool Line { get; set; }

        public DiagramPlotter()
        {
            Screen = new Plot();
            Screen.Style(Style.Gray1);
            Screen.Colorset(Colorset.OneHalfDark);
        }
        public void ClearScreen()
        {
            Screen = new Plot();
        }

        public void DrawData(double[,] data, bool line, string xAxis = "X", string yAxis = "Y")
        {
            if (IsDataValid(data))
            {
                Line = line;
                SplitData(data);
                Draw(xAxis, yAxis);
            }
            return;
        }

        public void DrawPoint(double x, double y, string label_ = "")
        {
            try
            {
                x += XData.Min();
                y += YData.Min();
            }
            catch
            {

            }

            Screen.PlotPoint(x, y, label: label_, color: System.Drawing.Color.LightBlue);
        }

        public void DrawText(string txt, double x, double y)
        {

            Screen.PlotText(txt, x, y, color: System.Drawing.Color.LightBlue);
        }

        private void Draw(string xAxis, string yAxis)
        {
            if (!Line)
            {
                Screen.PlotScatter(XData, YData, lineStyle: LineStyle.None);
            }
            else
            {
                Screen.PlotScatter(XData, YData);
            }
            Screen.AxisAuto();
            Screen.XLabel(xAxis);
            Screen.YLabel(yAxis);
            Screen.SaveFig(@"D:\Programme\C#\Projekte\Lineare Regression\linear.png");
        }

        public void OpenImage()
        {
            
            using Mat src = new Mat(@"D:\Programme\C#\Projekte\Lineare Regression\linear.png");
            using Mat dst = new Mat();
            Cv2.Canny(src, dst, 50, 200);
            using (new Window("src image", src))
            {
                Cv2.WaitKey();
            }
        }

        private bool IsDataValid(double[,] arr)
        {
            if (arr.Length % 2 != 0)
            {
                return false;
            }
            try
            {
                Console.WriteLine(arr[0, 3]);
                return false;
            }
            catch 
            {
                return true;
            }
        }

        private void SplitData(double[,] arr)
        {
            int i = 0;
            int j = 0;
            double[] xData = new double[arr.Length / 2];
            double[] yData = new double[arr.Length / 2];
            foreach (double item in arr)
            {
                if (i % 2 == 0)
                {
                    xData[j] = item;
                }
                else
                {
                    yData[j] = item;
                    j++;
                }
                i++;
            }
            XData = xData;
            YData = yData;
        }
    }
}
