#!/bin/sh

rm -r venv
python -m venv venv
source venv/bin/activate
./venv/bin/pip install -r requirements.txt
