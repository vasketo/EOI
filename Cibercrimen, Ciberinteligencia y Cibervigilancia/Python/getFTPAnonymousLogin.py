# -*- coding: utf-8 -*-

# Get the IP LIST of FTP with anonymous login

import shodan

API_KEY = '' 

api = shodan.Shodan(API_KEY)

query = '"220" "230 Login successful." port:21 country:ES'

# Count elements.
result = api.count(query)

print("Hay", result['total'], "ftp con acceso anónimo en España.")

# Get elements
results = api.search(query)

print ("hosts number: " + str(len( results['matches'])))
for match in results['matches']:
    if match['ip_str'] is not None:
        print (match['ip_str'])
