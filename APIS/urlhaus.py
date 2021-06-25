import wget
import requests
import os
import cv2
import json

#wget -O- --post-data="url=http://www.google.com" https://urlhaus-api.abuse.ch/v1/url/

decoded_url = ''
filename='/home/b00069517/College/Project-Code/http.png'


image = cv2.imread(filename)

detector = cv2.QRCodeDetector()

data, vertices_array, binary_qrcode = detector.detectAndDecode(image)

if vertices_array is not None:
    decoded_url = data
    print("Extracted URL: " + decoded_url)
else:
    print("An error has occoured")

url = "http://178.175.78.145:52136/Mozi.m"

test_url="https://urlhaus-api.abuse.ch/v1/url/"

print(os.system('wget -O- --post-data="url='+decoded_url+'" %s' %test_url))