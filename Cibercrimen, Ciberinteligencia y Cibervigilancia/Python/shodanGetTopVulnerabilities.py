# -*- encoding: utf-8 -*-

# Get TOP 10 verified vulnerabilities of Spain.

# -*- encoding: utf-8 -*-

import shodan

API_KEY =''

api = shodan.Shodan(API_KEY)

query = 'country:ES has_vuln:true'
facet = [ ('vuln.verified', 10) ]
result = api.count(query, facets=facet)

for facet in result['facets']:

    for pos,term in enumerate(result['facets'][facet]):

        print(pos+1, term['value'], "Cantidad", term['count'])
