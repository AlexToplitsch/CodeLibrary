using System;
using System.Collections.Generic;
using System.Text;
using System.IO;

namespace Algorithmen
{
    public class CSVSplitter
    {
        public static List<FamilyData> StoreData()
        {
            List<FamilyData> famData = new List<FamilyData>();
            string path = @"C:\Users\toplitsc\Desktop\galton.csv";

            using (StreamReader sr = new StreamReader(path))
            {
                while(sr.Peek() >= 0)
                {
                    try
                    {
                        string line = sr.ReadLine();
                        string[] data = line.Split(',');

                        data[1].Replace('.', ',');
                        data[2].Replace('.', ',');
                        data[4].Replace('.', ',');
                        famData.Add(new FamilyData(double.Parse(data[1], System.Globalization.CultureInfo.InvariantCulture), Convert.ToDouble(data[2], System.Globalization.CultureInfo.InvariantCulture), Convert.ToChar(data[3]), Convert.ToDouble(data[4], System.Globalization.CultureInfo.InvariantCulture)));
                    }
                    catch
                    {

                    }

                }
                return famData;
            }
        }
    }
}
