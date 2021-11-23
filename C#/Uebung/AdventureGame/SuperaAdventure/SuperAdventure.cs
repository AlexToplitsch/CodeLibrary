using Engine.Classes;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace SuperaAdventure
{
    public partial class SuperAdventure : Form
    {

        private Player buddy;
        public Player enemy;
        private Map map;
        
        public SuperAdventure()
        {
            InitializeComponent();
            buddy = new Player(2, 3, 100, 7, "Alex" );
            enemy = new Player(4, 1, 100, 7, "Gollum");
            map = new Map();
        }
        

        private void SuperAdventure_Load(object sender, EventArgs e)
        {

        }

       
        private void btnNorth_Click_1(object sender, EventArgs e)
        {
            buddy.Move_North();
            Visability();
            Projection();
        }

        private void btnWest_Click(object sender, EventArgs e)
        {
            buddy.Move_West();
            Visability();
            Projection();
        }
        private void btnEast_Click(object sender, EventArgs e)
        {
            buddy.Move_East();
            Visability();
            Projection();

        }

        private void btnSouth_Click(object sender, EventArgs e)
        {
            buddy.Move_South();
            Visability();
            Projection();
        }

        private void pictBox_Street_Click(object sender, EventArgs e)
        {

        }

        private void TxtBox_Info_TextChanged(object sender, EventArgs e)
        {

        }

        private void Btn_Fight_Click(object sender, EventArgs e)
        {
            Fight();
        }

        private void Visability()
        {
            btnNorth.Visible = map.LookUp(buddy.pos_x, buddy.pos_y);
            btnWest.Visible = map.LookLeft(buddy.pos_x, buddy.pos_y);
            btnEast.Visible = map.LookRight(buddy.pos_x, buddy.pos_y);
            btnSouth.Visible = map.LookDown(buddy.pos_x, buddy.pos_y);
        } 

        private void Projection()
        {
            if (enemy != null)
            {
                if (buddy.pos_x == enemy.pos_x && buddy.pos_y == enemy.pos_y)
                {
                    Btn_Fight.Visible = true;
                    TxtBox_Info.Text = "Achtung ein Gegner!";
                    pictBox_Street.Image = Image.FromFile(@"D:\IT-Unterricht\Programme\C#\AdventureGame\Engine\Pictures\monster.jpg");
                    btnNorth.Visible = false;
                    btnWest.Visible = false;
                    btnEast.Visible = false;
                    btnSouth.Visible = false;
                }
                else
                {
                    TxtBox_Info.Text = map.ShowFieldInfo(buddy.pos_x, buddy.pos_y);
                    pictBox_Street.Image = Image.FromFile(map.ShowFieldPicture(buddy.pos_x, buddy.pos_y));
                }
            }
            else
            {
                TxtBox_Info.Text = map.ShowFieldInfo(buddy.pos_x, buddy.pos_y);
                pictBox_Street.Image = Image.FromFile(map.ShowFieldPicture(buddy.pos_x, buddy.pos_y));
            }
        }

        private void Fight()
        {
            
            TxtBox_Info.Text = $"{enemy.Get_Hit(buddy.Dp)} \n {buddy.Get_Hit(enemy.Dp)}";
            if ( enemy.Hp <= 0)
            {
                TxtBox_Info.Text = "Gratulation! Sie haben den Gegner besiegt!";
                pictBox_Street.Image = Image.FromFile(map.ShowFieldPicture(buddy.pos_x, buddy.pos_y));
                enemy = null;
                Btn_Fight.Visible = false;

                btnNorth.Visible = true;
                btnWest.Visible = true;
                btnSouth.Visible = true;
            }

            else if (buddy.Hp <= 0)
            {
                TxtBox_Info.Text = "Sie haben leider verloren!";
                Btn_Fight.Visible = false;
                btnEast.Visible = false;
                btnNorth.Visible = false;
                btnSouth.Visible = false;
                btnWest.Visible = false;
                pictBox_Street.Image = Image.FromFile(@"D:\IT-Unterricht\Programme\C#\AdventureGame\Engine\Pictures\scull.jpg");
            }
        }
    }
}
