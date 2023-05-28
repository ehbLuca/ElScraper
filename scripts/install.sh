#!/bin/sh

dir="$(realpath $0 | xargs dirname)"

cd "$dir"/../src
python3 -m venv env
. ./env/bin/activate
pip3 install -r requirements.txt
