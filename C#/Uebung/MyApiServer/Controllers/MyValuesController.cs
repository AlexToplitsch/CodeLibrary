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
    public class MyValuesController : ControllerBase
    {
        // GET: api/<MyValuesController>
        [HttpGet]
        public IEnumerable<string> Get()
        {
            return new string[] { "value1", "value2" };
        }

        // GET api/<MyValuesController>/5
        [HttpGet("{id}")]
        public string Get(int id)
        {
            return "value";
        }

        // POST api/<MyValuesController>
        [HttpPost]
        public void Post([FromBody] string value)
        {
        }

        // PUT api/<MyValuesController>/5
        [HttpPut("{id}")]
        public string Put(int id, [FromBody] string value)
        {
            return value;
        }

        // DELETE api/<MyValuesController>/5
        [HttpDelete("{id}")]
        public void Delete(int id)
        {
        }
    }
}
