using System;
using System.IO;
using System.Text;

namespace ClassLibrary
{
    public class World
    {

        public const int LOCATION_ID_MAINROAD1 = 1;
        public const int LOCATION_ID_MAINROAD2 = 2;
        public const int LOCATION_ID_MAINROAD3 = 3;
        public const int LOCATION_ID_MAINROAD4 = 4;
        public const int LOCATION_ID_MAINROAD5 = 5;
        public const int LOCATION_ID_MAINROAD6 = 6;
        public const int LOCATION_ID_GRENZLANDHEIM = 7;
        public const int LOCATION_ID_FREIBAD = 8;
        public const int LOCATION_ID_SCHOOL = 9;
        public const int LOCATION_ID_MONUMENT = 10;
        public const int LOCATION_ID_CHURCH = 11;
        public const int LOCATION_ID_CASTLE = 12;
        public const int LOCATION_ID_MARKT = 13;
        public const int LOCATION_ID_MARKT1 = 14;
        public const int LOCATION_ID_MAINSQUARE = 15;
        public World()
        {
            SetLocations();
        }

        public void SetLocations()
        {
            string folder = @"D:\IT-Unterricht\Programme\C#\RPG\ClassLibrary\Info\";
            Location mainroad1 = new Location(LOCATION_ID_MAINROAD1, "Hauptstraße\n", Path.Combine(folder, @"mainroad.txt"));
            Location mainroad2 = new Location(LOCATION_ID_MAINROAD2, "Hauptstraße\n", Path.Combine(folder, @"mainroad.txt"));
            Location mainroad3 = new Location(LOCATION_ID_MAINROAD3, "Hauptstraße\n", Path.Combine(folder, @"mainroad.txt"));
            Location mainroad4 = new Location(LOCATION_ID_MAINROAD4, "Hauptstraße\n", Path.Combine(folder, @"mainroad.txt"));
            Location mainroad5 = new Location(LOCATION_ID_MAINROAD5, "Hauptstraße\n", Path.Combine(folder, @"mainroad.txt"));
            Location mainroad6 = new Location(LOCATION_ID_MAINROAD6, "Hauptstraße\n", Path.Combine(folder, @"mainroad.txt"));
            Location grenzlandheim = new Location(LOCATION_ID_GRENZLANDHEIM, "Grenzlandheim\n",Path.Combine(folder, @"grentlandheim.txt"));
            Location freibad = new Location(LOCATION_ID_FREIBAD, "Freibad\n", Path.Combine(folder, @"swim.txt"));
            Location school = new Location(LOCATION_ID_SCHOOL, "Schule\n", Path.Combine(folder, @"school.txt"));
            Location monument = new Location(LOCATION_ID_MONUMENT, "Kriegerdenkmal\n", Path.Combine(folder, @"monument.txt"));
            Location church = new Location(LOCATION_ID_CHURCH, "Kirche\n", Path.Combine(folder, @"church.txt"));
            Location castle = new Location(LOCATION_ID_CASTLE, "Schloss\n", Path.Combine(folder, @"castle.txt"));
            Location markt = new Location(LOCATION_ID_MARKT, "Marktwiese\n", Path.Combine(folder, @"markt.txt"));
            Location markt1 = new Location(LOCATION_ID_MARKT1, "Marktwiese\n", Path.Combine(folder, @"markt.txt"));
            Location mainsquare = new Location(LOCATION_ID_MAINSQUARE, "Hauptplatz\n", Path.Combine(folder, @"mainsquare.txt"));

            //Locations verbinden
            //mainroad1
            mainroad1.Location_to_north = mainroad2;
            mainroad1.Location_to_west = grenzlandheim;
            mainroad1.Location_to_east = freibad;
            //mainroad2
            mainroad2.Location_to_north = mainroad3;
            mainroad2.Location_to_south = mainroad1;
            //mainroad3
            mainroad3.Location_to_north = mainroad4;
            mainroad3.Location_to_south = mainroad2;
            mainroad3.Location_to_east = school;
            //mainroad4
            mainroad4.Location_to_north = mainroad5;
            mainroad4.Location_to_south = mainroad3;
            //mainroad5
            mainroad5.Location_to_north = mainroad6;
            mainroad5.Location_to_south = mainroad4;
            mainroad5.Location_to_east = mainsquare;
            //mainroad6
            mainroad6.Location_to_east = markt1;
            mainroad6.Location_to_south = mainroad5;
            //grenzlandheim
            grenzlandheim.Location_to_east = mainroad1;
            //freibad
            freibad.Location_to_west = mainroad1;
            //school
            school.Location_to_west = mainroad3;
            school.Location_to_east = monument;
            //monument
            monument.Location_to_west = school;
            monument.Location_to_north = church;
            //church
            church.Location_to_north = castle;
            church.Location_to_south = monument;
            //castle
            castle.Location_to_north = markt;
            castle.Location_to_south = church;
            castle.Location_to_west = mainsquare;
            //markt
            markt.Location_to_south = castle;
            markt.Location_to_west = markt1;
            //markt1
            markt1.Location_to_south = mainsquare;
            markt1.Location_to_west = mainroad6;
            markt1.Location_to_east = markt;
            //mainsqaure
            mainsquare.Location_to_north = markt1;
            mainsquare.Location_to_west = mainroad5;
            mainsquare.Location_to_east = castle;

        }
    }
}
