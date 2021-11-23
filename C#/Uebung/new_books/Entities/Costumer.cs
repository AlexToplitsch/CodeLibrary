using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Text.Json.Serialization;
using System.Threading.Tasks;

namespace new_books.Entities
{
    public class Costumer
    {
        [JsonPropertyName("ID")]
        public int ID { get; set; }
        [JsonPropertyName("First_name")]
        public string First_name { get; set; }
        [JsonPropertyName("Last_name")]
        public string Last_name { get; set; }
        [JsonPropertyName("Email")]
        public string Email { get; set; }
        [JsonPropertyName("Company_address")]
        public Company_address Company_address { get; set; }
    }
}
