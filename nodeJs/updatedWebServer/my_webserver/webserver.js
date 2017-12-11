/*var http = require('http'),
    fs = require('fs');


fs.readFile('./index.html', function (err, html) {
    if (err) {
        throw err; 
    } 
	else{
 	__html=html};		//__html is a global variable
});      

function doThis(){
console.log("Finally successful");
};

http.createServer(function(request, response) {  
        response.writeHeader(200, {"Content-Type": "text/html"});  
        doThis();
	response.write(__html);
        response.end();  
    }).listen(8000);
*/
var http = require('http'),
      fs = require('fs'),
     url = require('url'),
 choices = ["hello world", "goodbye world"];

http.createServer(function(request, response){
    var path = url.parse(request.url).pathname;
    if(path=="/getstring"){
        console.log("request recieved");
       // var string = choices[Math.floor(Math.random()*choices.length)];
       // console.log("string '" + string + "' chosen");
        response.writeHead(200, {"Content-Type": "text/plain"});
	
	fs.readFile('ajax_info.txt', function(err, my_file){
	if(err){
	throw err};
			
	response.write(my_file);
	
        response.end();});
        console.log("string sent");
    }else{
        fs.readFile('./index.html', function(err, file) {  
            if(err) {  
                // write an error response or nothing here  
                return;  
            }  
            response.writeHead(200, { 'Content-Type': 'text/html' });  
            response.end(file, "utf-8");  
        });
    }
}).listen(8001);
console.log("server initialized");
