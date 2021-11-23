using System;
using Entity_Framework.Classes;
using System.Collections.Generic;
using System.IO;
using System.Text.Json;
using Entity_Framework.Data;
using System.Linq;

namespace Entity_Framework
{
    class Program
    {
        static void Main(string[] args)
        {
            var persons_content = File.ReadAllText(@"Data\Persons_table.json");
            var c_cards_content = File.ReadAllText(@"Data\credit_cards_table.json");

            var persons = JsonSerializer.Deserialize<List<Person>>(persons_content);
            var credit_cards = JsonSerializer.Deserialize<List<Credit_Card>>(c_cards_content);

            var factory = new DbContext_factory();

            ShowAllUser(factory, 4);
            Console.WriteLine("Read Done");
            Console.ReadKey();
        }

        private static void ShowAllUser(DbContext_factory factory, int id)
        {
            using var db = factory.CreateDbContext();

            db.Persons.AsEnumerable().GroupBy(x => x.Birth_date).OrderByDescending(x => x.Key).ToList().ForEach(x => Console.WriteLine($"{x.Key} {x.Count()}"));

        }
    }
}
