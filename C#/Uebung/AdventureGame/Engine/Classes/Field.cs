using System;
using System.Collections.Generic;
using System.Dynamic;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Security.Cryptography.X509Certificates;
using System.Security.Policy;
using System.Text;
using System.Threading.Tasks;


namespace Engine.Classes
{
    public class Field
    {
        public string txt_folder = @"D:\IT-Unterricht\Programme\C#\AdventureGame\Engine\Info\";
        public string jpg_folder = @"D:\IT-Unterricht\Programme\C#\AdventureGame\Engine\Pictures\";
        public Field Upper_neighbor { get; set; }
        public Field Lower_neighbor { get; set; }
        public Field Left_neighbor { get; set; }
        public Field Right_neighbor { get; set; }
        
        public string Txt_file_name { get; set; }
        public string Jpg_file_name { get; set; }


        public Field()
        {
   
        }

        public string ShowLocationInfo()
        {
            string file = Path.Combine(txt_folder, Txt_file_name);
            string path = File.ReadAllText(file);
            return path;
        }

        public string ShowLocationPicture()
        {
            string path = Path.Combine(jpg_folder, Jpg_file_name);
            return path;
        }

    }
}
