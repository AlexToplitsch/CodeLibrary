using System;
using System.Collections.Generic;
using System.Globalization;
using System.Linq;
using System.Security.Cryptography.X509Certificates;
using System.Text;
using System.Threading.Tasks;
using System.IO;
using System.Security.Policy;

namespace Engine.Classes
{
    public class  Map
    {
        public Field[,] matrix = new Field[6, 5];
        public Map()
        {
            CreateFields();
            Set_Fieldneighbors();
        }
        

        //lässt nur noch die Objekte(Fields) übrig, welche befüllt werden
        private void CreateFields()
        { 
            for (int i = 0; i <= 5; i++)
            {
                for (int j = 0; j <= 4; j++)
                {
                    matrix[i, j] = new Field();
                }
            }
            
            // delete Fields
            matrix[0, 0] = null;
            matrix[0, 1] = null;
            matrix[2, 0] = null;
            matrix[2, 1] = null;
            matrix[2, 3] = null;
            matrix[3, 0] = null;
            matrix[3, 1] = null;
            matrix[3, 1] = null;
            matrix[4, 0] = null;
            matrix[4, 1] = null;
            matrix[4, 3] = null;
            matrix[4, 4] = null;
            matrix[5, 0] = null;
            matrix[5, 4] = null;
            matrix[1, 0] = null;
            matrix[1, 1] = null;

            //put info in Field
            for(int i = 0; i <= 5; i++)
            {
                matrix[i, 2].Txt_file_name = @"mainroad.txt";
            }
            matrix[0, 3].Txt_file_name = @"markt.txt";
            matrix[0, 4].Txt_file_name = @"markt.txt";
            matrix[1, 3].Txt_file_name = @"mainsquare.txt";
            matrix[1, 4].Txt_file_name = @"castle.txt";
            matrix[2, 4].Txt_file_name = @"church.txt";
            matrix[3, 3].Txt_file_name = @"school.txt";
            matrix[3, 4].Txt_file_name = @"monument.txt";
            matrix[5, 1].Txt_file_name = @"grenzlandheim.txt";
            matrix[5, 3].Txt_file_name = @"swim.txt";

            // picture in Field
            for (int i = 0; i <= 5; i++)
            {
                matrix[i, 2].Jpg_file_name = @"mainroad.jpg";
            }
            matrix[0, 3].Jpg_file_name = @"markt.jpg";
            matrix[0, 4].Jpg_file_name = @"markt.jpg";
            matrix[1, 3].Jpg_file_name = @"mainsquare.jpg";
            matrix[1, 4].Jpg_file_name = @"castle.jpg";
            matrix[2, 4].Jpg_file_name = @"church.jpg";
            matrix[3, 3].Jpg_file_name = @"school.jpg";
            matrix[3, 4].Jpg_file_name = @"monument.jpg";
            matrix[5, 1].Jpg_file_name = @"grenzlandheim.jpg";
            matrix[5, 3].Jpg_file_name = @"swim.jpg";

        }

        public void Set_Fieldneighbors()
        {
            for (int i = 0; i <= 5; i++)
            {
                for (int j = 0; j <= 4; j++)
                {   
                    if (j != 0) 
                    {
                        if (matrix[i, j] != null)
                        {
                            matrix[i, j].Upper_neighbor = matrix[i, j - 1];
                        }
                        
                    } 
                    if (j != 4)
                    {
                        if (matrix[i, j] != null)
                        {
                            matrix[i, j].Lower_neighbor = matrix[i, j + 1];
                        }
                    }
                    if (i != 0)
                    {
                        if (matrix[i, j] != null)
                        {
                            matrix[i, j].Left_neighbor = matrix[i - 1, j];
                        }
                    }
                    if (i != 5)
                    {
                        if (matrix[i, j] != null)
                        {
                            matrix[i, j].Right_neighbor = matrix[i + 1, j];
                        }
                    }
                }
            }
        }


        //schaut nach ob das obere Feld null oder ein Field ist
        public bool LookUp(int x, int y)
        {
            if (y == 0)
            {
                return false;
            }
            else if (matrix[y-1,x] == null)
            {
                return false;
            }
            else
            {
                return true;
            }
        }


        //schaut nach ob das untere Feld null oder ein Field ist
        public bool LookDown(int x, int y)
        { 
            if (y == 5)
            {
                return false;
            }
            else if (matrix[y + 1, x] == null)
            {
                return false;
            }
            else
            {
                return true;
            }
        }

        //schaut nach ob das linke Feld null oder ein Field ist
        public bool LookLeft(int x, int y)
        {
            if (x == 0)
            {
                return false;
            }
            else if (matrix[y, x-1] == null)
            {
                return false;
            }
            else
            {
                return true;
            }
        }


        //schaut nach ob das rechte Feld null oder ein Field ist
        public bool LookRight(int x, int y)
        {
            if (x == 4)
            {
                return false;
            }
            else if (matrix[y, x + 1] == null)
            {
                return false;
            }
            else
            {
                return true;
            }
        }
        public string ShowFieldInfo(int x, int y)
        {
            return matrix[y, x].ShowLocationInfo();
        }

        public string ShowFieldPicture(int x, int y)
        {
            return matrix[y, x].ShowLocationPicture();
        }
    }
}
