using books_reviews.Classes;
using books_reviews.Entities;
using Microsoft.EntityFrameworkCore;
using System;
using System.Collections.Generic;
using System.Diagnostics.CodeAnalysis;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace books_reviews.Data
{
    public class Books_DBContext : DbContext
    {
        public Books_DBContext(DbContextOptions options) : base(options)
        {

        }

        public DbSet<Book> Books_table { get; set; } //erzeugen einer Tabelle aus dem Entity Book
        public DbSet<Review> Rev_table { get; set; } //erzeugen einer Tabelle aus dem Entity Review
    }
}
