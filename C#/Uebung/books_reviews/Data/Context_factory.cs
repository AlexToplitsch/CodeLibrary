using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Design;
using Microsoft.Extensions.Configuration;

namespace books_reviews.Data
{
    class Context_factory : IDesignTimeDbContextFactory<Books_DBContext>
    {
        public Books_DBContext CreateDbContext(string[]? args = null)
        {
            var configuration = new ConfigurationBuilder().AddJsonFile("appsettings.json").Build();
            var optionsBuilder = new DbContextOptionsBuilder<Books_DBContext>();

            optionsBuilder.UseSqlite(configuration.GetConnectionString("Conn"));

            return new Books_DBContext(optionsBuilder.Options); 
        }
    }
}
