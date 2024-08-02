import os as MOD_OS
import network as MOD_NETWORK
import time as MOD_TIME

#Connect to Wifi
GLOB_WLAN=MOD_NETWORK.WLAN(MOD_NETWORK.STA_IF)
GLOB_WLAN.active(True)
GLOB_WLAN.connect("atmyhome", "home4internet")

while not GLOB_WLAN.isconnected():
  pass

#firebase example
import ufirebase as firebase
firebase.setURL("https://callrecorder-7ffff-default-rtdb.firebaseio.com/")

firebase.addto("testsensor", 128)
firebase.addto("testsensor", 124)
firebase.addto("testsensor", 120, DUMP="tagname")
print(firebase.tagname) # retourne '-MY7GTy4pp2LSpQp5775' (exemple)
# #Put Tag1
# firebase.put("testtag", "1234", bg=0)
# 
# #Put Tag2
# firebase.put("lolval/testval", {"somenumbers": [1,2,3], "something": "lol"}, bg=0)
# 
# #Get Tag1
# firebase.get("testtag", "var1", bg=0)
# print("testtag: "+str(firebase.var1))
# 
# #Get Tag2
# def callbackfunc():
#   print("\nlolval_1: "+str(firebase.lolwhat["testval"]["somenumbers"])+
#   "\nlolval_2: "+str(firebase.lolwhat["testval"]["something"])+
#   