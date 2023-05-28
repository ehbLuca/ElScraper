#!/bin/sh
dir="images"
mkdir -p "$dir"
while read line 
do 
	id="$(echo $line | cut -f 1 -d ',')"
	link="$(echo $line | cut -f 2 -d ',')"
	echo "$id -> $link"
	wget --quiet --show-progress -O "$dir/$id.png" $link 
done < ./img_links.txt
