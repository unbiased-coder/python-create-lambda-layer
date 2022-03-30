# layer is located in Python directory

import json
from layer import unbiased_coder_test_layer_function

def lambda_handler(event, context):
    unbiased_coder_test_layer_function()
