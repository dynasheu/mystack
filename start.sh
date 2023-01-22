#!/bin/bash

FILE=/helpers/requiremnts_met
if [ -f "$FILE" ]; then
    python3 ./helpers/build.py
else 
    ./helpers/requirements.sh
fi


