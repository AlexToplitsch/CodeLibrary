using books_reviews.Classes;
using books_reviews.Data;
using books_reviews.Entities;
using System.Collections.Generic;
using books_reviews.Utilities;
using System;
using System.Linq;
using Microsoft.EntityFrameworkCore;
using System.Text.Json;
using System.IO;

namespace books_reviews
{
    class Program
    {
        static void Main(string[] args)
        { 

            var content = File.ReadAllText(@"D:\Programme\C#\Übungen\books_reviews\Data\Books.json");
            var books = JsonSerializer.Deserialize<List<Book>>(content);
            //foreach(var item in books)  
            //{
            //    Console.WriteLine(item.Title);
            //}
            //var book = new Book() { ID = 1, Title = "Mercedes Killer" };
            //var rev = new Review();
            //rev.Stars = 3;
            //book.Rev = new List<Review>();
            //book.Rev.Add(new Review() { Stars = 4, Remark = "Hallo" });

            var factory = new Context_factory();

            using var db = factory.CreateDbContext();

            //db.Books_table.Add(book);
            //db.SaveChanges();

            //var db_book = db.Books_table    
            //    .Include(x => x.Rev) // inkludiert die abhängige Tabelle Rev_Table
            //    .Where(x => x.ID == 1) // where Befehl
            //    .Single(); // gibt nur ein Element zurück

            //db_book.Rev.Add(new Review() { Stars = 2, Remark = "New Rev"}); // dem Buch eine neue Review hinzufügen

            //db.Rev_table.Add(db_book.Rev.ElementAt(1)); // zweites Review Element aus dem Buch in die Tabelle speichern 
            db.Books_table.AddRange(books);
            db.SaveChanges();

            Console.WriteLine("Done");

            Console.ReadKey();
        }
    }
}
