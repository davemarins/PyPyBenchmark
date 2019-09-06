var http = require('http');

http.createServer(function (req, res) {
  var string = 'Hello Euro Python 2019!';
  var d1 = new Date();
  var start = d1.getMilliseconds();
  for(var i = 0; i < 1000000; i++) {
    string = 'Hello Euro Python 2019!';
  }
  var d2 = new Date();
  var end = d2.getMilliseconds();
  res.write('String output in JS in ' + (end - start) + ' ms\n');
  res.end();
}).listen(8080);
