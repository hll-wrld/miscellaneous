const express = require('express');
const https = require('https');
const fs = require('fs');
const port = 3000;

var key = fs.readFileSync('certs/selfsigned.key');
var cert = fs.readFileSync('certs/selfsigned.crt');
var options = {
  key: key,
  cert: cert
};

app = express()

app.get('/', (req, res) => {
   res.send('Welcome');
});

var server = https.createServer(options, app);

server.listen(port, () => {
  console.log("server on port : " + port)
});
