/*


*/
var http = require('http'),
      fs = require('fs'),
     url = require('url');

function my_func()
	{exec('python3 test.py', (error, stdout, stderr) =>{
		  if (error) 
		{
		    console.error(`exec error: ${error}`);
		    return;
		  }
  		console.log(`${stdout}`);
		console.log("Executed the python code");
 		//console.log(`stderr: ${stderr}`);
		});	
	}

/*This function creates the server and listens to the specified port for connections*/  
http.createServer(function(request, response){
	var path = url.parse(request.url).pathname;
	if(path=="/getstring")
	{
		console.log("request recieved");
		// var string = choices[Math.floor(Math.random()*choices.length)];
		// console.log("string '" + string + "' chosen");
		response.writeHead(200, {"Content-Type": "text/plain"});

		fs.readFile('ajax_info.txt', function(err, my_file)
		{
			if(err){
			throw err};
			response.write(my_file);
			response.end();
		});
        console.log("string sent");
    	}
	else
	{
		fs.readFile('./index.html', function(err, file) {  
		if(err) {  
		// write an error response or nothing here  
		return;  
		}  
		response.writeHead(200, { 'Content-Type': 'text/html' });  
		response.end(file, "utf-8");  
		//response.use(express.static(__dirname + '/public'));
        });
    }
}).listen(8001);
console.log("server initialized");
