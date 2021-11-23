using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace new_books.Entities
{
    public class Shipping_address : Address
    {
        public int ID { get; set; }
        public int CostumerID { get; set; }
    }
}
