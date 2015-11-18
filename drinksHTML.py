#  TITLE:    Web Server 
#  NOTE:     rendering HTML output to screens and onclick execute the Python Scripts
from bottle import get, post, request, run, load, os, install, sys, route, template 
from bottle_sqlite import SQLitePlugin
from Queue_Controller import addWebToQueue, removeFromQueue, userOrderQueue, createDeque

#script variables
serverIP = "localhost"           #---webpage IP
serverPort = 8888                #---port for page
database = "drinktionary.db"  

#gets database of drinks (ID's, Names, Quantities)
sqlite_plugin = SQLitePlugin(dbfile = database)
install(sqlite_plugin)

# get() the required HTML thats been requested
@route('/drinksHTML', method='get')
def drinks(db): #query the DB for names and ID's of the drinks to use for the HTMLbuttons
    global nameONE
    global nameTWO
    global nameTHREE
    global nameFOUR
    global nameFIVE
    c = db.execute('SELECT ID, NAME FROM drinks WHERE ID="1"') 
    row = c.fetchone()
    if row['NAME'] == '':
      nameONE = 'Plese Set Drink!'
    else:
      nameONE = row['NAME']
    
    c = db.execute('SELECT ID, NAME FROM drinks WHERE ID="2"')
    row = c.fetchone()
    if row['NAME'] == '':
      nameTWO = 'Plese Set Drink!'
    else:
      nameTWO = row['NAME']
    
    c = db.execute('SELECT ID, NAME FROM drinks WHERE ID="3"')
    row = c.fetchone()
    if row['NAME'] == '':
      nameTHREE = 'Plese Set Drink!'
    else:
      nameTHREE = row['NAME']
    
    c = db.execute('SELECT ID, NAME FROM drinks WHERE ID="4"')
    row = c.fetchone()
    if row['NAME'] == '':
      nameFOUR = 'Plese Set Drink!'
    else:
      nameFOUR = row['NAME']

    c = db.execute('SELECT ID, NAME FROM drinks WHERE ID="5"')
    row = c.fetchone()
    if row['NAME'] == '':
      nameFIVE = 'Plese Set Drink!'
    else:
      nameFIVE = row['NAME']

#mark up the page with a basic HTML frame with button variables    
    return '''
<style type="text/css">
body {
	background-color: #42463E;
}
button { 
  background-color:#C7BDAB;
}
h1, h2, h3 {
  color:#CCC;
  font-family: Arial, Helvetica, sans-serif;
}
</style>
<script type="text/javascript">
var tmonth=new Array("January","February","March","April","May","June","July","August","September","October","November","December");

function GetClock(){
var d=new Date();
var nmonth=d.getMonth(),ndate=d.getDate(),nyear=d.getYear();
if(nyear<1000) nyear+=1900;

var nhour=d.getHours(),nmin=d.getMinutes(),ap;
if(nhour==0){ap=" AM";nhour=12;}
else if(nhour<12){ap=" AM";}
else if(nhour==12){ap=" PM";}
else if(nhour>12){ap=" PM";nhour-=12;}

if(nmin<=9) nmin="0"+nmin;

document.getElementById('clockbox').innerHTML=""+tmonth[nmonth]+" "+ndate+", "+nyear+" "+nhour+":"+nmin+ap+"";
}

window.onload=function(){
GetClock();
setInterval(GetClock,1000);
}
</script>
<div id="clockbox" align='right' style="color:#CCC"></div>
<br><br><br><br><br>
<body>
<div id="title" align="center">
	<h1>Welcome to Drink Mixer</h1>
    <h3>Select an option below</h3>
</div><br>
<div align="center">
  <form action="/drinksHTML" method="post">
        <button style="width:200px; height:50px" style="color:Red;" name="submitButton:1">''', nameONE,'''</button>
        <button style="width:200px; height:50px" style="color: #C7BDAB;" name="submitButton:2">''', nameTWO,'''</button>
        <button style="width:200px; height:50px" style="color:#C7BDAB;" name="submitButton:3">''', nameTHREE,'''</button>
        <button style="width:200px; height:50px" style="color:#C7BDAB;" name="submitButton:4">''', nameFOUR,'''</button>
        <button style="width:200px; height:50px" style="color:#C7BDAB;" name="submitButton:5">''', nameFIVE,'''</button>
  </form>
</div>
<br><br><br><br><br><br>
<div align='center'>  
  <form action="/cancelDrink" method="post">
        <button style="width:200px; height:50px" style="color:#C7BDAB;" name="submitButton:10">Cancel A Drink</button>
  </form>
</div>  
</body>
</html>
    '''

#post() the return HTML after the onClick() functions and fulfil the required in the 'if' loop
@post('/drinksHTML')
def drinks_return():
   data = []
   for i in range(0, 5):
     if 'submitButton:1' in request.POST:
      drink_data = '1'
      data.append('1')
      addWebToQueue(nameONE)
      return('''<style type="text/css">
body {background-color: #42463E;}
h1, h2, h3 {color:#CCC; font-family: Arial, Helvetica, sans-serif;}
</style><meta http-equiv="Refresh" content="5"; url = "localhost:8888/drinksHTML" /><div align="center"><h2> Processing Drink Order, One Moment Please! </h2></div><div align="center"><h3>''' '''No.''', drink_data, ' - ', nameONE,'''</h3></div>''')
     
     if 'submitButton:2' in request.POST:
      drink_data = '2'
      data.append('2')
      addWebToQueue(nameTWO)
      return('''<style type="text/css">
body {background-color: #42463E;}
h1, h2, h3 {color:#CCC; font-family: Arial, Helvetica, sans-serif;}
</style><meta http-equiv="Refresh" content="5"; url = "localhost:8888/drinksHTML" /><div align="center"><h2> Processing Drink Order, One Moment Please! </h2></div><div align="center"><h3>''' '''No.''', drink_data, ' - ', nameTWO,'''</h3></div>''')
     
     if 'submitButton:3' in request.POST:
      drink_data = '3'
      data.append('3')
      addWebToQueue(nameTHREE)
      return('''<style type="text/css">
body {background-color: #42463E;}
h1, h2, h3 {color:#CCC; font-family: Arial, Helvetica, sans-serif;}
</style><meta http-equiv="Refresh" content="5"; url = "localhost:8888/drinksHTML" /><div align="center"><h2> Processing Drink Order, One Moment Please! </h2></div><div align="center"><h3>''' '''No.''', drink_data, ' - ', nameTHREE,'''</h3></div>''') 
     
     if 'submitButton:4' in request.POST:
      drink_data = '4'
      data.append('4')
      addWebToQueue(nameFOUR)
      return('''<style type="text/css">
body {background-color: #42463E; font-family: Arial, Helvetica, sans-serif;}
h1, h2, h3 {color:#CCC;}
</style><meta http-equiv="Refresh" content="5"; url = "localhost:8888/drinksHTML" /><div align="center"><h2> Processing Drink Order, One Moment Please! </h2></div><div align="center"><h3>''' '''No.''', drink_data, ' - ', nameFOUR,'''</h3></div>''') 
     
     if 'submitButton:5' in request.POST:
      drink_data = '5'
      data.append('5')
      addWebToQueue(nameFIVE)
      return('''<style type="text/css">
body {background-color: #42463E;}
h1, h2, h3 {color:#CCC; font-family: Arial, Helvetica, sans-serif;}
</style><meta http-equiv="Refresh" content="5"; url = "localhost:8888/drinksHTML" /><div align="center"><h2> Processing Drink Order, One Moment Please! </h2></div><div align="center"><h3>''' '''No.''', drink_data, ' - ', nameFIVE,'''</h3></div>''')


#To cancel drinks ----------------------------------------------- 

@route('/cancelDrink', method='post')
def drink_cansel():    
  global stringONE 
  global stringTWO
  global stringTHREE
  global dLegnth
  #dList = []
  createDeque()
  dList = userOrderQueue('Mr_Web')
  dLength = len(dList)
  if 'submitButton:10' in request.POST:
    if dLength == 0:
      stringONE = '<i>EMPTY</i>'
    elif dLength == 1 or 2:
      stringONE = (str(dList[0])[27:-1])
      
    if dLength == 1:
      stringTWO = '<i>EMPTY</i>'
    elif dLength == 2 or 3:
      stringTWO = (str(dList[1])[27:-1])
      
    if dLength == 2:
      stringTHREE = '<i>EMPTY</i>'
    elif dLength == 3:
      stringTHREE = (str(dList[2])[27:-1])
        
    return '''<style type="text/css">
body {background-color: #42463E;}
button {background-color:#C7BDAB;}
h1, h2 {color:#CCC; font-family: Arial, Helvetica, sans-serif;}
</style> 
  <div align='center'><h2>Cancel Drink Orders</h2></div>
  
  <div align='center'>
  <table border="1" cellspacing="0" bgcolor="#FFFFFF" align='center'>
  <tr align='center'>
    <td>DRINK ORDERS</td>
    <td>CANCEL BUTTON</td>
  </tr>
  <tr>
    <td>''', stringONE,'''</td>
    <td><form action="" method="post"><button style="width:200px; height:50px" name="submitButton:11">Cancel</button></form></td>
  </tr>
  <tr>
    <td>''', stringTWO,'''</td>
    <td><form action="" method="post"><button style="width:200px; height:50px" name="submitButton:12">Cancel</button></form></td>
    <tr>
    <td>''', stringTHREE,'''</td>
    <td><form action="" method="post"><button style="width:200px; height:50px" name="submitButton:13">Cancel</button></form></td>
  </tr>
</table>
</div>
'''

  if 'submitButton:11' in request.POST: 
    if stringONE == '<i>EMPTY</i>':
      return('''<style type="text/css">
  body {background-color: #42463E;}
    </style><br><br><div>QUEUE ERROR: No drink in queue slot</div>''')
    else:  
      removeOrderFromQueue((str(dList[0])[-4:-1]))
      return('''<style type="text/css">
  body {background-color: #42463E;}
  button {background-color:#C7BDAB;}
  h1, h2 {color:#CCC; font-family: Arial, Helvetica, sans-serif;}
  </style><div align="center"><h2>Drink Order Cancled - No.''', (str(dList[0])[-4:-1]),''' </h2></div>''')
   
       
  if 'submitButton:12' in request.POST:
    if stringTWO == '<i>EMPTY</i>':
      return('''<style type="text/css">
  body {background-color: #42463E;}
    </style><br><br><div>QUEUE ERROR: No drink in queue slot</div>''')
    else:
     removeOrderFromQueue((str(dList[1])[-4:-1]))
     return('''<style type="text/css">
  body {background-color: #42463E;}
  button {background-color:#C7BDAB;}
  h1, h2 {color:#CCC; font-family: Arial, Helvetica, sans-serif;}
    </style><div align="center"><h2>Drink Order Cancled - No.''', (str(dList[1])[-4:-1]),'''  </h2></div>''')
 
  
  if 'submitButton:13' in request.POST:
    if stringTHREE == '<i>EMPTY</i>':
      return('''<style type="text/css">
  body {background-color: #42463E;}
    </style><br><br><div>QUEUE ERROR: No drink in queue slot</div>''')
    else:
     removeOrderFromQueue((str(dList[2])[-4:-1]))
     return('''<style type="text/css">
  body {background-color: #42463E;}
  button {background-color:#C7BDAB;}
  h1, h2 {color:#CCC; font-family: Arial, Helvetica, sans-serif;}
    </style><div align="center"><h2>Drink Order Cancled - No.''', (str(dList[2])[-4:-1]),'''  </h2></div>''')
   
    



#send all the above info to the destination below.
run(host=serverIP, port=serverPort, debug=True)
