using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using LoginApp.Modules;
using LoginApp.Data;
using System.Security.Cryptography;
using System.Text;

namespace LoginApp.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class AccountController : ControllerBase
    {
        public User ExistUser { get; set; }

        private readonly DataContext _context;

        public AccountController(DataContext context)
        {
            ExistUser = new User() { Username = "alex", Password = "123" };
            _context = context;
        }

        [HttpGet]
        public string Test()
        {
            return "Funkt";
        }

        [HttpPost("login")]
        public ActionResult CompareUserdata([FromBody] User user)
        {
            //compare password mit HMACSHA512(user.PasswordSalt); user.PasswordSalt-->ist der byte[] verschlüsseln
            //hma.ComputeHash(Encoding.UTF8.GetBytes(registeredUser.Password)) vergleich mit hma.ComputeHash(Encoding.UTF8.GetBytes(user.Password));
            if (_context.Users.Where(f => f.Username == user.Username).SingleOrDefault() != null)
            {
                return Ok("cola");
            }
            else
            {
                return NotFound("Hallo");
            }
            
            

        }

        [HttpPost("signin")]
        public void CreateUserdata([FromBody] RegisterModel user)
        {
            using var hma = new HMACSHA512();//wenn kein using mit {} muss man bei dem HMCSHA512 die Dispose funktion aufrufen, um das wieder freizugeben
            {
                user.PasswordSalt = hma.Key;
                user.PasswordHash = hma.ComputeHash(Encoding.UTF8.GetBytes(user.Password));
            }
            _context.Users.Add(user);//insert nach jeder änderung braucht man ein SaveChanges
            _context.SaveChanges(); //commit 
        }

    }
}