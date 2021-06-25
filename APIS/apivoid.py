#!/usr/bin/python3

# To run the script just use this:
# python3 /path/to/script.py "https://www.twitter.com/"

import requests
import urllib.parse
import json
import sys
import os
import cv2

decoded_url = ''
filename='/home/b00069517/College/Project-Code/Project-Code/MalciousQRs/zqwaqafirz.png'


image = cv2.imread(filename)

detector = cv2.QRCodeDetector()

data, vertices_array, binary_qrcode = detector.detectAndDecode(image)

if vertices_array is not None:
    decoded_url = data
    print("Extracted URL: " + decoded_url)
else:
    print("An error has occoured")


apivoid_key = "840635313ddc47cbcb70197a3d61676e09cf6347";

try:
   url = decoded_url;
except:
   print("Usage: " + os.path.basename(__file__) + " <url>")
   sys.exit(1)

def apivoid_urlrep(key, url):
   try:
      r = requests.get(url='https://endpoint.apivoid.com/urlrep/v1/pay-as-you-go/?key='+key+'&url='+urllib.parse.quote(url))
      return json.loads(r.content.decode())
   except:
      return ""

data = apivoid_urlrep(apivoid_key, url)

if(data):
   if(data.get('error')):
      print("Error: "+data['error'])
   else:
      print("URL: "+str(url))
      print("Risk Score: "+str(data['data']['report']['risk_score']['result']))
      #print("---")
      #print("Is Suspicious URL Pattern: "+str(data['data']['report']['security_checks']['is_suspicious_url_pattern']))
      #print("Is Suspicious Content: "+str(data['data']['report']['security_checks']['is_suspicious_content']))
      #print("Is Domain Blacklisted: "+str(data['data']['report']['security_checks']['is_domain_blacklisted']))
      #print("Is Suspicious Domain: "+str(data['data']['report']['security_checks']['is_suspicious_domain']))
      print("Is Masked File: "+str(data['data']['report']['security_checks']['is_masked_file']))
      print("Is Masked EXE File: "+str(data['data']['report']['security_checks']['is_masked_windows_exe_file']))
      print("Is Windows EXE File: "+str(data['data']['report']['security_checks']['is_windows_exe_file']))
      
      #print("__________")

      print("__________")
      check = int(data['data']['report']['risk_score']['result'])
      
      if (check >= 50):
         print("Flagged as Malcious")
      else:
         print("Appears Clean")
else:
   print("Error: Request failed")
   
   