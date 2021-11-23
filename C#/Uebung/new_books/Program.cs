using new_books.Data;
using new_books.Utilities;
using System;
using System.IO;
using System.Text.Json;
using System.Collections.Generic;
using new_books.Entities;

namespace new_books
{
    class Program
    {
        static void Main(string[] args)
        {
            var factory = new DB_factory();

            Helper.CreateDB(factory, false);
            Helper.FillDB(factory, false);
            Helper.SelectData(factory, false, "Greece");
            Helper.InsertWithCheckEntries(factory);
            Console.WriteLine("Done");
            Console.ReadKey();

        }
    }
}
