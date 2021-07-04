import requests
import cv2

url = 'https://www.virustotal.com/vtapi/v2/url/report'

decoded_url = ''
filename='/home/b00069517/College/MscProject/MscProject/MalciousCodes2/Set_2_image_88.png'


AlienVault = ''
OpenPhish = ''
EmergingThreats= ''
Spamhaus = ''
CiscoTalosIPBlacklist = ''



image = cv2.imread(filename)

detector = cv2.QRCodeDetector()

data, vertices_array, binary_qrcode = detector.detectAndDecode(image)

if vertices_array is not None:
    decoded_url = data
    print(filename)
    print("Extracted URL: " + decoded_url)
else:
    print("An error has occoured")

params = {'apikey': '78cf33b2cd7327398c545a2e9901fdfaf69b213662155f5b03732c195f3356fb', 'resource':decoded_url}

response = requests.get(url, params=params)



try:
    AlienVault = response.json()['scans']['AlienVault']
    OpenPhish = AlienVault = response.json()['scans']['OpenPhish']
    EmergingThreats = response.json()['scans']['OpenPhish']
    Spamhaus = response.json()['scans']['Spamhaus']
    CiscoTalosIPBlacklist = response.json()['scans']['Cisco Talos IP Blacklist']

    print("-----")
   
    print("AlienVault : " + str(AlienVault))
    print("OpenPhish : " + str(OpenPhish))
    print("EmergingThreats : " + str(EmergingThreats))
    print("SpamHaus : " + str(Spamhaus))
    print("Talos: " + str(CiscoTalosIPBlacklist))

    print("-----")
except:
    print("-----")

    print("AlienVault : " + str(AlienVault))
    print("OpenPhish : " + str(OpenPhish))
    print("EmergingThreats : " + str(EmergingThreats))
    print("SpamHaus : " + str(Spamhaus))
    print("Talos: " + str(CiscoTalosIPBlacklist))

    print("-----")