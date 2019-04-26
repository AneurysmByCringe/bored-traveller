# The Bored Traveller. Wanders around cyberspace until he or she's too tired.
# Created by AneurysmByCringe
# Things to fix:
#   1- 'out of range' error when the list is empty
#   2- get rid of confusion whether try & except is necessary

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import random

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Connects to requested website
url = input('Enter URL - ')
count = int(input('Enter max count (1-100) - '))
print('Heading to', url + '...')
html = urllib.request.urlopen(url, context = ctx).read()

for i in range(count):
    # cleans up the HTML code
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieves links
    tags = soup('a')
    addresses = list()
    for tag in tags:
        # get(key, default=None)
        link = str(tag.get('href', None))
        # only adds them into list if they are accessible
        if link.startswith('http' or 'https' or 'www') and '.php' not in link:
            addresses.append(link)
    # sets a new url by selecting from the list of addresses
    x = len(addresses)
    newurl = str(addresses[random.randint(0,(x-1))])
    # attempts to establish connection to next link
    try:
        url = newurl
        html = urllib.request.urlopen(url, context = ctx).read()
        print('Heading to', url + '...')
    except:
        break

print('Heading to', url + '...')
print('You have arrived at', url + '!')
