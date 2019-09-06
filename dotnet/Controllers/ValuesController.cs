using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;

// dotnet add package Newtonsoft.Json
using Newtonsoft.Json;

namespace dotnet.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class ValuesController : ControllerBase
    {

        public const int Times = 1000000;

        // GET api/values
        [HttpGet]
        public ActionResult<string> Get()
        {
            string result = "";

            DateTime stringStart = DateTime.Now;
            for(int i = 0; i < Times; i++) {
                string tempString = "Hello Euro Python 2019!";
            }
            DateTime stringEnd = DateTime.Now;
            result += "String output in .NET in " + (stringEnd - stringStart)*100/1000000 + " ms\n";

            var myJson = new {
                userId = 1,
                id = 1,
                title = "delectus aut autem",
                completed = false
            };
            string myJsonReal = null;
            DateTime jsonEncodeStart = DateTime.Now;
            for(int i = 0; i < Times; i++) {
                myJsonReal = JsonConvert.SerializeObject(myJson);
            }
            DateTime jsonEncodeEnd = DateTime.Now;
            result += "JSON encode in .NET in " + (jsonEncodeEnd - jsonEncodeStart)*100/1000000 + " ms\n";
            
            DateTime jsonDecodeStart = DateTime.Now;
            for(int i = 0; i < Times; i++) {
                string jsonResult = JsonConvert.SerializeObject(myJsonReal);
            }
            DateTime jsonDecodeEnd = DateTime.Now;
            result += "JSON decode in .NET in " + (jsonDecodeEnd - jsonDecodeStart)*100/1000000 + " ms\n";

            int tempCalc = 1;
            DateTime calcStart = DateTime.Now;
            for(int i = 0; i < Times; i++) {
                if(tempCalc == 0) tempCalc = 1;
                tempCalc = (10*2)/tempCalc;
            }
            DateTime calcEnd = DateTime.Now;
            result += "Calculation output in .NET in " + (calcEnd - calcStart)*100/1000000 + " ms\n";

            return result;
        }
    }
}
