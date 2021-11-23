using System;
using System.Collections.Generic;
using System.Text;
using System.IO;


namespace ClassLibrary
{
    public class Location
    {
        public int Id { get; set; }
        public string Name { get; set; } 
        public string Description { get; set; }
        public Location Location_to_north { get; set; }
        public Location Location_to_south { get; set; }
        public Location Location_to_west { get; set; }
        public Location Location_to_east { get; set; }

        public Location(int id, string name, string description)
        {
            Id = id;
            Name = name;
            Description = File.ReadAllText(description);
        }
    }
    
}
