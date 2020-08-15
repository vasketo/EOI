# -*- encoding: utf-8 -*-

# Get number of devices afected by a vulnerability.

import shodan

# Configuration
API_KEY = ''
api = shodan.Shodan(API_KEY)

vulnerabilityQueries = ['vuln:MS17-010 country:ES', 'vuln:CVE-2014-0160 country:ES', 'vuln:CVE-2015-0204 country:ES']

for query in vulnerabilityQueries:

    result = api.count(query) 
    
    print(query.split()[0][5:],"Dispositivos afectados:", result['total'])
