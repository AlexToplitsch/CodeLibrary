using System;
using System.Collections.Generic;
using System.Text;
using System.IO;

namespace ClassLibrary
{
    public class Player
    {
        Location Current_Location { get; set; }
        public int Health_points { set; get; }
        public int Damage_points { set; get; }
        public Player(int hp, int dp, )
        {
            Health_points = hp;
            Damage_points = dp;
        }
    }
}
