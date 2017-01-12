#!/user/bin/env python

import requests

#print requests.__version__

#response = requests.get("http://google.com/")

#print response.text
#print response.status_code

response = requests.get("https://raw.githubusercontent.com/Koukoula/cmput404w17lab1web/master/versionCheck.py")
print response.text
print response.status_code
