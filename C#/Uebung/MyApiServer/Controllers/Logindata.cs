using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;

// For more information on enabling Web API for empty projects, visit https://go.microsoft.com/fwlink/?LinkID=397860

namespace MyApiServer.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class Logindata : ControllerBase
    {

        public string userName = "alexT";
        public string password = "test123";


        // GET: api/<Logindata>
        [HttpGet]
        public IEnumerable<string> Get()
        {
            return new string[] { "value1", "value2" };
        }

        // GET api/<Logindata>/5
        [HttpGet("{id}")]
        public string Get(int id)
        {
            return "value";
        }

        // POST api/<Logindata>
        [HttpPost]
        public bool Post([FromBody] string uN, string pw)
        {
            if(uN == userName && pw == password)
            {
                return true;
            }
            else
            {
                return false;
            }
        }

        // PUT api/<Logindata>/5
        [HttpPut("{id}")]
        public void Put(int id, [FromBody] string value)
        {
        }

        // DELETE api/<Logindata>/5
        [HttpDelete("{id}")]
        public void Delete(int id)
        {
        }
    }
}
