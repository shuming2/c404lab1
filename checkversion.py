#!/usr/bin/env python

import requests
print requests.__version__

response = requests.get("https://raw.githubusercontent.com/shuming2/c404lab1/master/checkversion.py")
print response.text
print response.status_code
