# -*- coding: utf-8 -*-

# Get the number of RDP exposed in a region.

import shodan

# Configuration
API_KEY = ''

api = shodan.Shodan(API_KEY)

query = 'country:ES region:AN'
facet = [ ('port', 10) ]
result = api.count(query, facets=facet)

for facet in result['facets']:

    for pos,term in enumerate(result['facets'][facet]):

        print(pos+1, ". Puerto:", term['value'], "Cantidad", term['count'])
