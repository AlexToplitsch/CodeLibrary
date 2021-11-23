using System;
using System.Collections.Generic;
using Algorithmen;

namespace Lineare_Regression
{
    class Program
    {
        static void Main(string[] args)
        {
            DiagramPlotter plotter = new DiagramPlotter();
              
            List<FamilyData> liste = CSVSplitter.StoreData();
            int count = 0;

            foreach (var item in liste)
            {
                if (item.Sex == 'M')
                {
                    count++;
                }
            }

            double[] heightC = new double[count];
            double[] heightF = new double[count];

            int i = 0;
            foreach (var item in liste)
            {
                if (item.Sex == 'M')
                {
                    heightC[i] = item.ChildHeight;
                    if (item.MotherHeight > item.FatherHeight)
                    {
                        heightF[i] = (item.MotherHeight + item.FatherHeight) / 2;
                    }
                    else
                    {
                        heightF[i] = (item.FatherHeight + item.MotherHeight) / 2;
                    }

                    i++;
                }
            }

            LineareRegression line1 = new LineareRegression(heightF, heightC);
            double[,] arr = line1.CalcTrendLine(60, 80, 1);
            double[,] data = MakeDoubleArr(heightF, heightC);


            plotter.DrawData(data, false);
            plotter.DrawData(arr, true, "Height of parents[feet]", "Height of child[feet]");
            plotter.DrawPoint(50, 50);
            plotter.DrawPoint(50, 55);
            plotter.DrawPoint(50, 60);
            plotter.DrawText("KoVar: " + Convert.ToString(line1.KoVar), 50.5, 50);
            plotter.DrawText("Var: " + Convert.ToString(line1.XVar), 50.5, 55);
            plotter.DrawText("KorKoeff: " + Convert.ToString(line1.KorKoeff), 50.5, 60);
            plotter.OpenImage();
            
        }

        public static double[,] MakeDoubleArr(double[]arrX, double[] arrY)
        {
            double[,] arr = new double[arrX.Length, 2];
            for (int i = 0; i < arrX.Length; i++)
            {
                arr[i, 0] = arrX[i];
                arr[i, 1] = arrY[i];
            }

            return arr;
        }

        public static double[] CreateXData(int n, double range)
        {
            double[] arr = new double[n];
            Random rnd = new Random();

            for (int i = 0; i < n; i++)
            {
                arr[i] = rnd.NextDouble() * range;
            }
            return arr;
        }
    }
}
