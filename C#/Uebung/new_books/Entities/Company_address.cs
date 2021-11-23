using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations.Schema;
using System.Linq;
using System.Text;
using System.Text.Json.Serialization;
using System.Threading.Tasks;

namespace new_books.Entities
{
    [Table("Company_addresses")] //Data annotation um die Tabelle anders zu bennen als die Klasse heißt
    public class Company_address : Address
    {
        [JsonPropertyName("ID")]
        public int ID { get; set; }
    }
}
