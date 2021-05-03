#!/bin/bash

makeArrayString() {
	echo $1 | sed 's/[][]//g' | sed 's/\,/ /g'
}

outputArrayVar() {
	local array=$1[@]
	printf '%s\n' "${!array}" | jq -R . | jq -s . > "/tmp/output/$1"
}

unquotedFile() {
	echo $* | sed 's/\"//g'
}

makedir(){
 [ -z $1 ] && return 
 mkdir -p $1 && echo "creating directory $1" && return 
 echo "error creating directory $1" && exit 1
}

makedir $data_dir
makedir $genome_dir
makedir $models_dir
makedir $fastq_dir
makedir $bam_dir

exit 0

