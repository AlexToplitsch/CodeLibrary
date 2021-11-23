using Microsoft.EntityFrameworkCore;
using new_books.Data;
using new_books.Entities;
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Text.Json;
using System.Threading.Tasks;

namespace new_books.Utilities
{

    public class Helper
    {
        internal static void CreateDB(DB_factory factory, bool create)
        {
            if (create)
            {
                using var db = factory.CreateDbContext();
                {
                    db.Database.EnsureDeleted();
                    db.Database.EnsureCreated();
                }
                Console.WriteLine("SQLite DB created!");
            }
        }

        internal static void FillDB(DB_factory factory, bool fill)
        {
            if (fill)
            {
                var file = File.ReadAllText(@"D:\\Programme\\C#\\Uebung\\new_books\\Data\\Costumer.json");
                var content = JsonSerializer.Deserialize<List<Costumer>>(file);
                using var db = factory.CreateDbContext();
                {
                    db.Costumers.AddRange(content);
                    db.SaveChanges();
                }
                Console.WriteLine("DB filled with content");
            }
        }

        internal static void SelectData(DB_factory factory, bool select, string city)
        {
            if (select)
            {
                using var db = factory.CreateDbContext();
                {
                    var content = db.Costumers.Include(x => x.Company_address)
                        .Where(c => c.Company_address.City == city)
                        .ToList();

                    foreach (var item in content)
                    {
                        Console.WriteLine($"{item.First_name} {item.Last_name}\n" +
                                          $"{item.Company_address.City} "); 
                    }
                }
            }
        }

        internal static void InsertWithCheckEntries(DB_factory factory)
        {
            using var db = factory.CreateDbContext();
            {
                var file = File.ReadAllText(@"D:\\Programme\\C#\\Uebung\\new_books\\Data\\Costumer.json");
                var content = JsonSerializer.Deserialize<List<Costumer>>(file);
                foreach( var item in content)
                {
                    if (db.Costumers.FirstOrDefault(x => x.Email == item.Email) != null)
                    {
                        db.Costumers.Add(item);
                        db.SaveChanges();
                    }
                    else
                    {
                        Console.WriteLine("Entry already exists");
                    }
                }
            }
        }
    }

}
