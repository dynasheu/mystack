#!/bin/bash

FILE=/helpers/requiremnts_met
if [ -f "$FILE" ]; then
    python ./helpers/build.py
else 
    ./helpers/requirements.sh
fi


