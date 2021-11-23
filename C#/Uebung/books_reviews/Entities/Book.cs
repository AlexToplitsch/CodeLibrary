using books_reviews.Entities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Text.Json.Serialization;

namespace books_reviews.Classes
{
    public class Book
    {
        public int ID { get; set; }
        [JsonPropertyName("Title")]
        public string Title { get; set; }
        [JsonPropertyName("Published")]
        public string Published {get; set;}
        [JsonPropertyName("Rev")]
        public ICollection<Review> Rev { get; set; }
    }
}
