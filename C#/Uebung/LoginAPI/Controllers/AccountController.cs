using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using LoginAPI.Modules;
using System.Security.Cryptography;
using System.Text;
using LoginAPI.Data;

// For more information on enabling Web API for empty projects, visit https://go.microsoft.com/fwlink/?LinkID=397860

namespace LoginAPI.Modules
{
    [Route("api/[controller]")]
    [ApiController]
    public class AccountController : ControllerBase
    {
        private readonly DataContext _context; 

        public AccountController(DataContext context)
        {
            _context = context;
        }

        // GET: api/<AccountController>
        [HttpGet]
        public string Get()
        {
            return "This one works!";
        }

        // GET api/<AccountController>/5
        [HttpGet("{id}")]
        public string Get(int id)
        {
            return "value";
        }


        //Compares the userdat from client with database
        [HttpPost("login")]
        public ActionResult CompareUserdata([FromBody] User user)
        {
            return Ok();
        }

        // POST api/<AccountController>
        [HttpPost("signin")]
        public ActionResult Post([FromBody] User user)
        {
            using var hmac = new HMACSHA512();
            {
                user.PasswordSalt = hmac.Key;
                user.PasswordHash = hmac.ComputeHash(Encoding.UTF8.GetBytes(user.Password));
            }

            _context.Add(user);
            _context.SaveChanges();
            return Ok("Insert");
        }

        // PUT api/<AccountController>/5
        [HttpPut("{id}")]
        public void Put(int id, [FromBody] string value)
        {
        }

        // DELETE api/<AccountController>/5
        [HttpDelete("{id}")]
        public void Delete(int id)
        {
        }
    }
}
