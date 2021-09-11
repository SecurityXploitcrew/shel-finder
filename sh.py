#SecurityXploitCrew
#-*- coding: utf-8 -*-

import requests as r
import datetime, time
v = datetime.datetime.now()
url = input("target ~> ")
t = 0
print(" ~Start Scanning in "+v.strftime("%d.%m.%Y %H:%M:%S"))
time.sleep(2)
print("")
array = [
   "wso.php",
   "alfa.php",
   "Alfa.php",
   "mini.php",
   "up.php",
   "b374k.php",
   "idx.php",
   "shel.php",
   "shell.php",
   "ganteng.php",
   "evil.php",
   "eviltwin.php",
   "ids.php",
   "indosec.php",
   "marijuana.php",
   "marjan.php",
   "indoxploit.php",
   "c99.php",
   "403.php",
   "bypass.php",
   "webadmin.php",
   "x.php",
   "up.phtml",
   "Alfa.phtml",
   "alfa.phtml",
   "shell.phtml",
   "shel.phtml",
   "403.phtml",
   "x.phtml",
   "marijuana.phtml",
   "up.php5",
   "up.php7",
   "upload.php",
   "idx.phtml",
   "bypass.phtml",
   "bypass.php5",
   "bypass.php7",
   "ganteng.phtml",
   "ganteng.php5",
   "gelay.php",     
]
for x in array:
	q = url + '/' + x
	c = r.get(q)
	if c.status_code == 200:
		t += 1
		print("[OK] : "+q)
	else:
	    print("ER : "+q)
print("")
print("result : ",str(t))