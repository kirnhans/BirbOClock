#!/bin/bash

set -e; set -u;

rm -rf venv
python -m venv venv
source venv/bin/activate
./venv/bin/pip install -r requirements.txt
