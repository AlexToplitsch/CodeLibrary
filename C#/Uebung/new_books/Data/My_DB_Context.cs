using Microsoft.EntityFrameworkCore;
using new_books.Entities;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace new_books.Data
{
    public class My_DB_Context : DbContext
    {
        public My_DB_Context(DbContextOptions options) : base(options)
        {
            
        }
        public DbSet<Costumer> Costumers { get; set; }
    }
}
