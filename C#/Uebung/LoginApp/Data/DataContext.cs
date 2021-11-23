using Microsoft.EntityFrameworkCore;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using LoginApp.Modules;
using System.Diagnostics.CodeAnalysis;

namespace LoginApp.Data
{
    public class DataContext : DbContext // verknüpfung mit Entity Framework Core (Vererbung)
    {
        public DataContext([NotNullAttribute] DbContextOptions options) : base(options)
        {
        }

        public DbSet<RegisterModel> Users { get; set; }
    }
}
