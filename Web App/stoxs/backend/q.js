const express = require('express');
const cors = require('cors');
const mysql = require('mysql');
var http = require('http');

const app = express();

const SELECT_ALL = 'SELECT * FROM ';

// Connect to database
const connection = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: 'data1000',
    database: 'AMEX'
});

connection.connect(err => {
    if(err) {
      return err;
    }
    console.log("Connected")
});

// Query from database
var company;
var info = [];

function get_company(callback) {
  
  connection.query("SELECT * FROM COMPANY", (err, result) => {
    if (err) {
      return res.send(err)
    }
    else {
      callback(result.map(result=>({...result})))
      //callback(result)
    }
  });
}

get_company(function(err, data) {
  if(err) {
    console.log(err)
  } else {
    var len = data.length;
    console.log(data[6]);
    company = JSON.parse(data);

  }
})


//console.log(company)


/*
var mydate = '2019-04-29';
var len = 121;

function get_info(symbol, callback) {
  connection.query("SELECT closep, netchg, perchg, volume FROM " 
  + symbol + 
  "0 WHERE date=\'" + mydate + "\'", (err, result) => {
    if (err) {
      console.log(err)
    }
    else {
      try {
        var f = result[0];
        callback(result)
      }
      catch(err) {
        var e = 1;
      }     
    }
  });
}

var i;
for (i = 0; i < len; i++) {
  var x = {name: '', symbol: '', closep: '', netchg: '', perchg: '', volume: ''};
  x.name = company[i].name;
  x.symbol = company[i].symbol;
  get_info(x.symbol, function(err, data) {
    if(err) {
      console.log(err)
    } else {
      x.closep = data[0].closep;
      x.netchg = data[0].netchg;
      x.perchg = data[0].perchg;
      x.volume = data[0].volume;
    }
  });
  info.push(x);
}
*/
        
//console.log(info)

app.get('/Amex',(rq,res) =>{
  res.json({
    data: info
  })
})
// Send data
app.get('/',(rq,res) => {
  res.send('go to /[market] to see data');
});

app.use(cors());

app.listen(3002,() =>{
 // console.log('listening on port 3002')
});
