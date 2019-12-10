# Copyright 2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License").
# You may not use this file except in compliance with the License.
# A copy of the License is located at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# or in the "license" file accompanying this file. This file is distributed
# on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
# express or implied. See the License for the specific language governing
# permissions and limitations under the License.

# Description:
# This is a test fixture, which provides a fixed baseline upon which tests can reliably and repeatedly execute
# In particular, this file provides a Elasticsearch object with all things configured
# so that tests can use this to communicate with Elasticsearch.


index_payload = {'properties': {'@timestamp': {'type': 'date', 'format': 'epoch_millis'}, 'test_field': {'type': 'text'}}}

req_headers = {'content-type': 'application/json'}

test_data = {'@timestamp': 1568682293174, 'test_field': 'test_value'}

params= {'refresh': 'true'}
