using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace LambdaExpressions
{
    public class Employee
    {
        public Employee(string name, char gender, bool apprentice, int birth_year)
        {
            Name = name;
            Gender = gender;
            Apprentice = apprentice;
            Birth_year = birth_year;
        }

        public string Name { get; }
        public char Gender { get; }
        public bool Apprentice { get; }
        public int Birth_year { get; }
    }
}
