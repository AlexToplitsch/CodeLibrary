using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;

namespace LambdaExpressions
{
    public static class Helper
    {
        public static List<Employee> Create_dataset()
        {
            List<Employee> emps = new List<Employee>();
            var lines = File.ReadLines(@"D:\Programme\C#\Uebung\LambdaExpressions\MOCK_DATA (2).csv");
            List<string> text = lines.ToList();
            text.RemoveAt(0);
            foreach(string line in text)
            {
                var values = line.Split(",");
                emps.Add(new Employee(values[0], (char)values[1][0], Convert.ToBoolean(values[2]), Convert.ToInt32(values[3])));
            }
            return emps;
        }

        public static void Display_enum(IEnumerable<Employee>en)
        {
            Console.WriteLine("Count: " + Convert.ToString(en.Count()));
            foreach (var app in en)
            {
                Console.Write(app.Name + ", " + app.Birth_year + ", ");
                Console.WriteLine(app.Gender);
            }
        }
    }
}
