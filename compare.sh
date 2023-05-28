#!/bin/sh

cut -f 1 -d ',' img_links.txt | 
	sort -n |
	uniq > list
seq 1 262 |
	diff list - |
	grep "^>" |
	cut -f 2 -d ' ' |
	tee list |
	tr '\n' ',' |
	sed 's/.$//;s/.*/[&]/'
