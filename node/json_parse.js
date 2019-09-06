var http = require('http');

http.createServer(function (req, res) {
  var d1 = new Date();
  var start = d1.getMilliseconds();
  for(var i = 0; i < 1000000; i++) {
    var obj = { userID: 1, id: 1, title: "delectus aut autem", completed: false };
    var jsonString = JSON.stringify(obj);
    var jsonReal = JSON.parse(jsonString);
  }
  var d2 = new Date();
  var end = d2.getMilliseconds();
  res.write('JSON output in JS in ' + (start - end) + ' - ' + (end - start) + ' ms\n');
  res.end();
}).listen(8080);
