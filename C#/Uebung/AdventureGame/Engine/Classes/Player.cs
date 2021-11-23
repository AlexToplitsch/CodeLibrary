using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Engine.Classes
{
    public class Player
    {
        public int pos_x;
        public int pos_y;
        public int Hp { get; set; }
        public int Dp { get; set; }
        public string Name { get; set; }
        public Player(int x, int y, int hp, int dp, string name)
        {
            pos_x = x;
            pos_y = y;
            Hp = hp;
            Dp = dp;
            Name = name;
        }
        
        public int Move_East()
        {
            if (pos_x == 4)
            {
                return pos_x;
            }
            else
            {
                pos_x++;
                return pos_x;
            }
        }

        public int Move_West()
        {
            if (pos_x == 0)
            {
                return pos_x;
            }
            else
            {
                pos_x--;
                return pos_x;
            }

            
        }

        public int Move_North()
        {
            if (pos_y == 0)
            {
                return pos_y;
            }
            else
            {
                pos_y--;
                return pos_y;
            }
            
        }

        public int Move_South()
        {
            if (pos_y == 5)
            {
                return pos_y;
            }
            else
            {
                pos_y++;
                return pos_y;
            }
        }

        public string Get_Hit(int damage)
        {
            Random rand = new Random();
            int krit = rand.Next(0, 3);
            
            if (krit == 0)
            {
                Hp = Hp - damage;
                return Name + $" hat {damage} Schaden bekommen!";
            }
            else if (krit == 1)
            {
                Hp = Hp - (damage + 4);
                return Name + $" hat {damage + 4} Schaden bekommen!";
            }
            else
            {
                return Name + " ist ausgewichen!"; 
            }

        }
    }
}
