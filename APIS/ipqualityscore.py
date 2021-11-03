import requests
import json
import cv2
import urllib.parse

decoded_url = ''
filename='/home/b00069517/College/Project-Code/Project-Code/Non-Malcious QRs/youtube.com.png'
image = cv2.imread(filename)

detector = cv2.QRCodeDetector()

data, vertices_array, binary_qrcode = detector.detectAndDecode(image)

if vertices_array is not None:
    decoded_url = data
    print("Extracted URL: " + decoded_url)
else:
    print("An error has occoured")


encoded_decoded_url = urllib.parse.quote(decoded_url, safe='')

print(encoded_decoded_url)


r = requests.post("https://ipqualityscore.com/api/json/url/KEY_HERE/"+encoded_decoded_url)
print(r.json())


