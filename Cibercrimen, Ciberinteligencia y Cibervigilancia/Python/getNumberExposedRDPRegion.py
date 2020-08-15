# -*- coding: utf-8 -*-

# Get the number of RDP exposed in a region.

import shodan

API_KEY = '' #JOSINES

api = shodan.Shodan(API_KEY)

query = "country:ES region:AN port:3389"

# Count elements.
result = api.count(query)

print("Hay", result['total'], "rdp expuestos en Andalucía.")