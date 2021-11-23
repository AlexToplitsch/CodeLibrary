using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Text.Json.Serialization;
using System.Threading.Tasks;

namespace new_books.Entities
{
    public class Address
    {
        [JsonPropertyName("Street")]
        public string Street { get; set; }
        [JsonPropertyName("StrtNr")]
        public string StrtNr { get; set; }
        [JsonPropertyName("City")]
        public string City { get; set; }
        [JsonPropertyName("Postal_code")]
        public string Postal_code { get; set; }
    }
}
