index_payload = {'properties': {'@timestamp': {'type': 'date', 'format': 'epoch_millis'}, 'test_field': {'type': 'text'}}}

req_headers = {'content-type': 'application/json'}

test_data = {'@timestamp': 1568682293174, 'test_field': 'test_value'}

params= {'refresh': 'true'}
