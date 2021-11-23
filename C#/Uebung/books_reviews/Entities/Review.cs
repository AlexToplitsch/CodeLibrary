using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Text.Json.Serialization;

namespace books_reviews.Entities
{
    public class Review
    {
        public int ID { get; set; }
        [JsonPropertyName("Stars")]
        public int Stars { get; set; }
        [JsonPropertyName("Remark")]
        public string Remark { get; set; }
        [JsonPropertyName("BookID")]
        public int BookID { get; set; }
    }
}

