#!/bin/bash

for i in {1..100}; do
    cp "./config_${i}.json" ./config.json
    ./init.config
    
    # Ki?m tra xem t?p env_file c� t?n t?i kh�ng tru?c khi sao ch�p
    if [[ -f "./worker-data/env_file" ]]; then
        cp ./worker-data/env_file "./worker-data/env_file_$((i))"
    else
        echo "T?p env_file kh�ng t?n t?i."
    fi
done
