import requests
import json
import cv2
import time


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


print("SUBMISSION STATUS")

headers = {'API-Key':'0d990430-a76a-40fb-bded-a2cf26b2e156','Content-Type':'application/json'}
data = {"url": decoded_url, "visibility": "public"}
response = requests.post('https://urlscan.io/api/v1/scan/',headers=headers, data=json.dumps(data))


print(response)
print(response.json())

uuid = response.json()['uuid']


print("RESULTS")
print(uuid)

time.sleep(20)

r = requests.get("https://urlscan.io/api/v1/result/"+ uuid +"/")
print(r.json())
