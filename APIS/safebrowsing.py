import cv2
import requests
import json


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



api_key = 'KEY_HERE'
url = "https://safebrowsing.googleapis.com/v4/threatMatches:find"
payload = {'client': {'clientId': "mycompany", 'clientVersion': "0.1"},
        'threatInfo': {'threatTypes': ["THREAT_TYPE_UNSPECIFIED","SOCIAL_ENGINEERING", "MALWARE","UNWANTED_SOFTWARE","POTENTIALLY_HARMFUL_APPLICATION"],

                       'platformTypes': ["ANY_PLATFORM"],
                       'threatEntryTypes': ["URL","THREAT_ENTRY_TYPE_UNSPECIFIED","EXECUTABLE"],
                       'threatEntries': [{'url': decoded_url }]}}
params = {'key': api_key}
r = requests.post(url, params=params, json=payload)
# Print response


#print(r) 
#print(r.json())


json_data = json.loads(r.text)

if json_data:
    
    print(json_data)
    print("malcious")

if not json_data:
    print("Not flagged as malcious")
