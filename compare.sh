#!/bin/sh

seq 0 262 > list

cut -f 1 -d ',' img_links.txt |
	diff list - |
	grep "<" |
	cut -f 2 -d ' ' | tee list
