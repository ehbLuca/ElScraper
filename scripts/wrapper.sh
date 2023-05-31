#!/bin/sh


# cleanup () {
# 	echo exit
# }

thisdir="$(realpath "$0" | xargs -I {} dirname "{}")"
list="$($thisdir/compare.sh)"

# trap cleanup EXIT INT

export DISPLAY=:99
Xvfb :99 &
XVFB_PID=$!

cd $thisdir/../src/
./env/bin/python main.py "$list"
