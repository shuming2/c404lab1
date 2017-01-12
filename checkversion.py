#!/usr/bin/env python

import requests
print requests.__version__

response = requests.get("https://www.google.com/")
print response.text
print response.status_code
