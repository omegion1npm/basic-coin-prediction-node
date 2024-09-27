# -*- coding: utf-8 -*-

import json

# �?nh nghia file g?c config.json
config_template = {
    "wallet": {
        "addressKeyName": "test1",
        "addressRestoreMnemonic": "...", 
        "alloraHomeDir": "",
        "gas": "auto",
        "gasAdjustment": 1.5,
        "nodeRpc": "http://65.108.204.245:32657/",
        "maxRetries": 10,
        "delay": 4,
        "submitTx": True
    },
    "worker": [
        {
              "topicId": 10,
              "inferenceEntrypointName": "api-worker-reputer",
              "loopSeconds": 5,
              "parameters": {
                  "InferenceEndpoint": "http://inference:8000/inference/{BlockHeight}"
              }
          }
    ]
}

# H�m d? t?o c�c file config
def generate_configs(num_files):
    for i in range(1, num_files + 1):
        # T?o b?n sao c?a template
        config_data = config_template.copy()
        
        # C?p nh?t "addressKeyName" cho t?ng file
        config_data['wallet']['addressKeyName'] = f'test{i}'
        
        # T�n file
        file_name = f'config_{i}.json'
        
        # Ghi n?i dung ra file json
        with open(file_name, 'w') as file:
            json.dump(config_data, file, indent=4)
        
        print(f'{file_name} created successfully.')

# G?i h�m d? t?o c�c file (v� d? t?o 10 file)
generate_configs(100)
