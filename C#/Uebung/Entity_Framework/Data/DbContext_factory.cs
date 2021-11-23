using System;
using System.Collections.Generic;
using System.Text;
using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Design;
using Microsoft.Extensions.Configuration;


namespace Entity_Framework.Data
{
    class DbContext_factory : IDesignTimeDbContextFactory<DB_context>
    {
        public DB_context CreateDbContext(string[] args = null)
        {
            var configuration = new ConfigurationBuilder().AddJsonFile("appsettings.json").Build();
            var optionsBuilder = new DbContextOptionsBuilder<DB_context>();

            optionsBuilder.UseSqlite(configuration.GetConnectionString("Conn"));

            return new DB_context(optionsBuilder.Options);
        }
    }
}
