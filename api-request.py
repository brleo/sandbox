##curl -v -X POST \
##      'https://cbkiwry0ej.execute-api.us-east-1.amazonaws.com/betaswap/' \
##      -H 'content-type: application/json, get-random-names-api-key:VRr3rdLDRc3Iove41JJQ6131EwoWrGt43AGM4nPo' \
##      -d '{ "table_name": "facebook_data_dj_full", "total_items": "100" }'

import json
import requests

from datetime import datetime

url     = 'https://cbkiwry0ej.execute-api.us-east-1.amazonaws.com/betaswap/'
payload = { "table_name": "facebook_data_dj_full", "requested_fields": "firstName,lastName", "total_items": "100" }
headers = { "content-type": "application/json", "get-random-names-api-key": "VRr3rdLDRc3Iove41JJQ6131EwoWrGt43AGM4nPo" }

for counter in range(0, 1000):
    
    start_date = datetime.now()
    
    request = requests.post(url, data=json.dumps(payload), headers=headers)
    
    end_date = datetime.now()
    elapsed_time = end_date - start_date
    
    print(str(counter + 1))
    print("Response: " + str(request.json))
    print("Operation took {}".format(elapsed_time))