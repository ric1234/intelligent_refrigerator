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
//Send to
	if(path=="/getstring")
	{
		console.log("request recieved");
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
//Send the left image
	else if(path=="/img1")
	{
		var img = fs.readFileSync('images/pic01.jpg');
     		response.writeHead(200, {'Content-Type': 'image/jpg' });
     response.end(img, 'binary');
    	}
//Send the right image
	else if(path=="/img2")
	{
		var img = fs.readFileSync('images/pic02.jpg');
     		response.writeHead(200, {'Content-Type': 'image/jpg' });
     response.end(img, 'binary');
    	}
else if(path=="/img3")
	{
		var img = fs.readFileSync('images/pic03.jpg');
     		response.writeHead(200, {'Content-Type': 'image/jpg' });
     response.end(img, 'binary');
    	}
else if(path=="/picfridge")
	{
	console.log("request for picture recieved");
		

		fs.readFile('fridge_pic.html', function(err, my_file)
		{
			if(err){
			throw err};
			response.writeHead(200, {"Content-Type": "text/plain"});
			response.write(my_file);
			response.end();
			
		});
        console.log("")
    	}
//Send the CSS file
	else if(path=="/assets/css/main.css")
	{
		var css = fs.readFileSync('assets/css/main.css');
     		response.writeHead(200, {'Content-Type': 'text/css' });
     response.end(css);
    	}
//Send the main HTML page
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
