using System;
using System.Collections.Generic;
using System.Text;
using Entity_Framework.Classes;
using Microsoft.EntityFrameworkCore;

namespace Entity_Framework.Data
{
    class DB_context : DbContext
    {
        public DB_context(DbContextOptions options) : base(options)
        {

        }

        public DbSet<Person> Persons { get; set; }

        public DbSet<Credit_Card> Credit_Cards { get; set; }

    }
}
