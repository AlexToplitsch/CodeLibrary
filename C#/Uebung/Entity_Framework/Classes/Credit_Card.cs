using System;
using System.Collections.Generic;
using System.Text;
using System.Text.Json.Serialization;

namespace Entity_Framework.Classes
{
    class Credit_Card
    {
        public int ID { get; set; }
        [JsonPropertyName("owner")]
        public string Owner { get; set; }
        [JsonPropertyName("card_number")]
        public string Card_number { get; set; }
        [JsonPropertyName("valid_thru")]
        public string Valid_thru { get; set; }
    }
}
