# -*- coding: utf-8 -*-
import json
import re

def remove_invalid_chars(data):
    # Lo?i b? c�c k� t? kh�ng h?p l?
    return re.sub(r'[\x00-\x1F\x7F]', '', data)

for i in range(1, 101):
    filename = f'config_{i}.json'
    
    # �?c t?p JSON
    with open(filename, 'r', encoding='utf-8') as file:
        raw_data = file.read()
    
    # X�a c�c k� t? kh�ng h?p l?
    cleaned_data = remove_invalid_chars(raw_data)
    
    # Ph�n t�ch c� ph�p JSON
    data = json.loads(cleaned_data)
    
    # X�a kho?ng tr?ng ? cu?i chu?i addressRestoreMnemonic
    data['wallet']['addressRestoreMnemonic'] = data['wallet']['addressRestoreMnemonic'].rstrip()
    
    # Ghi l?i v�o t?p JSON
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)

print("Removed trailing whitespace from all files.")
