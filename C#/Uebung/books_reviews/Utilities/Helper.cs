using books_reviews.Data;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace books_reviews.Utilities
{
    public class Helper
    {
        internal static void CreateDB(Context_factory factory)
        {
            using var db = factory.CreateDbContext();
            {
                db.Database.EnsureDeleted();
                db.Database.EnsureCreated();
            }
        }
    }
}
