using System;
using System.Collections.Generic;
using System.Text;

namespace Algorithmen
{
    public class FamilyData
    {
        public double FatherHeight { get; private set; }
        public double MotherHeight { get; private set; }
        public char Sex { get; private set; }
        public double ChildHeight { get; private set; }

        public FamilyData(double fatherH, double motherH, char sex, double childH)
        {
            FatherHeight = fatherH;
            MotherHeight = motherH;
            Sex = sex;
            ChildHeight = childH;
        }
    }
}
