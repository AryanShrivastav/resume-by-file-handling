

Aryan Shrivastav

from webbrowser import open_new as aap

a= open("index.html","w") r = """<!doctype html> 
<html> 
<head> 
<title>RESUME</title> 
<meta charset="utf-8"> 
<meta name="viewport" content="width=device-width, initial-scale=1"> 
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"> 
</head> 
<body style="padding-top: 5%; padding-left:10%; padding-right: 10%; "> 
<div class="col-xs-6" > 
<h1 style="text-align:center;"><u style="margin-bottom: 60px; ">MY RESUME</u></h1> 
<h2 style="text-transform: uppercase;" > Aryan Shrivastav</h2> 
<p style="font-size: 25px;"><a href="aryanshrivastav69@gmail.com">Gmailid : 
aryanshrivastav69@gmail.com </a></p>
<p style="font-size: 25px;">Contact No. : 9165275031</p> 
 
<p style="font-size: 25px;"> Address : 36 apoorva enclave ayodhya bypass bhopal</p> 

<p style="font-size: 25px"> DOB : 14-Dec-1999 </p> 
<h3 ><u>CAREER OBJECTIVE</u></h3> 
<p style="font-size: 25px;">To succeed in an environment of 
growth and excellence in computer science and to excel as a 
software engineer in the corporate paradigm and to pursue the 
opportunity of becoming a good coder.</p> 
<h2 id="two"><b>EDUCATION </b></h2> 
<table class="table" border="3" style="text-align:center;x"> 
<thead> 
<tr class="table-primary text-center col-lg" style="font-size: 
150%;"> <td><b>Qualification<b></td> 
<td><b>Institute</b></td> 
<td><b>Percentage / Grades</b></td> 
<td><b>Year</td></b> 
</tr> 
<tr style="font-size: 20px;"> 
<td>10th</td> 
<td>St.xaviers senior secondary school <br> awadhpuri bhopal </td> 
<td>76%</td> 
<td>2015</td> 
</tr> 
<tr style="font-size: 20px;"> 
<td>12th</td> 
<td>St.xaviers senior secondary school <br> awadhpuri 
bhopal</td> <td>76%</td><td>2017</td> 
</tr> 
<tr style="font-size: 20px;"> 
<td>1st Sem</td> 
<td>Barkatullah University Institute<br> Of Technology,Bhopal</td> 
<td>6.44 SGPA</td> 
<td>2019</td> 
</tr> 
<tr style="font-size: 20px;"> 
<td>2nd Sem</td> 
<td>Barkatullah University Institute<br> Of Technology , Bhopal</td> 
<td>6.64 SGPA</td> 
<td>2019</td> 
</tr> 
</thead></div> 
</table> 
<h3 style="text-transform: uppercase;"><b>Key 
Skills</b></h3> <ol> 
<h4 style="text-transform: uppercase;"><li> 
html</h4> <div class="progress"> 
<div class="progress-bar progress-bar-successs" role="progressbar" aria- 
vlauenow="60" aria-valuemin="0" aria-valuemax="100" style="width: 60%; background-color: 
green;"></div> 
</div></li> 
<h4 style="text-transform: uppercase;"><li> 
python</h4> <div class="progress"> 
<div class="progress-bar " role="progressbar" aria-vlauenow="60" aria-valuemin="0" aria- 
valuemax="100" style="width: 30%;background-color: green;"></div> 
</div> 
</li>
<h4> <li> C++</h4> 
<div class="progress progress-striped"><div class="progress-bar" aria-vlauenow="60" aria-valuemin="0" aria-valuemax="100" 
style="width: 30%; background-color: green;"></div> </div> 
</li>
<h4><li> C</h4> 
<div class="progress progress-striped"> 
<div class="progress-bar" aria-vlauenow="60" aria-valuemin="0" aria-valuemax="100" 
style="width: 30%; background-color: green;"></div> 
</div></li> 
</ol> 
<h4><b><u style="text-transform: uppercase;">Langauges</u></b></h4> 
<ol style="font-size: 25px;"> 
<li> English</li> 
<li>Hindi</li> 
</ol> 
<h3><b><u>HOBBIES</u></b></h3> 
<ol style="font-size: 25px;"><li>Reading 
novels</li> <li>partaking in sports</li> 
<li>learning up on new technology </li> 
</ol>
<h3><u><b>PROJECTS</b></u> </h3> 
<p><b><h3>1st Sem :</h3> </b><span style="font-size: 25px;">It has made many c and 
c++ program and create one static website.So see on the my <a href = 
"https://github.com/AryanShrivastav/DS-sessional" >C and C++. </a> </span>.</p> 
<p><b><h3>2nd Sem :</h3></b><span style="font-size: 25px;">It has made many  
 python langauge create many programs see on the Github <a 
href="https://github.com/AryanShrivastav/python-programming-personal-">Python Programs.</a></span></p> 
<p><b><h3>3rd Sem :</b></h3><span style="font-size: 25px;"> First is to make Resume host in the google so click on this link <a 
href="https://aryanshrivastav.github.io/resume-by-file-handling/"> 
Resume.</a>. </p></span> 
<h3><u><b>WORK EXPERIENCE</u></b></h3> 
<p><span style="font-size: 25px;">Fresher</span></p> 
</div> 
</div> 
</div> 
</body> 
</html>"""
a.write(r)

a.close()

aap("index.html")
