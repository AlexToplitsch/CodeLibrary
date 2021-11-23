using System;
using System.Collections.Generic;
using System.Text;

namespace Algorithmen
{
    public class LineareRegression
    {
        public double X_ { get; private set; }
        public double Y_ { get; private set; }
        public double KoVar { get; private set; }
        public double XVar { get; private set; }
        public double YVar { get; private set; }
        public double B1 { get; private set; }
        public double B0 { get; private set; }
        public double KorKoeff { get; private set; }

        public LineareRegression(double[] xData, double[] yData)
        {
            LinearInit(xData, yData);
        }

        private void LinearInit(double[] xData, double[] yData)
        {
            CalcXMid(xData);
            CalcYMid(yData);
            CalcXVar(xData);
            CalcYVar(yData);
            CalcKoVar(xData, yData);
            CalcB1();
            CalcB0();
            CalcKorKoeff();
        }

        private void CalcKorKoeff()
        {
            KorKoeff = KoVar / Math.Sqrt(XVar * YVar);
        }

        private void CalcB0()
        {
            B0 = Y_ - B1 * X_;
        }

        private void CalcB1()
        {
            B1 = KoVar / XVar;
        }

        private void CalcXMid(double[] xData)
        {
            double sum = 0;
            for( int i = 0; i < xData.Length; i++)
            {
                sum += xData[i];
            }
            X_ =  sum / xData.Length;
        }

        private void CalcYMid(double[] yData)
        {
            double sum = 0;
            for (int i = 0; i < yData.Length; i++)
            {
                sum += yData[i];
            }
            Y_ = sum / yData.Length;
        }

        private void CalcXVar(double[] xData)
        {
            double sum = 0;
            for (int i = 0; i < xData.Length; i++)
            {
                sum += Math.Pow(xData[i] - X_, 2);
            }
            XVar = sum;
        }

        private void CalcYVar(double[] yData)
        {
            double sum = 0;
            for (int i = 0; i < yData.Length; i++)
            {
                sum += Math.Pow(yData[i] - Y_, 2);
            }

            YVar = sum;
        }

        private void CalcKoVar(double[] xData, double[] yData)
        {
            double sum = 0;
            for(int i = 0; i < xData.Length; i++)
            {
                sum += (xData[i] - X_) * (yData[i] - Y_);
            }
            KoVar = sum;
        }

        public double[,] CalcTrendLine(double minX, double maxX, double steps)
        {
            int n = Convert.ToInt32((maxX - minX) / steps) + 1; //anzahl der Daten
            double data = minX;
            double[,] arr = new double[n, 2];
            for (int i = 0; i < n; i++)
            {
                arr[i, 0] = data;
                arr[i, 1] = B0 + B1 * data;
                data += steps;
            }
            return arr;
        }
    }
}
