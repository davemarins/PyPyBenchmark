var http = require('http');

http.createServer(function (req, res) {
  var result = 1;
  var d1 = new Date();
  var start = d1.getMilliseconds();
  for(var i = 0; i < 1000000; i++) {
      if(result == 0) {
        result = 1;
      } else {
        result = (10*2)/result;
      }
  }
  var d2 = new Date();
  var end = d2.getMilliseconds();
  res.write('Calculation output in JS in ' + (end - start) + ' ms\n');
  res.end();
}).listen(8080);
