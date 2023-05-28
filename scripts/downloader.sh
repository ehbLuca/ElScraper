#!/bin/sh

dir="$(realpath $0 | xargs dirname)"
cd "$dir"/../out

img_dir="images"

mkdir -p "$img_dir"
while read line 
do 
	id="$(echo $line | cut -f 1 -d ',')"
	link="$(echo $line | cut -f 2 -d ',')"
	wget --no-clobber --quiet --show-progress -O "$img_dir/$id" $link 
done < ./img_links.txt
