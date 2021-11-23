using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Design;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.Logging;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace new_books.Data
{
    public class DB_factory : IDesignTimeDbContextFactory<My_DB_Context> // bei Webapplikation nicht nötig, weil Dependency Injection
    {
        public My_DB_Context CreateDbContext(string[]? args = null)
        {
            var configuration = new ConfigurationBuilder().AddJsonFile("appsettings.json").Build();
            var optionsBuilder = new DbContextOptionsBuilder<My_DB_Context>();

            optionsBuilder
                .UseLoggerFactory(LoggerFactory.Create(builder => builder.AddConsole()))
                .UseSqlite(configuration.GetConnectionString("Conn"));

            return new My_DB_Context(optionsBuilder.Options);
        }
    }
}
