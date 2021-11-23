using System;
using System.Collections.Generic;
using System.Text;
using System.Text.Json.Serialization;

namespace Entity_Framework.Classes
{
    class Person
    {
        public int ID { get; set; }
        [JsonPropertyName("first_name")]
        public string First_name { get; set; }
        [JsonPropertyName("last_name")]
        public string Last_name { get; set; }
        [JsonPropertyName("birth_date")]
        public string Birth_date { get; set; }
        [JsonPropertyName("credit_card")]
        public string Card_number { get; set; }

    }
}
